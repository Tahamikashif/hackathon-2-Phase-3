
const MessageList = ({ messages }) => {
  return (
    <div className="space-y-4">
      {messages.map((message) => (
        <div
          key={message.id}
          className={`max-w-[90%] p-4 rounded-2xl transition-all duration-300 ${
            message.role === 'user'
              ? 'bg-gradient-to-r from-blue-600 to-indigo-700 text-white ml-auto rounded-br-none'
              : message.role === 'assistant'
              ? 'bg-white text-slate-800 mr-auto rounded-bl-none border border-slate-200 shadow-sm'
              : 'bg-gradient-to-r from-amber-100 to-amber-50 text-slate-800 mr-auto rounded-bl-none border border-amber-200'
          }`}
        >
          <div className="flex items-start">
            <div className="flex-1">
              <div className="flex items-center mb-2">
                <div className={`font-bold ${
                  message.role === 'user'
                    ? 'text-blue-100'
                    : message.role === 'assistant'
                      ? 'text-indigo-700'
                      : 'text-amber-700'
                }`}>
                  {message.role === 'user' ? 'You' : message.role === 'assistant' ? 'TaskBot AI' : 'System'}
                </div>
                {message.role === 'assistant' && (
                  <div className="ml-2 bg-gradient-to-r from-emerald-100 to-emerald-200 text-emerald-800 text-xs px-2 py-1 rounded-full flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                    </svg>
                    AI Assistant
                  </div>
                )}
              </div>
              <div className="whitespace-pre-wrap text-slate-700 dark:text-slate-200 text-sm">{message.content}</div>

              {/* Display tool calls if present */}
              {message.toolCalls && message.toolCalls.length > 0 && (
                <div className={`mt-3 pt-3 border-t ${
                  message.role === 'user'
                    ? 'border-blue-500/30'
                    : 'border-slate-200'
                }`}>
                  <div className="flex items-center text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
                    </svg>
                    AI Actions Performed
                  </div>
                  <div className="space-y-2">
                    {message.toolCalls.map((call, index) => (
                      <div
                        key={index}
                        className={`p-2.5 rounded-lg backdrop-blur-sm ${
                          message.role === 'user'
                            ? 'bg-blue-500/20 border border-blue-400/30'
                            : 'bg-slate-100 border border-slate-300/50'
                        }`}
                      >
                        <div className="flex items-center">
                          <div className="bg-gradient-to-r from-blue-500 to-indigo-600 p-1.5 rounded-lg mr-2.5">
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
                            </svg>
                          </div>
                          <div className="font-mono font-bold text-xs text-indigo-600 dark:text-indigo-300">{call.name}</div>
                        </div>
                        <div className="mt-1.5 text-xs text-slate-600 dark:text-slate-300 bg-black/5 p-1.5 rounded-md">
                          {JSON.stringify(call.arguments)}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
            {message.role !== 'user' && (
              <div className="ml-3 flex-shrink-0">
                <div className="bg-gradient-to-r from-blue-100 to-indigo-100 w-8 h-8 rounded-full flex items-center justify-center shadow-md">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-indigo-600" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clipRule="evenodd" />
                  </svg>
                </div>
              </div>
            )}
          </div>
        </div>
      ))}
    </div>
  );
};

export default MessageList;