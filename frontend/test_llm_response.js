// This is a frontend test script to simulate how the chat interface works
// This would typically run in the browser console or as a test

async function testLLMResponse() {
  console.log("Testing LLM response from frontend...");
  
  // Simulating the fetch call that happens in ChatInterface.jsx
  const userId = "test-user";
  const message = "Hello, how are you?";
  
  try {
    console.log("Sending message to backend:", message);
    
    const response = await fetch('http://localhost:8000/api/v1/conversations/' + userId, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message: message,
      }),
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    
    console.log("Received response from backend:");
    console.log("- Conversation ID:", data.conversation_id);
    console.log("- Response:", data.response);
    console.log("- Tool Calls:", data.tool_calls);
    
    // This is the LLM response you're looking for
    console.log("\nLLM Response:", data.response);
    
    // Test task operation too
    console.log("\n\nTesting task operation...");
    const taskResponse = await fetch('http://localhost:8000/api/v1/conversations/' + userId, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message: "Add a task to buy groceries",
      }),
    });
    
    if (!taskResponse.ok) {
      throw new Error(`HTTP error! status: ${taskResponse.status}`);
    }
    
    const taskData = await taskResponse.json();
    
    console.log("Task operation response:", taskData.response);
    console.log("Tool calls:", taskData.tool_calls);
    
  } catch (error) {
    console.error("Error in LLM response test:", error);
  }
}

// Run the test
testLLMResponse();