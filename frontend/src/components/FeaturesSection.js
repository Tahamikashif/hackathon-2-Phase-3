const FeaturesSection = () => {
  return (
    <div className="mt-20">
      <div className="text-center max-w-2xl mx-auto mb-16">
        <h2 className="text-3xl font-light text-slate-900 mb-4" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Powerful Features for Modern Teams</h2>
        <p className="text-lg text-slate-600" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Everything you need to boost productivity and streamline your workflow in one integrated platform.</p>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div className="bg-gradient-to-b from-white to-slate-50 p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-lg transition-all duration-300 group">
          <div className="w-14 h-14 rounded-xl bg-gradient-to-r from-indigo-500 to-blue-600 flex items-center justify-center mb-5 group-hover:scale-105 transition-transform duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
          </div>
          <h3 className="text-xl font-normal text-slate-900 mb-3" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Natural Language Processing</h3>
          <p className="text-slate-600 mb-4" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Simply tell us what you need to do in plain English. No complex commands required.</p>
          <a href="#" className="text-indigo-600 font-medium flex items-center group-hover:underline" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
            Learn more
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </a>
        </div>
        <div className="bg-gradient-to-b from-white to-slate-50 p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-lg transition-all duration-300 group">
          <div className="w-14 h-14 rounded-xl bg-gradient-to-r from-blue-500 to-cyan-600 flex items-center justify-center mb-5 group-hover:scale-105 transition-transform duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <h3 className="text-xl font-normal text-slate-900 mb-3" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Smart Automation</h3>
          <p className="text-slate-600 mb-4" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>AI automatically organizes, prioritizes, and schedules your tasks based on context.</p>
          <a href="#" className="text-indigo-600 font-medium flex items-center group-hover:underline" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
            Learn more
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </a>
        </div>
        <div className="bg-gradient-to-b from-white to-slate-50 p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-lg transition-all duration-300 group">
          <div className="w-14 h-14 rounded-xl bg-gradient-to-r from-purple-500 to-indigo-600 flex items-center justify-center mb-5 group-hover:scale-105 transition-transform duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
            </svg>
          </div>
          <h3 className="text-xl font-normal text-slate-900 mb-3" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Enterprise Security</h3>
          <p className="text-slate-600 mb-4" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Military-grade encryption and privacy controls to keep your data secure.</p>
          <a href="#" className="text-indigo-600 font-medium flex items-center group-hover:underline" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
            Learn more
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </a>
        </div>
        <div className="bg-gradient-to-b from-white to-slate-50 p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-lg transition-all duration-300 group">
          <div className="w-14 h-14 rounded-xl bg-gradient-to-r from-green-500 to-emerald-600 flex items-center justify-center mb-5 group-hover:scale-105 transition-transform duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4" />
            </svg>
          </div>
          <h3 className="text-xl font-normal text-slate-900 mb-3" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Seamless Integrations</h3>
          <p className="text-slate-600 mb-4" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Connect with your favorite tools like Slack, Google Calendar, and more.</p>
          <a href="#" className="text-indigo-600 font-medium flex items-center group-hover:underline" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
            Learn more
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </a>
        </div>
        <div className="bg-gradient-to-b from-white to-slate-50 p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-lg transition-all duration-300 group">
          <div className="w-14 h-14 rounded-xl bg-gradient-to-r from-amber-500 to-orange-600 flex items-center justify-center mb-5 group-hover:scale-105 transition-transform duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
          <h3 className="text-xl font-normal text-slate-900 mb-3" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Advanced Analytics</h3>
          <p className="text-slate-600 mb-4" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Gain insights into your productivity patterns and optimize your workflow.</p>
          <a href="#" className="text-indigo-600 font-medium flex items-center group-hover:underline" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
            Learn more
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </a>
        </div>
        <div className="bg-gradient-to-b from-white to-slate-50 p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-lg transition-all duration-300 group">
          <div className="w-14 h-14 rounded-xl bg-gradient-to-r from-rose-500 to-pink-600 flex items-center justify-center mb-5 group-hover:scale-105 transition-transform duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
            </svg>
          </div>
          <h3 className="text-xl font-normal text-slate-900 mb-3" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Custom Workflows</h3>
          <p className="text-slate-600 mb-4" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Create custom automation rules tailored to your specific needs.</p>
          <a href="#" className="text-indigo-600 font-medium flex items-center group-hover:underline" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
            Learn more
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </a>
        </div>
      </div>
    </div>
  );
};

export default FeaturesSection;