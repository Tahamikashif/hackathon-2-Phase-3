# MCP Tool Contracts: AI-Powered Todo Chatbot

## Overview
This document defines the Model Context Protocol (MCP) tools that will be exposed to the AI agent for task management operations.

## Tool: add_task

**Purpose**: Create a new task

**Input Parameters**:
- `user_id` (string, required): Identifier for the user creating the task
- `title` (string, required): Title of the task
- `description` (string, optional): Detailed description of the task

**Output**:
- `task_id` (integer): Unique identifier for the created task
- `status` (string): Status of the task ("pending")
- `title` (string): Title of the task

**Example Request**:
```json
{
  "user_id": "user-123",
  "title": "Buy groceries",
  "description": "Milk, eggs, bread"
}
```

**Example Response**:
```json
{
  "task_id": 42,
  "status": "pending",
  "title": "Buy groceries"
}
```

## Tool: list_tasks

**Purpose**: Retrieve tasks for a user

**Input Parameters**:
- `user_id` (string, required): Identifier for the user whose tasks to retrieve
- `status` (string, optional): Filter tasks by status ("all", "pending", "completed") - defaults to "all"

**Output**:
- Array of task objects with properties:
  - `task_id` (integer): Unique identifier for the task
  - `status` (string): Status of the task ("pending" or "completed")
  - `title` (string): Title of the task
  - `description` (string, optional): Description of the task

**Example Request**:
```json
{
  "user_id": "user-123",
  "status": "pending"
}
```

**Example Response**:
```json
[
  {
    "task_id": 42,
    "status": "pending",
    "title": "Buy groceries",
    "description": "Milk, eggs, bread"
  },
  {
    "task_id": 43,
    "status": "pending",
    "title": "Call mom",
    "description": "Check on her health"
  }
]
```

## Tool: complete_task

**Purpose**: Mark a task as completed

**Input Parameters**:
- `user_id` (string, required): Identifier for the user who owns the task
- `task_id` (integer, required): Unique identifier for the task to complete

**Output**:
- `task_id` (integer): Unique identifier for the task
- `status` (string): Updated status of the task ("completed")
- `title` (string): Title of the task

**Example Request**:
```json
{
  "user_id": "user-123",
  "task_id": 42
}
```

**Example Response**:
```json
{
  "task_id": 42,
  "status": "completed",
  "title": "Buy groceries"
}
```

## Tool: delete_task

**Purpose**: Delete a task

**Input Parameters**:
- `user_id` (string, required): Identifier for the user who owns the task
- `task_id` (integer, required): Unique identifier for the task to delete

**Output**:
- `task_id` (integer): Unique identifier for the task
- `status` (string): Status of the task at deletion ("pending" or "completed")
- `title` (string): Title of the task

**Example Request**:
```json
{
  "user_id": "user-123",
  "task_id": 42
}
```

**Example Response**:
```json
{
  "task_id": 42,
  "status": "pending",
  "title": "Buy groceries"
}
```

## Tool: update_task

**Purpose**: Update task title or description

**Input Parameters**:
- `user_id` (string, required): Identifier for the user who owns the task
- `task_id` (integer, required): Unique identifier for the task to update
- `title` (string, optional): New title for the task
- `description` (string, optional): New description for the task

**Output**:
- `task_id` (integer): Unique identifier for the task
- `status` (string): Current status of the task ("pending" or "completed")
- `title` (string): Updated title of the task

**Example Request**:
```json
{
  "user_id": "user-123",
  "task_id": 42,
  "title": "Buy groceries and household items"
}
```

**Example Response**:
```json
{
  "task_id": 42,
  "status": "pending",
  "title": "Buy groceries and household items"
}
```