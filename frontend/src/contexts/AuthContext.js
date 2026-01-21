// contexts/AuthContext.js
import { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userEmail, setUserEmail] = useState('');
  const [userId, setUserId] = useState('');

  useEffect(() => {
    // Check if user is logged in by checking for stored user info
    const storedUserId = localStorage.getItem('chatbot_user_id');
    const storedUserEmail = localStorage.getItem('chatbot_user_email');
    
    if (storedUserId) {
      setIsLoggedIn(true);
      setUserId(storedUserId);
      setUserEmail(storedUserEmail || '');
    }
  }, []);

  const login = (userId, email) => {
    localStorage.setItem('chatbot_user_id', userId);
    localStorage.setItem('chatbot_user_email', email);
    setIsLoggedIn(true);
    setUserId(userId);
    setUserEmail(email);
  };

  const logout = () => {
    localStorage.removeItem('chatbot_user_id');
    localStorage.removeItem('chatbot_user_email');
    setIsLoggedIn(false);
    setUserId('');
    setUserEmail('');
  };

  return (
    <AuthContext.Provider value={{ isLoggedIn, userEmail, userId, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};