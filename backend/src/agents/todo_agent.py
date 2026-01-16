import json
from typing import List, Dict, Any
import os
import re
from .prompts import SYSTEM_PROMPT

# Import for Gemini if available
try:
    import google.generativeai as genai
    from google.generativeai.types import GenerationConfig
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
except Exception:
    GEMINI_AVAILABLE = False

# Import for OpenAI
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
except Exception:
    OPENAI_AVAILABLE = False


class MockFunction:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


class MockToolCall:
    def __init__(self, id, function):
        self.id = id
        self.function = function


class MockResponse:
    def __init__(self, content="", tool_calls=None):
        self.content = content
        self.tool_calls = tool_calls or []

        # Add attributes that the API expects
        self.role = "assistant"


class TodoAgent:
    """
    AI agent that processes natural language input and selects appropriate MCP tools to fulfill user intent.
    Supports both OpenAI and Google Gemini models.
    """

    def __init__(self, model_provider="openai"):  # Default to openai for backward compatibility
        self.system_prompt = SYSTEM_PROMPT
        self.model_provider = model_provider

        # Initialize API clients based on provider
        if model_provider == "gemini" and GEMINI_AVAILABLE:
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key or api_key == "your_gemini_api_key_here" or api_key == "test_key" or api_key.startswith("AIzaSy") or len(api_key) < 30:
                # Use mock behavior if no valid API key is provided or using web API key
                # Note: AIzaSy... format is typically for browser-based APIs, not server-side Gemini API
                # Also check if key is too short to be valid
                print("Warning: GEMINI_API_KEY not properly configured for server use. Using mock responses.")
                self.use_mock = True
            else:
                try:
                    genai.configure(api_key=api_key)
                    # Configure the model with tools
                    self.model = genai.GenerativeModel(
                        model_name="gemini-1.5-pro-latest",
                        system_instruction=SYSTEM_PROMPT,
                        tools=self._get_gemini_tools()
                    )
                    self.use_mock = False
                except Exception as e:
                    print(f"Error initializing Gemini: {e}. Using mock responses.")
                    self.use_mock = True
        elif model_provider == "openai" and OPENAI_AVAILABLE:
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key or api_key == "test_key" or len(api_key) < 20 or api_key.startswith("sk-") and len(api_key) < 30:
                # Use mock behavior if using default test key or invalid key
                print("Warning: OPENAI_API_KEY not properly configured. Using mock responses.")
                self.use_mock = True
            else:
                try:
                    self.client = OpenAI()
                    self.use_mock = False
                except Exception as e:
                    print(f"Error initializing OpenAI: {e}. Using mock responses.")
                    self.use_mock = True
        else:
            # Fallback to mock behavior if neither provider is available
            print(f"Warning: {model_provider} provider not available. Using mock responses.")
            self.use_mock = True

    def _get_gemini_tools(self):
        """Define the tools available to Gemini"""
        return [
            {
                "name": "add_task",
                "description": "Create a new task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Identifier for the user creating the task"},
                        "title": {"type": "string", "description": "Title of the task"},
                        "description": {"type": "string", "description": "Detailed description of the task (optional)"}
                    },
                    "required": ["user_id", "title"]
                }
            },
            {
                "name": "list_tasks",
                "description": "Retrieve tasks for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Identifier for the user whose tasks to retrieve"},
                        "status": {"type": "string", "enum": ["all", "pending", "completed"], "description": "Filter tasks by status (defaults to 'all')"}
                    },
                    "required": ["user_id"]
                }
            },
            {
                "name": "complete_task",
                "description": "Mark a task as completed",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Identifier for the user who owns the task"},
                        "task_id": {"type": "integer", "description": "Unique identifier for the task to complete"}
                    },
                    "required": ["user_id", "task_id"]
                }
            },
            {
                "name": "delete_task",
                "description": "Delete a task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Identifier for the user who owns the task"},
                        "task_id": {"type": "integer", "description": "Unique identifier for the task to delete"}
                    },
                    "required": ["user_id", "task_id"]
                }
            },
            {
                "name": "update_task",
                "description": "Update task title or description",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Identifier for the user who owns the task"},
                        "task_id": {"type": "integer", "description": "Unique identifier for the task to update"},
                        "title": {"type": "string", "description": "New title for the task (optional)"},
                        "description": {"type": "string", "description": "New description for the task (optional)"}
                    },
                    "required": ["user_id", "task_id"]
                }
            }
        ]

    def _convert_messages_for_gemini(self, messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Convert messages from OpenAI format to Gemini format"""
        gemini_messages = []
        for msg in messages:
            role = "model" if msg["role"] == "assistant" else "user"
            gemini_messages.append({
                "role": role,
                "parts": [{"text": msg["content"]}]
            })
        return gemini_messages

    def _execute_tool_calls_gemini(self, response, user_id: str):
        """Execute tool calls from Gemini response"""
        tool_calls = []

        if hasattr(response.candidates[0], 'function_calls'):
            for function_call in response.candidates[0].function_calls:
                # Add user_id to function args if not present
                args_dict = {k: v for k, v in function_call.args.items()}
                if "user_id" not in args_dict:
                    args_dict["user_id"] = user_id

                tool_call = MockToolCall(
                    id=function_call.name,
                    function=MockFunction(
                        name=function_call.name,
                        arguments=json.dumps(args_dict)
                    )
                )
                tool_calls.append(tool_call)

        return tool_calls

    def _execute_tool_calls_openai(self, response, user_id: str):
        """Execute tool calls from OpenAI response"""
        tool_calls = []

        if hasattr(response, 'choices') and len(response.choices) > 0:
            choice = response.choices[0]
            if hasattr(choice, 'message') and hasattr(choice.message, 'tool_calls'):
                for tool_call in choice.message.tool_calls:
                    # Parse arguments and add user_id if not present
                    args_dict = json.loads(tool_call.function.arguments)
                    if "user_id" not in args_dict:
                        args_dict["user_id"] = user_id

                    mock_tool_call = MockToolCall(
                        id=tool_call.id,
                        function=MockFunction(
                            name=tool_call.function.name,
                            arguments=json.dumps(args_dict)
                        )
                    )
                    tool_calls.append(mock_tool_call)

        return tool_calls

    def run(self, messages: List[Dict[str, str]], tools: List[Dict[str, Any]]) -> MockResponse:
        """
        Run the agent with the provided messages and tools using the selected provider.

        Args:
            messages: List of messages in the conversation
            tools: List of available tools

        Returns:
            Response from the agent including any tool calls
        """
        # Extract user_id from the messages (should be consistent across all messages)
        user_id = 'default-user'
        for msg in messages:
            if 'user_id' in msg:
                user_id = msg['user_id']
                break

        if self.use_mock:
            # Use mock behavior when API keys are not properly configured
            last_user_message = messages[-1]['content'].lower() if messages else ""
            mock_response = self._simulate_agent_response(last_user_message, tools, user_id)
            return MockResponse(content=mock_response['content'], tool_calls=mock_response.get('tool_calls', []))
        elif self.model_provider == "gemini" and GEMINI_AVAILABLE:
            return self._run_with_gemini(messages, user_id=user_id)
        elif self.model_provider == "openai" and OPENAI_AVAILABLE:
            return self._run_with_openai(messages, tools)
        else:
            # Fallback to mock behavior
            last_user_message = messages[-1]['content'].lower() if messages else ""
            mock_response = self._simulate_agent_response(last_user_message, tools, user_id)
            return MockResponse(content=mock_response['content'], tool_calls=mock_response.get('tool_calls', []))

    def _run_with_gemini(self, messages: List[Dict[str, str]], user_id: str) -> MockResponse:
        """Run the agent using Google Gemini"""
        try:
            # Convert messages to Gemini format
            gemini_formatted_messages = self._convert_messages_for_gemini(messages)

            # Generate response with potential function calls
            response = self.model.generate_content(
                gemini_formatted_messages,
                generation_config=GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=1000
                )
            )

            # Extract content
            content = ""
            if response.candidates and response.candidates[0].content.parts:
                content = response.candidates[0].content.parts[0].text
            else:
                # If no content was generated, provide a default response
                content = "I'm here to help you manage your tasks. You can ask me to add, list, update, or complete tasks."

            # Extract and process tool calls
            tool_calls = self._execute_tool_calls_gemini(response, user_id)

            return MockResponse(content=content, tool_calls=tool_calls)
        except Exception as e:
            print(f"Error calling Gemini: {e}")
            # Instead of falling back to mock response, let's try to generate a response with Gemini directly
            try:
                # Get the last user message
                last_user_message = messages[-1]['content'] if messages else "Hello"

                # Try to get a response from Gemini without tools
                safety_settings = {
                    "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
                    "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
                    "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
                    "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
                }

                model_without_tools = genai.GenerativeModel(
                    model_name="gemini-1.5-pro-latest",
                    system_instruction=self.system_prompt,
                    safety_settings=safety_settings
                )

                response = model_without_tools.generate_content(
                    last_user_message,
                    generation_config=GenerationConfig(
                        temperature=0.7,
                        max_output_tokens=1000
                    )
                )

                content = response.text if response.text else "I'm here to help you manage your tasks. You can ask me to add, list, update, or complete tasks."

                return MockResponse(content=content, tool_calls=[])
            except Exception as e2:
                print(f"Secondary error calling Gemini: {e2}")
                # Fallback to mock response only if both attempts fail
                last_user_message = messages[-1]['content'].lower() if messages else ""
                mock_response = self._simulate_agent_response(last_user_message, [])
                return MockResponse(content=mock_response['content'], tool_calls=mock_response.get('tool_calls', []))

    def _run_with_openai(self, messages: List[Dict[str, str]], tools: List[Dict[str, Any]]) -> MockResponse:
        """Run the agent using OpenAI"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",  # You can change this to gpt-4 if preferred
                messages=messages,
                tools=tools,
                tool_choice="auto"
            )

            # Extract content
            content = response.choices[0].message.content or ""

            # Extract and process tool calls
            tool_calls = self._execute_tool_calls_openai(response, messages[0].get('user_id', 'default-user'))

            return MockResponse(content=content, tool_calls=tool_calls)
        except Exception as e:
            print(f"Error calling OpenAI: {e}")
            # Instead of falling back to mock response immediately, try without tools
            try:
                # Try to get a response from OpenAI without tools
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    tool_choice="none"  # Don't force tool use
                )

                # Extract content
                content = response.choices[0].message.content or "I'm here to help you manage your tasks. You can ask me to add, list, update, or complete tasks."

                return MockResponse(content=content, tool_calls=[])
            except Exception as e2:
                print(f"Secondary error calling OpenAI: {e2}")
                # Fallback to mock response only if both attempts fail
                last_user_message = messages[-1]['content'].lower() if messages else ""
                mock_response = self._simulate_agent_response(last_user_message, tools)
                return MockResponse(content=mock_response['content'], tool_calls=mock_response.get('tool_calls', []))

    def _simulate_agent_response(self, message: str, tools: List[Dict[str, Any]], user_id: str = "mock_user") -> Dict[str, Any]:
        """
        Simulate agent response based on message content (fallback method)
        """
        response = {"content": "", "tool_calls": []}

        # Pattern matching for different commands
        if any(word in message for word in ["add", "create", "new task", "remember"]):
            # Extract task title from message
            import re
            # Look for task after phrases like "called", "named", "to", "that", etc.
            # Handle both quoted and unquoted titles
            match = re.search(r'(?:called|named|to|that|for)\s+([\'"]?)(.*?)(?<!\\)\1(?=\s|$|,|\.|\?)', message)
            if match:
                task_title = match.group(2)  # Get the content inside the quotes
            else:
                # If no specific pattern matched, try to extract the most meaningful part
                # Remove common verbs and get the rest
                task_title = re.sub(r'^(add|create|make|remember|remind me to|need to|want to)\s+', '', message).strip()
                if not task_title:
                    task_title = "New task from: " + message[:50]

            # Create a mock tool call for add_task
            tool_call = MockToolCall(
                id='call_123',
                function=MockFunction(
                    name='add_task',
                    arguments=json.dumps({"title": task_title, "user_id": user_id})
                )
            )

            response["content"] = f"I've added the task '{task_title}' to your list."
            response["tool_calls"] = [tool_call]

        elif any(word in message for word in ["list", "show", "what", "do i have"]):
            # Create a mock tool call for list_tasks
            tool_call = MockToolCall(
                id='call_456',
                function=MockFunction(
                    name='list_tasks',
                    arguments=json.dumps({"user_id": user_id})
                )
            )

            response["content"] = "I'm retrieving your task list now."
            response["tool_calls"] = [tool_call]

        elif any(word in message for word in ["complete", "done", "finish", "finished"]):
            # Extract task info
            task_ref = message.replace("complete", "").replace("done", "").replace("finish", "").strip()
            if not task_ref or task_ref == "the":
                task_ref = "your task"

            # Create a mock tool call for complete_task
            tool_call = MockToolCall(
                id='call_789',
                function=MockFunction(
                    name='complete_task',
                    arguments=json.dumps({"task_id": 1, "user_id": user_id})  # Assuming task ID 1 exists
                )
            )

            response["content"] = f"I've marked '{task_ref}' as completed."
            response["tool_calls"] = [tool_call]

        elif any(word in message for word in ["delete", "remove", "cancel"]):
            # Extract task info
            task_ref = message.replace("delete", "").replace("remove", "").replace("cancel", "").strip()
            if not task_ref or task_ref == "the":
                task_ref = "your task"

            # Create a mock tool call for delete_task
            tool_call = MockToolCall(
                id='call_999',
                function=MockFunction(
                    name='delete_task',
                    arguments=json.dumps({"task_id": 1, "user_id": user_id})  # Assuming task ID 1 exists
                )
            )

            response["content"] = f"I've removed '{task_ref}' from your list."
            response["tool_calls"] = [tool_call]

        else:
            response["content"] = f"I understand you said: '{message}'. You can ask me to add, list, update, or complete tasks."

        return response

    def run_with_tool_execution(self, messages: List[Dict[str, str]], tools: List[Dict[str, Any]], user_id: str) -> MockResponse:
        """
        Run the agent and execute any tool calls using the selected provider

        Args:
            messages: List of messages in the conversation
            tools: List of available tools
            user_id: User ID to pass to tools

        Returns:
            Response from the agent including any tool calls and their results
        """
        # Get response from the appropriate provider
        response = self.run(messages, tools)

        # Execute any tool calls
        if response.tool_calls:
            # Process each tool call
            for tool_call in response.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                # Ensure user_id is in function args
                function_args["user_id"] = user_id

                # Execute the appropriate function based on the name
                import asyncio
                if function_name == "add_task":
                    from ..tools.task_operations import add_task
                    # Run the async function in the current event loop
                    try:
                        loop = asyncio.get_running_loop()
                    except RuntimeError:
                        # If no event loop is running, create a new one
                        tool_response = asyncio.run(add_task(**function_args))
                    else:
                        # If event loop is running, schedule the coroutine
                        import concurrent.futures
                        with concurrent.futures.ThreadPoolExecutor() as executor:
                            future = executor.submit(asyncio.run, add_task(**function_args))
                            tool_response = future.result()
                elif function_name == "list_tasks":
                    from ..tools.task_operations import list_tasks
                    try:
                        loop = asyncio.get_running_loop()
                    except RuntimeError:
                        tool_response = asyncio.run(list_tasks(**function_args))
                    else:
                        import concurrent.futures
                        with concurrent.futures.ThreadPoolExecutor() as executor:
                            future = executor.submit(asyncio.run, list_tasks(**function_args))
                            tool_response = future.result()
                elif function_name == "complete_task":
                    from ..tools.task_operations import complete_task
                    try:
                        loop = asyncio.get_running_loop()
                    except RuntimeError:
                        tool_response = asyncio.run(complete_task(**function_args))
                    else:
                        import concurrent.futures
                        with concurrent.futures.ThreadPoolExecutor() as executor:
                            future = executor.submit(asyncio.run, complete_task(**function_args))
                            tool_response = future.result()
                elif function_name == "delete_task":
                    from ..tools.task_operations import delete_task
                    try:
                        loop = asyncio.get_running_loop()
                    except RuntimeError:
                        tool_response = asyncio.run(delete_task(**function_args))
                    else:
                        import concurrent.futures
                        with concurrent.futures.ThreadPoolExecutor() as executor:
                            future = executor.submit(asyncio.run, delete_task(**function_args))
                            tool_response = future.result()
                elif function_name == "update_task":
                    from ..tools.task_operations import update_task
                    try:
                        loop = asyncio.get_running_loop()
                    except RuntimeError:
                        tool_response = asyncio.run(update_task(**function_args))
                    else:
                        import concurrent.futures
                        with concurrent.futures.ThreadPoolExecutor() as executor:
                            future = executor.submit(asyncio.run, update_task(**function_args))
                            tool_response = future.result()
                else:
                    tool_response = {"error": f"Unknown tool: {function_name}"}

                # Update the response content with tool result
                response.content += f" [Action: {function_name} completed with result: {tool_response}]"

        return response