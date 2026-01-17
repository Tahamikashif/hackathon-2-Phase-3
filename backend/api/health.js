# api/health.js - Health check endpoint for Vercel
export default function handler(request, response) {
  response.status(200).json({ status: 'healthy' });
}

export const config = {
  runtime: 'edge',
};