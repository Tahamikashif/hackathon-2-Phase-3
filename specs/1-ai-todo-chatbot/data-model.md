# Data Model: AI-Powered Todo Chatbot

## Entity Definitions

### Task
Represents a user's task to be completed

**Fields**:
- `id` (Integer): Unique identifier for the task
- `user_id` (String): Identifier for the user who owns the task
- `title` (String, required): Title of the task
- `description` (String, optional): Detailed description of the task
- `completed` (Boolean): Status indicating if the task is completed
- `created_at` (DateTime): Timestamp when the task was created
- `updated_at` (DateTime): Timestamp when the task was last updated

**Relationships**:
- Belongs to a User (via user_id)

**Validation Rules**:
- Title must not be empty
- Title must be less than 255 characters
- Description must be less than 1000 characters if provided

### Conversation
Represents a session of interaction between a user and the AI assistant

**Fields**:
- `id` (Integer): Unique identifier for the conversation
- `user_id` (String): Identifier for the user who owns the conversation
- `created_at` (DateTime): Timestamp when the conversation was started
- `updated_at` (DateTime): Timestamp when the conversation was last updated

**Relationships**:
- Belongs to a User (via user_id)
- Has many Messages

**Validation Rules**:
- Must have a valid user_id

### Message
Represents individual exchanges within a conversation

**Fields**:
- `id` (Integer): Unique identifier for the message
- `conversation_id` (Integer): Reference to the conversation this message belongs to
- `user_id` (String): Identifier for the user who sent the message
- `role` (String): Role of the sender ('user' or 'assistant')
- `content` (String, required): Content of the message
- `created_at` (DateTime): Timestamp when the message was created

**Relationships**:
- Belongs to a Conversation (via conversation_id)
- Belongs to a User (via user_id)

**Validation Rules**:
- Content must not be empty
- Role must be either 'user' or 'assistant'
- Must reference a valid conversation_id

### User
Represents individuals using the system

**Fields**:
- `id` (String): Unique identifier for the user
- `email` (String): Email address of the user
- `name` (String, optional): Full name of the user
- `created_at` (DateTime): Timestamp when the user account was created
- `updated_at` (DateTime): Timestamp when the user account was last updated

**Relationships**:
- Has many Tasks
- Has many Conversations
- Has many Messages

**Validation Rules**:
- Email must be valid
- Email must be unique

## State Transitions

### Task State Transitions
- `pending` → `completed`: When a user marks a task as done
- `completed` → `pending`: When a user reopens a completed task (optional feature)

### Conversation State Transitions
- `active` → `archived`: When a conversation is archived after inactivity (optional feature)

## Relationships

```
User (1) ←→ (Many) Task
User (1) ←→ (Many) Conversation  
User (1) ←→ (Many) Message
Conversation (1) ←→ (Many) Message
```

## Indexes

- Task: Index on (user_id, completed) for efficient querying
- Conversation: Index on user_id for efficient retrieval
- Message: Index on conversation_id for efficient retrieval
- User: Index on email for authentication