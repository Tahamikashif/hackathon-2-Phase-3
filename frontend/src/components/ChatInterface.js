import React, { useState, useRef, useEffect } from 'react';
import MessageList from './MessageList';
import config from '../config';

const ChatInterface = ({ userId: propUserId }) => {
  const [userId, setUserId] = useState(propUserId || '');
  const [isAuthenticated, setIsAuthenticated] = useState(!!propUserId);
  const [showAuthForm, setShowAuthForm] = useState(!propUserId);
  const [authEmail, setAuthEmail] = useState('');
  const [authPassword, setAuthPassword] = useState('');
  const [authMode, setAuthMode] = useState('login'); // 'login' or 'signup'
  const [messages, setMessages] = useState([
    {
      id: 1,
      role: 'assistant',
      content: 'Welcome to the Todo AI Chatbot! I\'m your intelligent task management assistant. You can ask me to add, list, update, or complete tasks using natural language. Try saying "Add a task to buy groceries", "Show my tasks", or "Mark groceries as done".',
      timestamp: new Date().toISOString()
    }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [modelProvider, setModelProvider] = useState('openai'); // Default to openai
  const messagesEndRef = useRef(null);

  const handleAuthSubmit = (e) => {
    e.preventDefault();
    if ((authEmail.trim() && authPassword.trim()) || propUserId) {
      // Use provided userId or derive from email
      const derivedUserId = propUserId || authEmail.trim() || `user_${Date.now()}`;

      setUserId(derivedUserId);
      setIsAuthenticated(true);
      setShowAuthForm(false);

      // Store user info in localStorage for persistence
      localStorage.setItem('chatbot_user_id', derivedUserId);
      localStorage.setItem('chatbot_user_email', authEmail.trim());
    }
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
    setShowAuthForm(true);
    setUserId('');
    setAuthEmail('');
    setAuthPassword('');
    setMessages([{
      id: 1,
      role: 'assistant',
      content: 'Hello! I\'m your AI task assistant. Please authenticate to start chatting.',
      timestamp: new Date().toISOString()
    }]);
    localStorage.removeItem('chatbot_user_id');
    localStorage.removeItem('chatbot_user_email');
  };

  // Scroll to bottom of messages
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading || !isAuthenticated) return;

    // Add user message to the chat
    const userMessage = {
      id: Date.now(),
      role: 'user',
      content: inputValue,
      timestamp: new Date().toISOString()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Send message to backend
      const response = await fetch(`${config.API_BASE_URL}/${userId}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: inputValue,
          model_provider: modelProvider,  // Include the selected model provider
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();

      // Add assistant response to the chat
      const assistantMessage = {
        id: Date.now() + 1,
        role: 'assistant',
        content: data.response,
        toolCalls: data.tool_calls,
        timestamp: new Date().toISOString()
      };

      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Error sending message:', error);

      // Add error message to the chat
      const errorMessage = {
        id: Date.now() + 1,
        role: 'system',
        content: 'Sorry, there was an error processing your request. Please try again.',
        timestamp: new Date().toISOString()
      };

      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-full bg-gradient-to-br from-slate-50 to-slate-100 rounded-2xl shadow-lg border border-slate-200">
      {!isAuthenticated ? (
        <div className="flex flex-col items-center justify-center h-full p-6">
          <div className="bg-white p-8 rounded-2xl shadow-xl w-full max-w-md border border-slate-200">
            <div className="text-center mb-6">
              <div className="mx-auto bg-gradient-to-r from-indigo-600 to-blue-700 w-16 h-16 rounded-full flex items-center justify-center mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
              </div>
              <h2 className="text-2xl font-bold text-slate-800">Welcome to TaskBot AI</h2>
              <p className="text-slate-600 mt-2">{authMode === 'login' ? 'Sign in to start chatting with your AI assistant' : 'Create an account to start chatting with your AI assistant'}</p>
            </div>

            <form onSubmit={handleAuthSubmit} className="space-y-5">
              <div>
                <label htmlFor="email" className="block text-sm font-medium text-slate-700 mb-2">Email Address</label>
                <div className="relative">
                  <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                  </div>
                  <input
                    type="email"
                    id="email"
                    value={authEmail}
                    onChange={(e) => setAuthEmail(e.target.value)}
                    placeholder="Enter your email"
                    className="w-full pl-10 pr-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all duration-300"
                    required
                  />
                </div>
              </div>

              <div>
                <label htmlFor="password" className="block text-sm font-medium text-slate-700 mb-2">Password</label>
                <div className="relative">
                  <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                    </svg>
                  </div>
                  <input
                    type="password"
                    id="password"
                    value={authPassword}
                    onChange={(e) => setAuthPassword(e.target.value)}
                    placeholder="Enter your password"
                    className="w-full pl-10 pr-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all duration-300"
                    required
                  />
                </div>
              </div>

              <button
                type="submit"
                className="w-full bg-gradient-to-r from-indigo-600 to-blue-700 text-white py-3 rounded-lg hover:from-indigo-700 hover:to-blue-800 transition-all duration-300 shadow-md hover:shadow-lg transform hover:-translate-y-0.5 flex items-center justify-center"
              >
                <span className="font-medium">{authMode === 'login' ? 'Sign In' : 'Sign Up'}</span>
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
              </button>
            </form>

            <div className="mt-5 text-center">
              <button
                type="button"
                onClick={() => setAuthMode(authMode === 'login' ? 'signup' : 'login')}
                className="text-indigo-600 hover:text-indigo-800 text-sm font-medium inline-flex items-center"
              >
                {authMode === 'login' ? "Don't have an account? " : "Already have an account? "}
                <span className="ml-1 underline">{authMode === 'login' ? 'Sign up' : 'Sign in'}</span>
              </button>
            </div>

            <div className="mt-8 pt-6 border-t border-slate-200">
              <p className="text-xs text-slate-500 text-center">By signing in, you agree to our Terms and Privacy Policy</p>
            </div>
          </div>
        </div>
      ) : (
        <>
          <div className="flex-grow overflow-y-auto mb-3 p-4">
            <div className="flex justify-between items-center mb-4 p-3 bg-gradient-to-r from-slate-100 to-slate-50 rounded-xl border border-slate-200">
              <div className="flex items-center">
                <div className="bg-gradient-to-r from-indigo-100 to-blue-100 p-2 rounded-lg mr-3">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                </div>
                <div>
                  <div className="text-xs text-slate-500">Signed in as</div>
                  <div className="text-sm font-semibold text-slate-800 truncate max-w-[160px]">{localStorage.getItem('chatbot_user_email') || userId}</div>
                </div>
              </div>
              <button
                onClick={handleLogout}
                className="text-xs bg-gradient-to-r from-red-500 to-red-600 text-white px-4 py-2 rounded-lg hover:from-red-600 hover:to-red-700 transition-all duration-300 shadow-sm flex items-center"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                </svg>
                Logout
              </button>
            </div>
            <MessageList messages={messages} />
            <div ref={messagesEndRef} />
          </div>

          <form onSubmit={handleSubmit} className="mt-auto p-4 bg-gradient-to-b from-white to-slate-50 rounded-b-2xl border-t border-slate-200">
            <div className="relative rounded-xl border border-slate-300 overflow-hidden focus-within:ring-2 focus-within:ring-indigo-500 focus-within:border-indigo-500 bg-white shadow-sm">
              <input
                type="text"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                placeholder="Ask me to manage your tasks using natural language (e.g. 'Add a task to buy groceries', 'Show my tasks', 'Mark groceries as done', 'Complete task 1', 'Delete my shopping list')..."
                className="w-full px-5 py-4 pr-16 focus:outline-none text-slate-700 placeholder-slate-500 rounded-xl"
                disabled={isLoading}
              />
              <button
                type="submit"
                className={`absolute right-3 top-1/2 transform -translate-y-1/2 px-4 py-2 rounded-lg font-medium text-white ${
                  isLoading
                    ? 'bg-slate-400 cursor-not-allowed'
                    : 'bg-gradient-to-r from-indigo-600 to-blue-700 hover:from-indigo-700 hover:to-blue-800'
                } transition-all duration-300 shadow-md flex items-center`}
                disabled={isLoading || !inputValue.trim()}
              >
                {isLoading ? (
                  <svg className="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                ) : (
                  <span className="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 5l7 7-7 7M5 5l7 7-7 7" />
                    </svg>
                    Send
                  </span>
                )}
              </button>
            </div>
            <div className="mt-3 flex justify-between items-center">
              <div className="text-xs text-slate-500 flex items-center">
                <div className="flex items-center bg-emerald-100 px-2 py-1 rounded-full mr-2">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5 mr-1 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                  </svg>
                  <span>AI Secured</span>
                </div>
                <span>Powered by AI • Private</span>
              </div>
              <div className="flex items-center space-x-3">
                <div className="flex items-center bg-slate-100 rounded-lg px-2 py-1">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-slate-500 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
                  </svg>
                  <select
                    value={modelProvider}
                    onChange={(e) => setModelProvider(e.target.value)}
                    className="text-xs bg-transparent border-none focus:outline-none focus:ring-0 text-slate-700 font-medium"
                  >
                    <option value="openai">OpenAI</option>
                    <option value="gemini">Gemini</option>
                  </select>
                </div>
                <div className="flex space-x-2">
                  <button className="text-slate-500 hover:text-indigo-600 transition-colors p-1 rounded-full hover:bg-slate-100">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
                    </svg>
                  </button>
                  <button className="text-slate-500 hover:text-indigo-600 transition-colors p-1 rounded-full hover:bg-slate-100">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </button>
                </div>
              </div>
            </div>
          </form>
        </>
      )}
    </div>
  );
};

export default ChatInterface;