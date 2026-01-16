import Head from 'next/head';
import ChatInterface from '../src/components/ChatInterface';

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100">
      <Head>
        <title>TaskBot AI - Advanced SaaS Todo Management</title>
        <meta name="description" content="Advanced AI-powered SaaS Todo Management Platform with Natural Language Processing" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      {/* Navigation Bar */}
      <nav className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <div className="flex items-center">
              <div className="flex-shrink-0 flex items-center">
                <div className="bg-gradient-to-r from-indigo-600 to-blue-700 w-10 h-10 rounded-lg flex items-center justify-center">
                  <span className="text-white font-bold text-xl">TB</span>
                </div>
                <span className="ml-3 text-xl font-bold bg-gradient-to-r from-indigo-600 to-blue-700 bg-clip-text text-transparent">TaskBot AI</span>
              </div>
            </div>
            <div className="hidden md:flex items-center space-x-8">
              <a href="#" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300">Features</a>
              <a href="#" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300">Solutions</a>
              <a href="#" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300">Pricing</a>
              <a href="#" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300">Resources</a>
              <button className="bg-gradient-to-r from-indigo-600 to-blue-700 text-white px-5 py-2 rounded-lg hover:from-indigo-700 hover:to-blue-800 transition-all duration-300 shadow-md hover:shadow-lg">
                Sign In
              </button>
            </div>
          </div>
        </div>
      </nav>

      <main className="container mx-auto px-4 py-8">
        <div className="max-w-6xl mx-auto">
          {/* Hero Section */}
          <div className="text-center mb-12">
            <div className="inline-block px-4 py-1 bg-indigo-100 text-indigo-700 rounded-full text-sm font-semibold mb-4">
              AI-Powered Productivity
            </div>
            <h1 className="text-4xl md:text-5xl font-bold text-slate-900 mb-6 leading-tight">
              <span className="block">Transform Your Tasks with</span>
              <span className="block bg-gradient-to-r from-indigo-600 to-blue-700 bg-clip-text text-transparent">AI Intelligence</span>
            </h1>
            <p className="mt-4 text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">
              Introducing the Todo AI Chatbot - an advanced AI-powered task management platform that understands natural language commands. Simply tell our AI assistant what you need to do, and it will automatically create, manage, and track your tasks.
            </p>
            <div className="mt-8 flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4">
              <button className="bg-gradient-to-r from-indigo-600 to-blue-700 text-white px-6 py-3 rounded-lg hover:from-indigo-700 hover:to-blue-800 transition-all duration-300 shadow-md hover:shadow-lg font-medium">
                Start Free Trial
              </button>
              <button className="border border-slate-300 text-slate-700 px-6 py-3 rounded-lg hover:border-indigo-500 hover:text-indigo-600 transition-all duration-300 font-medium">
                Watch Demo
              </button>
            </div>
          </div>

          {/* Stats Section */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
            <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 text-center">
              <div className="text-3xl font-bold text-indigo-600 mb-1">98%</div>
              <div className="text-slate-600 font-medium">Task Completion Rate</div>
            </div>
            <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 text-center">
              <div className="text-3xl font-bold text-indigo-600 mb-1">24/7</div>
              <div className="text-slate-600 font-medium">AI Assistant Availability</div>
            </div>
            <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 text-center">
              <div className="text-3xl font-bold text-indigo-600 mb-1">10K+</div>
              <div className="text-slate-600 font-medium">Active Users</div>
            </div>
          </div>

          {/* Chat Container */}
          <div className="bg-white rounded-2xl shadow-lg overflow-hidden border border-slate-200">
            <div className="bg-gradient-to-r from-indigo-600 to-blue-700 px-6 py-4">
              <div className="flex items-center">
                <div className="bg-white/20 p-2 rounded-lg">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                  </svg>
                </div>
                <div className="ml-3">
                  <h2 className="text-white text-lg font-semibold">Task Assistant</h2>
                  <p className="text-indigo-200 text-xs">Powered by AI • Always available</p>
                </div>
              </div>
            </div>
            <div className="p-1">
              <div className="bg-slate-50 rounded-xl p-4 h-[50vh] min-h-[400px]">
                <div className="h-full flex items-center justify-center text-slate-500">
                  Chat Interface Loading...
                </div>
              </div>
            </div>
          </div>

          {/* Features Section */}
          <div className="mt-16">
            <h2 className="text-2xl font-bold text-center text-slate-900 mb-12">Powerful Features for Modern Teams</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 hover:shadow-md transition-shadow duration-300">
                <div className="w-12 h-12 rounded-lg bg-indigo-100 flex items-center justify-center mb-4">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                  </svg>
                </div>
                <h3 className="text-lg font-semibold text-slate-900 mb-2">Natural Language Processing</h3>
                <p className="text-slate-600 text-sm">Simply tell us what you need to do in plain English. No complex commands required.</p>
              </div>
              <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 hover:shadow-md transition-shadow duration-300">
                <div className="w-12 h-12 rounded-lg bg-blue-100 flex items-center justify-center mb-4">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                  </svg>
                </div>
                <h3 className="text-lg font-semibold text-slate-900 mb-2">Smart Automation</h3>
                <p className="text-slate-600 text-sm">AI automatically organizes, prioritizes, and schedules your tasks based on context.</p>
              </div>
              <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 hover:shadow-md transition-shadow duration-300">
                <div className="w-12 h-12 rounded-lg bg-purple-100 flex items-center justify-center mb-4">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-purple-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                </div>
                <h3 className="text-lg font-semibold text-slate-900 mb-2">Enterprise Security</h3>
                <p className="text-slate-600 text-sm">Military-grade encryption and privacy controls to keep your data secure.</p>
              </div>
              <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 hover:shadow-md transition-shadow duration-300">
                <div className="w-12 h-12 rounded-lg bg-green-100 flex items-center justify-center mb-4">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4" />
                  </svg>
                </div>
                <h3 className="text-lg font-semibold text-slate-900 mb-2">Seamless Integrations</h3>
                <p className="text-slate-600 text-sm">Connect with your favorite tools like Slack, Google Calendar, and more.</p>
              </div>
              <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 hover:shadow-md transition-shadow duration-300">
                <div className="w-12 h-12 rounded-lg bg-amber-100 flex items-center justify-center mb-4">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                  </svg>
                </div>
                <h3 className="text-lg font-semibold text-slate-900 mb-2">Advanced Analytics</h3>
                <p className="text-slate-600 text-sm">Gain insights into your productivity patterns and optimize your workflow.</p>
              </div>
              <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 hover:shadow-md transition-shadow duration-300">
                <div className="w-12 h-12 rounded-lg bg-rose-100 flex items-center justify-center mb-4">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-rose-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                  </svg>
                </div>
                <h3 className="text-lg font-semibold text-slate-900 mb-2">Custom Workflows</h3>
                <p className="text-slate-600 text-sm">Create custom automation rules tailored to your specific needs.</p>
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* CTA Section */}
      <div className="bg-gradient-to-r from-indigo-600 to-blue-700 py-16 mt-16">
        <div className="max-w-3xl mx-auto text-center px-4">
          <h2 className="text-2xl font-bold text-white mb-4">Ready to Transform Your Productivity?</h2>
          <p className="text-lg text-indigo-100 mb-8 max-w-xl mx-auto">
            Join thousands of professionals who have revolutionized their task management with AI.
          </p>
          <div className="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4">
            <button className="bg-white text-indigo-600 px-6 py-3 rounded-lg hover:bg-slate-100 transition-all duration-300 shadow-md hover:shadow-lg font-medium">
              Start Free Trial
            </button>
            <button className="bg-transparent border border-white text-white px-6 py-3 rounded-lg hover:bg-white/10 transition-all duration-300 font-medium">
              Schedule a Demo
            </button>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="bg-slate-800 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            <div>
              <div className="flex items-center">
                <div className="bg-gradient-to-r from-indigo-600 to-blue-700 w-8 h-8 rounded-lg flex items-center justify-center">
                  <span className="text-white font-bold">TB</span>
                </div>
                <span className="ml-2 text-lg font-bold">TaskBot AI</span>
              </div>
              <p className="mt-3 text-slate-400 text-sm">
                Advanced AI-powered task management for modern teams.
              </p>
            </div>
            <div>
              <h3 className="text-base font-semibold mb-3">Product</h3>
              <ul className="space-y-1 text-slate-400 text-sm">
                <li><a href="#" className="hover:text-white transition">Features</a></li>
                <li><a href="#" className="hover:text-white transition">Solutions</a></li>
                <li><a href="#" className="hover:text-white transition">Pricing</a></li>
                <li><a href="#" className="hover:text-white transition">Demo</a></li>
              </ul>
            </div>
            <div>
              <h3 className="text-base font-semibold mb-3">Resources</h3>
              <ul className="space-y-1 text-slate-400 text-sm">
                <li><a href="#" className="hover:text-white transition">Blog</a></li>
                <li><a href="#" className="hover:text-white transition">Help Center</a></li>
                <li><a href="#" className="hover:text-white transition">Community</a></li>
                <li><a href="#" className="hover:text-white transition">Events</a></li>
              </ul>
            </div>
            <div>
              <h3 className="text-base font-semibold mb-3">Company</h3>
              <ul className="space-y-1 text-slate-400 text-sm">
                <li><a href="#" className="hover:text-white transition">About Us</a></li>
                <li><a href="#" className="hover:text-white transition">Careers</a></li>
                <li><a href="#" className="hover:text-white transition">Contact</a></li>
                <li><a href="#" className="hover:text-white transition">Partners</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-slate-700 mt-8 pt-6 text-center text-slate-400 text-sm">
            <p>&copy; 2026 TaskBot AI. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}