// Frontend configuration
const config = {
  // Backend API URL
  API_BASE_URL: process.env.NEXT_PUBLIC_API_BASE_URL || 'https://backend-ebon-beta-29.vercel.app',

  // Timeout for API requests (in milliseconds)
  REQUEST_TIMEOUT: 30000,

  // Retry settings
  MAX_RETRIES: 3,
};

export default config;