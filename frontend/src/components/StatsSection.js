const StatsSection = () => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
      <div className="bg-gradient-to-b from-white to-slate-50 p-8 rounded-2xl shadow-sm border border-slate-200 text-center">
        <div className="text-4xl font-light bg-gradient-to-r from-indigo-600 to-blue-700 bg-clip-text text-transparent mb-2" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>98%</div>
        <div className="text-slate-600 font-medium" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Task Completion Rate</div>
      </div>
      <div className="bg-gradient-to-b from-white to-slate-50 p-8 rounded-2xl shadow-sm border border-slate-200 text-center">
        <div className="text-4xl font-light bg-gradient-to-r from-indigo-600 to-blue-700 bg-clip-text text-transparent mb-2" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>24/7</div>
        <div className="text-slate-600 font-medium" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>AI Assistant Availability</div>
      </div>
      <div className="bg-gradient-to-b from-white to-slate-50 p-8 rounded-2xl shadow-sm border border-slate-200 text-center">
        <div className="text-4xl font-light bg-gradient-to-r from-indigo-600 to-blue-700 bg-clip-text text-transparent mb-2" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>10K+</div>
        <div className="text-slate-600 font-medium" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>Active Users</div>
      </div>
    </div>
  );
};

export default StatsSection;