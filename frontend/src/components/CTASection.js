const CTASection = () => {
  return (
    <div
      className="py-16 mt-16 mb-10 rounded-2xl relative overflow-hidden"
      style={{
        backgroundImage: "url('https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80')",
        backgroundSize: 'cover',
        backgroundPosition: 'center',
      }}
    >
      <div className="absolute inset-0 bg-gradient-to-br from-slate-800/70 to-slate-900/80"></div>
      <div className="max-w-4xl mx-auto text-center px-4 relative z-10">
        <div className="inline-block px-4 py-1 bg-gradient-to-r from-slate-200 to-slate-300 text-slate-700 rounded-full text-xs font-medium mb-4">
          <span className="flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            Join thousands of productive teams
          </span>
        </div>
        <h2 className="text-2xl md:text-3xl font-light text-white mb-4" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Ready to Transform Your Productivity?</h2>
        <p className="text-lg text-slate-200 mb-6 max-w-2xl mx-auto" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
          Join thousands of professionals who have revolutionized their task management with AI.
        </p>
        <div className="flex flex-col sm:flex-row justify-center space-y-3 sm:space-y-0 sm:space-x-3">
          <button className="bg-gradient-to-r from-slate-700 to-slate-800 text-white px-6 py-3 rounded-lg hover:from-slate-800 hover:to-slate-900 transition-all duration-300 shadow-lg hover:shadow-xl font-medium text-base">
            Start Free 14-Day Trial
          </button>
          <button className="bg-transparent border border-slate-500 text-white px-6 py-3 rounded-lg hover:bg-slate-500/10 transition-all duration-300 font-medium text-base">
            Schedule a Demo
          </button>
        </div>
        <div className="mt-4 flex flex-col sm:flex-row justify-center items-center text-slate-300 text-xs" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
          <div className="flex items-center mb-1 sm:mb-0">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-green-400 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            <span>No credit card required</span>
          </div>
          <span className="hidden sm:inline mx-2">•</span>
          <div className="flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-green-400 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            <span>Cancel anytime</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CTASection;