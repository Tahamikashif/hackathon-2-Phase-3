
const MessageList = ({ messages }) => {
  return (
    <div className="space-y-4">
      {messages.map((message) => (
        <div
          key={message.id}
          className={`p-4 rounded-2xl max-w-[85%] ${
            message.role === 'user'
              ? 'bg-gradient-to-r from-indigo-500 to-blue-600 text-white ml-auto shadow-md'
              : message.role === 'assistant'
              ? 'bg-gradient-to-r from-slate-50 to-slate-100 text-slate-800 mr-auto border border-slate-200 shadow-sm'
              : 'bg-gradient-to-r from-amber-50 to-amber-100 text-amber-800 mr-auto border border-amber-200 shadow-sm'
          }`}
        >
          <div className={`font-semibold mb-2 flex items-center ${
            message.role === 'user' ? 'text-indigo-100' : 'text-slate-500'
          }`}>
            {message.role === 'user' ? (
              <>
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
                You
              </>
            ) : message.role === 'assistant' ? (
              <>
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                </svg>
                TaskBot AI
              </>
            ) : (
              <>
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                </svg>
                System
              </>
            )}
          </div>
          <div className={`whitespace-pre-wrap ${
            message.role === 'user' ? 'text-white' : 'text-slate-700'
          }`}>{message.content}</div>

          {/* Display tool calls if present */}
          {message.toolCalls && message.toolCalls.length > 0 && (
            <div className={`mt-3 pt-3 border-t ${
              message.role === 'user' ? 'border-indigo-400' : 'border-slate-300'
            }`}>
              <div className={`text-xs font-semibold ${
                message.role === 'user' ? 'text-indigo-200' : 'text-slate-500'
              }`}>Tool Operations:</div>
              <ul className="text-xs bg-white/20 p-3 rounded-lg mt-2 backdrop-blur-sm">
                {message.toolCalls.map((call, index) => (
                  <li key={index} className="mb-2 last:mb-0">
                    <div className="flex items-center">
                      <span className={`font-mono ${
                        message.role === 'user' ? 'bg-white/30 text-white' : 'bg-slate-200 text-slate-700'
                      } px-2 py-1 rounded mr-2`}>{call.name}</span>
                      <span className={`${message.role === 'user' ? 'text-indigo-100' : 'text-slate-600'}`}>
                        {JSON.stringify(call.arguments)}
                      </span>
                    </div>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      ))}
    </div>
  );
};

export default MessageList;