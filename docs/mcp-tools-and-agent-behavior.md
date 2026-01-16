# AI-Powered Todo Chatbot Documentation

## MCP Tools

The system implements several Model Context Protocol (MCP) tools for task management:

### add_task
- **Purpose**: Create a new task
- **Parameters**:
  - `user_id` (string, required): Identifier for the user creating the task
  - `title` (string, required): Title of the task
  - `description` (string, optional): Detailed description of the task
- **Returns**: Object with `task_id`, `status`, and `title`

### list_tasks
- **Purpose**: Retrieve tasks for a user
- **Parameters**:
  - `user_id` (string, required): Identifier for the user whose tasks to retrieve
  - `status` (string, optional): Filter tasks by status ("all", "pending", "completed") - defaults to "all"
- **Returns**: Array of task objects with properties

### complete_task
- **Purpose**: Mark a task as completed
- **Parameters**:
  - `user_id` (string, required): Identifier for the user who owns the task
  - `task_id` (integer, required): Unique identifier for the task to complete
- **Returns**: Object with `task_id`, `status`, and `title`

### delete_task
- **Purpose**: Delete a task
- **Parameters**:
  - `user_id` (string, required): Identifier for the user who owns the task
  - `task_id` (integer, required): Unique identifier for the task to delete
- **Returns**: Object with `task_id`, `status`, and `title`

### update_task
- **Purpose**: Update task title or description
- **Parameters**:
  - `user_id` (string, required): Identifier for the user who owns the task
  - `task_id` (integer, required): Unique identifier for the task to update
  - `title` (string, optional): New title for the task
  - `description` (string, optional): New description for the task
- **Returns**: Object with `task_id`, `status`, and `title`

## Agent Behavior

The AI agent follows these rules:

1. Always use the appropriate tool to perform task operations
2. When a user wants to add a task, use the add_task tool
3. When a user wants to see their tasks, use the list_tasks tool
4. When a user wants to complete a task, use the complete_task tool
5. When a user wants to delete a task, use the delete_task tool
6. When a user wants to update a task, use the update_task tool
7. Always confirm actions in friendly language to users
8. If a user refers to a task by name, use list_tasks first to find the task ID
9. Handle errors gracefully and inform the user appropriately
10. If a user request is unclear, ask for clarification
11. You can chain multiple tools in a single response if needed (e.g., list tasks then delete one)
12. Be specific with task IDs when performing operations
13. Always include the user_id in tool calls

## API Usage Examples

### Starting a conversation:
```bash
curl -X POST http://localhost:8000/api/user123/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "I need to buy groceries"}'
```

### Continuing a conversation:
```bash
curl -X POST http://localhost:8000/api/user123/chat \
  -H "Content-Type: application/json" \
  -d '{"conversation_id": 1, "message": "What else do I need to do?"}'
```

## Architecture

The system follows a stateless architecture where all conversation and task state is persisted in the database. The AI agent uses MCP tools to perform task operations.

### Request Flow

1. Client sends message to `POST /api/{user_id}/chat`
2. Backend fetches conversation + messages from database
3. Message history is assembled for the agent
4. User message is persisted
5. Agent is executed with MCP tools
6. Agent invokes MCP tool(s) as needed
7. Tool results are returned to the agent
8. Assistant response is generated
9. Assistant response and tool calls are persisted
10. Response is returned to client