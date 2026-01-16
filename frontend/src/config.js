// Frontend configuration
const config = {
  // Backend API URL
  API_BASE_URL: process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:5000/api',

  // Timeout for API requests (in milliseconds)
  REQUEST_TIMEOUT: 30000,

  // Retry settings
  MAX_RETRIES: 3,
};

export default config;