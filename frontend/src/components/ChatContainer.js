import ChatInterface from './ChatInterface';

const ChatContainer = () => {
  return (
    <div id="chat-section" className="bg-white rounded-2xl shadow-xl overflow-hidden border border-slate-200">
      <div className="bg-gradient-to-r from-slate-800 to-slate-900 px-6 py-5">
        <div className="flex items-center">
          <div className="bg-gradient-to-r from-indigo-500 to-blue-600 p-3 rounded-xl">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
            </svg>
          </div>
          <div className="ml-4">
            <h2 className="text-white text-xl font-normal" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>TaskBot AI Assistant</h2>
            <div className="flex items-center mt-1">
              <div className="w-2 h-2 bg-green-400 rounded-full mr-2"></div>
              <p className="text-slate-300 text-sm" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Online • Ready to assist</p>
            </div>
          </div>
          <div className="ml-auto flex space-x-2">
            <button className="text-slate-400 hover:text-white transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
            <button className="text-slate-400 hover:text-white transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </button>
          </div>
        </div>
      </div>
      <div className="p-1">
        <div className="bg-gradient-to-br from-slate-50 to-slate-100 rounded-xl p-4 h-[50vh] min-h-[400px]">
          <ChatInterface userId="default-user" />
        </div>
      </div>
    </div>
  );
};

export default ChatContainer;