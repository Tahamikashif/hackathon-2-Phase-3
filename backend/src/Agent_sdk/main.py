from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio
from typing import Dict, Any, List, Optional
from sqlmodel import Session, select
import json
# Import database and models inside the methods to avoid circular imports during initialization

load_dotenv(override=True)

# Check if OpenAI Assistants API is available (this is part of the OpenAI API)
# Since the official OpenAI Agents SDK might not be available yet, we'll use assistants API directly
class OpenAIAgentSDK:
    """
    Wrapper for OpenAI Assistants API that integrates with the existing database and models
    Using OpenRouter API for LLM responses
    """

    def __init__(self, model_provider="openrouter"):
        if model_provider == "openrouter" or model_provider == "openai":
            openrouter_api = os.getenv("OPENROUTER_API_KEY")
            if not openrouter_api:
                raise ValueError("OPENROUTER_API_KEY not found in environment variables")

            self.client = AsyncOpenAI(api_key=openrouter_api, base_url="https://openrouter.ai/api/v1")
            # Use a more reliable OpenRouter model
            self.model = "openai/gpt-3.5-turbo"
        else:
            # For other providers, you would initialize differently
            openrouter_api = os.getenv("OPENROUTER_API_KEY")
            if not openrouter_api:
                raise ValueError("OPENROUTER_API_KEY not found in environment variables")

            self.client = AsyncOpenAI(api_key=openrouter_api, base_url="https://openrouter.ai/api/v1")
            # Default to a reliable model
            self.model = "openai/gpt-3.5-turbo"

        # Define a general purpose assistant
        self.general_assistant_instructions = """You are a helpful assistant that can answer general questions and help with tasks.
        You can handle both general queries and task management. For task management, you can:
        - Add new tasks
        - List existing tasks
        - Mark tasks as complete
        - Update task details
        - Delete tasks

        When a user wants to manage tasks, respond with structured JSON indicating the action to take.
        For general questions, provide helpful and accurate responses."""

    async def run_conversation(self, messages: List[Dict[str, str]], user_id: str) -> Dict[str, Any]:
        """
        Run a conversation using the OpenAI API through OpenRouter

        Args:
            messages: List of messages in the conversation
            user_id: User ID for the conversation

        Returns:
            Dictionary with response content and metadata
        """
        try:
            # Validate inputs
            if not messages or not isinstance(messages, list):
                raise ValueError("Messages must be a non-empty list of dictionaries")

            for msg in messages:
                if not isinstance(msg, dict) or 'role' not in msg or 'content' not in msg:
                    raise ValueError("Each message must be a dictionary with 'role' and 'content' keys")

            # Call the OpenRouter API with the conversation history
            response = await self.client.chat.completions.create(
                model=self.model,  # Using the model from the instance
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )

            response_text = response.choices[0].message.content

            # Ensure response is not None
            if response_text is None:
                response_text = "I couldn't generate a response to your message. Could you please try again?"

            # Try to parse potential tool calls from the response
            tool_calls = []
            # Look for JSON structures in the response that might indicate tool calls
            # This is a simplified approach - in a real implementation you'd want more robust parsing
            if response_text and '{' in response_text and '}' in response_text:
                try:
                    # Attempt to extract JSON from response
                    import re
                    json_matches = re.findall(r'\{[^{}]*\}', response_text)
                    for match in json_matches:
                        try:
                            parsed_json = json.loads(match)
                            if 'action' in parsed_json or 'function' in parsed_json:
                                tool_calls.append(parsed_json)
                        except json.JSONDecodeError:
                            continue
                except Exception as parse_error:
                    print(f"Error parsing potential tool calls from response: {parse_error}")
                    # Continue without tool calls if parsing fails

            return {
                "content": response_text,
                "tool_calls": tool_calls,
                "usage": {
                    "prompt_tokens": response.usage.prompt_tokens if response and response.usage else 0,
                    "completion_tokens": response.usage.completion_tokens if response and response.usage else 0,
                    "total_tokens": response.usage.total_tokens if response and response.usage else 0
                }
            }
        except Exception as e:
            print(f"Error calling OpenRouter API: {e}")
            return {
                "content": f"Sorry, I encountered an error processing your request: {str(e)}",
                "tool_calls": [],
                "usage": {}
            }

    async def process_general_question_with_history(self, messages: List[Dict[str, str]], user_id: str) -> Dict[str, Any]:
        """
        Process a general question using the OpenAI API with conversation history

        Args:
            messages: List of messages in the conversation (including history)
            user_id: User ID for the conversation

        Returns:
            Dictionary with response content and metadata
        """
        # Add system message at the beginning to guide the assistant
        system_message = {
            "role": "system",
            "content": self.general_assistant_instructions
        }

        # Prepend system message to the conversation
        full_messages = [system_message] + messages

        result = await self.run_conversation(full_messages, user_id)
        return result


# Function to determine if a message is a general question or task-related
def is_general_question(message: str) -> bool:
    """
    Determine if a message is a general question or task-related request

    Args:
        message: User's message

    Returns:
        Boolean indicating if the message is a general question
    """
    message_lower = message.lower().strip()

    # Phrases that indicate task-related requests (more specific than just single words)
    task_indicators = [
        "add task", "create task", "new task", "remember to", "add a task", "create a task",
        "list tasks", "show tasks", "what tasks", "do i have", "my tasks",
        "complete task", "finish task", "done with", "mark as complete", "mark as done",
        "delete task", "remove task", "cancel task",
        "update task", "change task", "modify task",
        "task:", "todo:", "to-do:", "to do:",
        "add ", "create ", "new ", "task"
    ]

    # Check for task-related phrases
    for indicator in task_indicators:
        if indicator in message_lower:
            return False

    # Additional check: if message contains task-related keywords combined with action words
    action_words = ["add", "create", "list", "show", "complete", "finish", "delete", "remove", "update", "change"]
    task_related_contexts = ["task", "todo", "to do", "to-do"]

    words = message_lower.split()
    for i, word in enumerate(words):
        if word in action_words and i < len(words) - 1:
            next_word = words[i + 1]
            # Check if the action word is followed by a task-related term
            for context in task_related_contexts:
                if context in next_word or next_word in ["task", "tasks", "todo"]:
                    return False

    # If none of the task indicators are found, treat as a general question
    return True


async def main():
    while True:
        msg = input("Enter your sentences (or 'exit' to quit): ")

        if msg.lower() in ["exit", "quit"]:
            break

        # Determine if it's a general question
        if is_general_question(msg):
            try:
                agent_sdk = OpenAIAgentSDK()
                # Create a simple message history for console testing
                messages = [{"role": "user", "content": msg}]
                result = await agent_sdk.process_general_question_with_history(messages, "console_user")
                print(f"General Assistant: {result['content']}")

                if result['tool_calls']:
                    print(f"Tool calls detected: {result['tool_calls']}")
            except ValueError as e:
                print(f"Configuration error: {e}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("This appears to be a task-related request. Use the main API for task operations.")

if __name__ == "__main__":
    asyncio.run(main())