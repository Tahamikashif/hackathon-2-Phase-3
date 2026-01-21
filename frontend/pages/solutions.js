import Head from 'next/head';
import Link from 'next/link';

export default function SolutionsPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100">
      <Head>
        <title>Solutions | TaskBot AI</title>
        <meta name="description" content="Explore solutions for different team sizes and industries" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      {/* Navigation Bar */}
      <nav className="bg-white shadow-sm border-b border-slate-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <div className="flex items-center">
              <div className="flex-shrink-0 flex items-center">
                <div className="bg-gradient-to-r from-blue-600 to-indigo-700 w-10 h-10 rounded-lg flex items-center justify-center shadow-md">
                  <span className="text-white font-bold text-xl">TB</span>
                </div>
                <Link href="/" className="ml-3 text-xl font-bold bg-gradient-to-r from-blue-600 to-indigo-700 bg-clip-text text-transparent">TaskBot AI</Link>
              </div>
              <div className="hidden md:ml-10 md:flex md:space-x-8">
                <Link href="/" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300 border-b-2 border-transparent hover:border-indigo-500 py-5">Home</Link>
                <Link href="/features" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300 border-b-2 border-transparent hover:border-indigo-500 py-5">Features</Link>
                <Link href="/solutions" className="text-indigo-600 font-medium transition duration-300 border-b-2 border-indigo-500 py-5">Solutions</Link>
                <Link href="/pricing" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300 border-b-2 border-transparent hover:border-indigo-500 py-5">Pricing</Link>
                <Link href="/resources" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300 border-b-2 border-transparent hover:border-indigo-500 py-5">Resources</Link>
                <Link href="/contact" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300 border-b-2 border-transparent hover:border-indigo-500 py-5">Contact</Link>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <Link href="/login" className="hidden md:block text-slate-600 hover:text-indigo-600 font-medium transition duration-300">
                Sign in
              </Link>
              <Link href="/signup" className="bg-gradient-to-r from-blue-600 to-indigo-700 text-white px-5 py-2 rounded-lg hover:from-blue-700 hover:to-indigo-800 transition-all duration-300 shadow-md hover:shadow-lg font-medium">
                Get Started
              </Link>
              <button className="md:hidden text-slate-600">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </nav>

      <main className="container mx-auto px-4 py-8">
        <div className="max-w-6xl mx-auto">
          {/* Hero Section */}
          <div className="text-center mb-16">
            <h1 className="text-4xl md:text-5xl font-bold text-slate-900 mb-6 leading-tight">
              Tailored <span className="bg-gradient-to-r from-blue-600 to-indigo-700 bg-clip-text text-transparent">Solutions</span> for Every Team
            </h1>
            <p className="text-lg text-slate-600 max-w-3xl mx-auto leading-relaxed">
              Discover how TaskBot AI adapts to your unique workflow and business needs.
            </p>
          </div>

          {/* Solutions Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 hover:shadow-lg transition-all duration-300 group">
              <div className="w-14 h-14 rounded-xl bg-gradient-to-r from-blue-500 to-indigo-600 flex items-center justify-center mb-5 group-hover:scale-105 transition-transform duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Small Business</h3>
              <p className="text-slate-600 mb-4">Streamline operations and boost productivity for growing teams with our affordable solution.</p>
              <Link href="#" className="text-indigo-600 font-medium flex items-center group-hover:underline">
                Learn more
                <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              </Link>
            </div>
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 hover:shadow-lg transition-all duration-300 group">
              <div className="w-14 h-14 rounded-xl bg-gradient-to-r from-indigo-500 to-purple-600 flex items-center justify-center mb-5 group-hover:scale-105 transition-transform duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                </svg>
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Enterprise</h3>
              <p className="text-slate-600 mb-4">Scale your organization with advanced features, security, and administrative controls.</p>
              <Link href="#" className="text-indigo-600 font-medium flex items-center group-hover:underline">
                Learn more
                <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              </Link>
            </div>
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 hover:shadow-lg transition-all duration-300 group">
              <div className="w-14 h-14 rounded-xl bg-gradient-to-r from-purple-500 to-pink-600 flex items-center justify-center mb-5 group-hover:scale-105 transition-transform duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
                </svg>
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Remote Teams</h3>
              <p className="text-slate-600 mb-4">Keep distributed teams connected and accountable with our collaboration tools.</p>
              <Link href="#" className="text-indigo-600 font-medium flex items-center group-hover:underline">
                Learn more
                <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              </Link>
            </div>
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 hover:shadow-lg transition-all duration-300 group">
              <div className="w-14 h-14 rounded-xl bg-gradient-to-r from-green-500 to-emerald-600 flex items-center justify-center mb-5 group-hover:scale-105 transition-transform duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                </svg>
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Project Management</h3>
              <p className="text-slate-600 mb-4">Manage complex projects with timelines, dependencies, and milestone tracking.</p>
              <Link href="#" className="text-indigo-600 font-medium flex items-center group-hover:underline">
                Learn more
                <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              </Link>
            </div>
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 hover:shadow-lg transition-all duration-300 group">
              <div className="w-14 h-14 rounded-xl bg-gradient-to-r from-amber-500 to-orange-600 flex items-center justify-center mb-5 group-hover:scale-105 transition-transform duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Time Tracking</h3>
              <p className="text-slate-600 mb-4">Automatically track time spent on tasks and projects for accurate reporting.</p>
              <Link href="#" className="text-indigo-600 font-medium flex items-center group-hover:underline">
                Learn more
                <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              </Link>
            </div>
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 hover:shadow-lg transition-all duration-300 group">
              <div className="w-14 h-14 rounded-xl bg-gradient-to-r from-rose-500 to-pink-600 flex items-center justify-center mb-5 group-hover:scale-105 transition-transform duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                </svg>
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Compliance</h3>
              <p className="text-slate-600 mb-4">Meet industry regulations with audit trails and compliance reporting features.</p>
              <Link href="#" className="text-indigo-600 font-medium flex items-center group-hover:underline">
                Learn more
                <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              </Link>
            </div>
          </div>

          {/* CTA Section */}
          <div
            className="py-16 rounded-2xl relative overflow-hidden"
            style={{
              backgroundImage: "url('https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80')",
              backgroundSize: 'cover',
              backgroundPosition: 'center',
            }}
          >
            <div className="absolute inset-0 bg-gradient-to-br from-slate-800/70 to-slate-900/80"></div>
            <div className="max-w-3xl mx-auto text-center px-4 relative z-10">
              <h2 className="text-2xl md:text-3xl font-bold text-white mb-4">Ready to Transform Your Productivity?</h2>
              <p className="text-lg text-slate-200 mb-8 max-w-2xl mx-auto">
                Join thousands of professionals who have revolutionized their task management with AI.
              </p>
              <div className="flex flex-col sm:flex-row justify-center space-y-3 sm:space-y-0 sm:space-x-3">
                <Link href="/signup" className="bg-white text-slate-700 px-6 py-3 rounded-lg hover:bg-slate-100 transition-all duration-300 shadow-lg hover:shadow-xl font-semibold text-base">
                  Start Free 14-Day Trial
                </Link>
                <Link href="/demo" className="bg-transparent border border-white text-white px-6 py-3 rounded-lg hover:bg-white/10 transition-all duration-300 font-semibold text-base">
                  Schedule a Demo
                </Link>
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gradient-to-b from-slate-800 to-slate-900 text-white pt-10 pb-6 mt-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6">
            <div className="lg:col-span-2">
              <div className="flex items-center">
                <div className="bg-gradient-to-r from-blue-600 to-indigo-700 w-8 h-8 rounded-lg flex items-center justify-center shadow-md">
                  <span className="text-white font-bold text-sm">TB</span>
                </div>
                <span className="ml-2 text-lg font-bold bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">TaskBot AI</span>
              </div>
              <p className="mt-2 text-slate-300 text-sm max-w-md">
                AI-powered task management for modern teams.
              </p>
              <div className="flex space-x-3 mt-4">
                <a href="#" className="text-slate-300 hover:text-white transition-colors">
                  <span className="sr-only">Twitter</span>
                  <svg className="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" />
                  </svg>
                </a>
                <a href="#" className="text-slate-300 hover:text-white transition-colors">
                  <span className="sr-only">LinkedIn</span>
                  <svg className="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" />
                  </svg>
                </a>
                <a href="#" className="text-slate-300 hover:text-white transition-colors">
                  <span className="sr-only">GitHub</span>
                  <svg className="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                    <path fillRule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clipRule="evenodd" />
                  </svg>
                </a>
              </div>
            </div>
            
            <div>
              <h3 className="text-xs font-semibold mb-3 text-slate-200">Product</h3>
              <ul className="space-y-2">
                <li><Link href="/features" className="text-slate-300 hover:text-white transition-colors text-sm">Features</Link></li>
                <li><Link href="/solutions" className="text-slate-300 hover:text-white transition-colors text-sm">Solutions</Link></li>
                <li><Link href="/pricing" className="text-slate-300 hover:text-white transition-colors text-sm">Pricing</Link></li>
                <li><Link href="/demo" className="text-slate-300 hover:text-white transition-colors text-sm">Demo</Link></li>
              </ul>
            </div>
            <div>
              <h3 className="text-xs font-semibold mb-3 text-slate-200">Resources</h3>
              <ul className="space-y-2">
                <li><Link href="/blog" className="text-slate-300 hover:text-white transition-colors text-sm">Blog</Link></li>
                <li><Link href="/help" className="text-slate-300 hover:text-white transition-colors text-sm">Help Center</Link></li>
                <li><Link href="/community" className="text-slate-300 hover:text-white transition-colors text-sm">Community</Link></li>
                <li><Link href="/tutorials" className="text-slate-300 hover:text-white transition-colors text-sm">Tutorials</Link></li>
              </ul>
            </div>
            <div>
              <h3 className="text-xs font-semibold mb-3 text-slate-200">Company</h3>
              <ul className="space-y-2">
                <li><Link href="/about" className="text-slate-300 hover:text-white transition-colors text-sm">About Us</Link></li>
                <li><Link href="/careers" className="text-slate-300 hover:text-white transition-colors text-sm">Careers</Link></li>
                <li><Link href="/contact" className="text-slate-300 hover:text-white transition-colors text-sm">Contact</Link></li>
                <li><Link href="/legal" className="text-slate-300 hover:text-white transition-colors text-sm">Legal</Link></li>
              </ul>
            </div>
          </div>
          
          <div className="border-t border-slate-700 mt-6 pt-4 flex flex-col md:flex-row justify-between items-center">
            <p className="text-slate-400 text-xs">
              &copy; 2026 TaskBot AI. All rights reserved.
            </p>
            <div className="flex space-x-4 mt-2 md:mt-0">
              <Link href="/privacy" className="text-slate-400 hover:text-slate-200 text-xs transition-colors">Privacy Policy</Link>
              <Link href="/terms" className="text-slate-400 hover:text-slate-200 text-xs transition-colors">Terms of Service</Link>
              <Link href="/cookies" className="text-slate-400 hover:text-slate-200 text-xs transition-colors">Cookie Policy</Link>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}