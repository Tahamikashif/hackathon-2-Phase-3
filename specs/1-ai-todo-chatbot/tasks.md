# Task List: AI-Powered Todo Chatbot

**Feature**: 1-ai-todo-chatbot
**Created**: 2026-01-16
**Status**: Draft

## Implementation Strategy

This document breaks the approved `sp.plan` into **atomic, sequential tasks** suitable for execution by **Claude Code**. Each task is independently verifiable and must be completed in order. No manual coding is permitted.

The implementation follows an incremental approach:
- **Phase 1**: Repository and foundational setup
- **Phase 2**: Core data models and persistence
- **Phase 3**: MCP tools implementation (US1 - P1)
- **Phase 4**: AI agent and chat API (US1 - P1)
- **Phase 5**: Persistent conversation context (US2 - P1)
- **Phase 6**: Task operations via AI agent (US3 - P2)
- **Phase 7**: Frontend implementation
- **Phase 8**: Authentication integration
- **Phase 9**: Testing and validation
- **Phase 10**: Polish and delivery

## Phase 1: Repository and Foundation Setup

**Goal**: Create a clean project structure with foundational configuration

**Independent Test**: Repository structure matches spec and basic app starts without errors

**Tasks**:
- [X] T001 Create project structure with /frontend, /backend, /specs directories
- [X] T002 Add base README.md with project overview
- [X] T003 Create .gitignore for Python and Node.js projects
- [X] T004 Create environment variable templates (.env.example) for backend
- [X] T005 [P] Set up backend requirements.txt with FastAPI, SQLModel, OpenAI, MCP SDK
- [X] T006 [P] Set up frontend package.json with ChatKit dependencies

## Phase 2: Data Models and Persistence

**Goal**: Implement database models and setup

**Independent Test**: Database models compile without errors and migrations work

**Tasks**:
- [X] T007 Define Task model in backend/src/models/task.py with id, user_id, title, description, completed, timestamps
- [X] T008 Define Conversation model in backend/src/models/conversation.py with id, user_id, timestamps
- [X] T009 Define Message model in backend/src/models/message.py with id, conversation_id, user_id, role, content, timestamp
- [X] T010 Define User model in backend/src/models/user.py with id, email, name, timestamps
- [X] T011 Create database connection setup in backend/src/database.py
- [X] T012 Configure Alembic for database migrations in backend/
- [X] T013 Create initial migration for all models in backend/alembic/versions/
- [X] T014 Apply database migrations to Neon PostgreSQL

## Phase 3: MCP Tools Implementation (US1 - P1)

**Goal**: Implement Model Context Protocol tools for task management

**Independent Test**: MCP tools can be registered and invoked correctly

**Tasks**:
- [X] T015 [P] [US1] Set up MCP server foundation in backend/src/mcp_server.py
- [X] T016 [P] [US1] Implement add_task MCP tool in backend/src/tools/task_operations.py
- [X] T017 [P] [US1] Implement list_tasks MCP tool in backend/src/tools/task_operations.py
- [X] T018 [P] [US1] Implement complete_task MCP tool in backend/src/tools/task_operations.py
- [X] T019 [P] [US1] Implement delete_task MCP tool in backend/src/tools/task_operations.py
- [X] T020 [P] [US1] Implement update_task MCP tool in backend/src/tools/task_operations.py
- [X] T021 [US1] Register all MCP tools with the MCP server
- [X] T022 [US1] Test MCP tools individually with mock data

## Phase 4: AI Agent and Chat API (US1 - P1)

**Goal**: Create the AI agent and connect it to MCP tools

**Independent Test**: AI agent can accept natural language and invoke appropriate MCP tools

**Tasks**:
- [X] T023 Create OpenAI agent configuration in backend/src/agents/todo_agent.py
- [X] T024 Define system prompt for the agent with tool usage rules in backend/src/agents/prompts.py
- [X] T025 Connect agent to MCP tools in backend/src/agents/todo_agent.py
- [X] T026 Create chat API endpoint POST /api/{user_id}/chat in backend/src/api/chat.py
- [X] T027 Implement message persistence in chat endpoint
- [X] T028 Implement response and tool call return in chat endpoint
- [X] T029 Test basic chat functionality with simple commands

## Phase 5: Persistent Conversation Context (US2 - P1)

**Goal**: Ensure conversation context persists across server restarts

**Independent Test**: After server restart, AI remembers previous conversation context

**Tasks**:
- [X] T030 Implement conversation history retrieval in backend/src/api/chat.py
- [X] T031 Create new conversation if none exists in backend/src/api/chat.py
- [X] T032 Associate messages with conversation in backend/src/api/chat.py
- [X] T033 Test conversation continuity after server restart
- [X] T034 Validate message ordering in conversation history

## Phase 6: Task Operations via AI Agent (US3 - P2)

**Goal**: Ensure AI agent correctly interprets intent and performs task operations

**Independent Test**: Various natural language inputs result in correct MCP tool invocations

**Tasks**:
- [X] T035 Refine system prompt for better intent recognition in backend/src/agents/prompts.py
- [X] T036 Implement tool chaining capability in backend/src/agents/todo_agent.py
- [X] T037 Add confirmation behavior to agent responses in backend/src/agents/todo_agent.py
- [X] T038 Test add_task scenarios with various natural language inputs
- [X] T039 Test list_tasks scenarios with various natural language inputs
- [X] T040 Test complete_task scenarios with various natural language inputs
- [X] T041 Test delete_task scenarios with various natural language inputs
- [X] T042 Test update_task scenarios with various natural language inputs

## Phase 7: Frontend Implementation

**Goal**: Create user interface for the todo chatbot

**Independent Test**: User can interact with AI through the frontend interface

**Tasks**:
- [X] T043 Set up ChatKit frontend in frontend/src/
- [X] T044 Configure API endpoint connection in frontend/src/config.js
- [X] T045 Implement chat interface in frontend/src/components/ChatInterface.jsx
- [X] T046 Display messages and AI responses in frontend/src/components/MessageList.jsx
- [X] T047 Test frontend-backend integration
- [X] T048 Configure domain allowlist for hosted ChatKit

## Phase 8: Authentication Integration

**Goal**: Secure user data with authentication

**Independent Test**: Users can only access their own tasks and conversations

**Tasks**:
- [X] T049 Integrate Better Auth in backend/src/auth.py
- [X] T050 Bind user identity to user_id in API endpoints
- [X] T051 Enforce user-level data isolation in all database queries
- [X] T052 Test authentication and authorization flows
- [X] T053 Validate that unauthorized access is blocked

## Phase 9: Testing and Validation

**Goal**: Ensure all functionality works as specified

**Independent Test**: All success criteria from spec are met

**Tasks**:
- [X] T054 Create unit tests for backend components in backend/tests/
- [X] T055 Create integration tests for API endpoints in backend/tests/
- [X] T056 Test all natural language commands work correctly
- [X] T057 Test tool chaining scenarios
- [X] T058 Test error handling for invalid inputs
- [X] T059 Validate stateless behavior after server restart
- [X] T060 Run end-to-end tests for all user stories

## Phase 10: Polish and Delivery

**Goal**: Prepare the project for submission

**Independent Test**: Repository is judge-ready with complete documentation

**Tasks**:
- [X] T061 Finalize README with setup instructions and architecture explanation
- [X] T062 Document MCP tools and agent behavior in docs/
- [X] T063 Add API usage examples in docs/
- [X] T064 Verify all success criteria are met
- [X] T065 Clean up code and add necessary comments

## Dependencies

User stories can be completed in this order:
1. US1 (Natural Language Task Management) - Foundation for all other stories
2. US2 (Persistent Conversation Context) - Depends on US1
3. US3 (Task Operations via AI Agent) - Depends on US1

## Parallel Execution Opportunities

Within each user story, these components can be developed in parallel:
- [US1] Task models and MCP tools can be developed separately
- [US1] Different MCP tools (add_task, list_tasks, etc.) can be implemented in parallel
- [US2] Conversation persistence and message persistence can be developed separately
- [US7] Frontend components can be developed in parallel