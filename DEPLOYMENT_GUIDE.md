# Deployment Guide for AI-Powered Todo Chatbot

## Backend Deployment to Vercel

### Prerequisites
- Vercel account (sign up at https://vercel.com)
- Vercel CLI installed: `npm i -g vercel`
- Your project code pushed to a Git repository

### Steps to Deploy Backend

1. **Prepare your environment variables:**
   - Go to your Vercel dashboard
   - Navigate to your project settings
   - Add the following environment variables:
     - `OPENROUTER_API_KEY`: Your OpenRouter API key for LLM responses
     - `DATABASE_URL`: Your Neon database connection string
     - `ENVIRONMENT`: production

2. **Deploy using Vercel CLI:**
   ```bash
   cd C:\Users\CSC\Desktop\Hackathon-5-phases\Hackathon-2\phase-3\backend
   vercel --prod
   ```

3. **Or deploy directly from the Vercel dashboard:**
   - Go to https://vercel.com/dashboard
   - Click "New Project"
   - Connect your Git repository
   - Vercel will automatically detect this is a Python project
   - Make sure to set the build command to use the correct entry point
   - Add the environment variables during the setup process

### Backend API Endpoints
After deployment, your backend will be available at:
- Root: `https://your-project-name.vercel.app/`
- Health check: `https://your-project-name.vercel.app/health`
- Chat endpoint: `https://your-project-name.vercel.app/api/v1/conversations/{user_id}`

## Frontend Deployment to Vercel

### Steps to Deploy Frontend

1. **Update the frontend configuration:**
   In `frontend/src/config.js`, update the API_BASE_URL to point to your deployed backend:
   ```javascript
   API_BASE_URL: process.env.NEXT_PUBLIC_API_BASE_URL || 'https://your-backend-deployed-url.vercel.app'
   ```

2. **Set environment variables in Vercel:**
   - `NEXT_PUBLIC_API_BASE_URL`: The URL of your deployed backend API

3. **Deploy the frontend:**
   ```bash
   cd C:\Users\CSC\Desktop\Hackathon-5-phases\Hackathon-2\phase-3\frontend
   vercel --prod
   ```

## Features Included in Deployment

✅ **LLM Responses**: Using OpenRouter API for general questions when "OpenAI" is selected
✅ **Task Management**: Full CRUD operations for tasks
✅ **Database Integration**: Neon database for storing conversations and tasks
✅ **Multi-Provider Support**: Works with different AI model selectors
✅ **Real-time Chat Interface**: Interactive chatbot interface

## Configuration Notes

- The backend uses the `api.py` file as the entry point for Vercel
- CORS is configured to allow connections from Vercel deployments
- The application supports both general questions and task operations
- Database tables are created automatically on startup

## Troubleshooting

If you encounter issues after deployment:

1. **Check environment variables** are properly set in Vercel dashboard
2. **Verify CORS settings** if frontend can't connect to backend
3. **Review logs** in the Vercel dashboard for error details
4. **Confirm database connection** if using Neon database

## Post-Deployment Setup

1. Once both frontend and backend are deployed:
   - Update the frontend's config to point to the deployed backend URL
   - Test the chat functionality with both general questions and task operations
   - Verify that the OpenAI selector provides LLM responses
   - Confirm that task operations work correctly