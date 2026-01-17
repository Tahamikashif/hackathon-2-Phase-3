# api/index.js - Root endpoint for Vercel
export default function handler(request, response) {
  response.status(200).json({ message: 'Welcome to the AI-Powered Todo Chatbot API' });
}

export const config = {
  runtime: 'edge',
};