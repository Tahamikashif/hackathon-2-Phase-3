import Link from 'next/link';
import { useAuth } from '../contexts/AuthContext';

const Navbar = () => {
  const { isLoggedIn, userEmail, logout } = useAuth();

  return (
    <nav className="bg-white shadow-sm border-b border-slate-100">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16 items-center">
          <div className="flex items-center">
            <div className="flex-shrink-0 flex items-center">
              <div className="bg-gradient-to-r from-indigo-600 to-blue-700 w-10 h-10 rounded-lg flex items-center justify-center shadow-md">
                <span className="text-white font-bold text-xl">TB</span>
              </div>
              <span className="ml-3 text-xl font-normal bg-gradient-to-r from-indigo-600 to-blue-700 bg-clip-text text-transparent" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>TaskBot AI</span>
            </div>
            <div className="hidden md:ml-10 md:flex md:space-x-8">
              <Link href="/" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300 border-b-2 border-transparent hover:border-indigo-500 py-5" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                Home
              </Link>
              <div className="relative group">
                <Link href="/features" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300 border-b-2 border-transparent hover:border-indigo-500 py-5 flex items-center" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                  Features
                  <svg className="ml-1 h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                  </svg>
                </Link>
                <div className="absolute z-10 hidden group-hover:block w-56 bg-white shadow-lg rounded-lg py-2 mt-2 border border-slate-200">
                  <Link href="/features#task-management" className="block px-4 py-2 text-sm text-slate-700 hover:bg-indigo-50 hover:text-indigo-600" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                    Task Management
                  </Link>
                  <Link href="/features#ai-assistant" className="block px-4 py-2 text-sm text-slate-700 hover:bg-indigo-50 hover:text-indigo-600" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                    AI Assistant
                  </Link>
                  <Link href="/features#team-collaboration" className="block px-4 py-2 text-sm text-slate-700 hover:bg-indigo-50 hover:text-indigo-600" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                    Team Collaboration
                  </Link>
                  <Link href="/features#analytics" className="block px-4 py-2 text-sm text-slate-700 hover:bg-indigo-50 hover:text-indigo-600" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                    Analytics
                  </Link>
                </div>
              </div>
              <div className="relative group">
                <Link href="/solutions" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300 border-b-2 border-transparent hover:border-indigo-500 py-5 flex items-center" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                  Solutions
                  <svg className="ml-1 h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                  </svg>
                </Link>
                <div className="absolute z-10 hidden group-hover:block w-56 bg-white shadow-lg rounded-lg py-2 mt-2 border border-slate-200">
                  <Link href="/solutions#small-business" className="block px-4 py-2 text-sm text-slate-700 hover:bg-indigo-50 hover:text-indigo-600" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                    Small Business
                  </Link>
                  <Link href="/solutions#enterprise" className="block px-4 py-2 text-sm text-slate-700 hover:bg-indigo-50 hover:text-indigo-600" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                    Enterprise
                  </Link>
                  <Link href="/solutions#remote-teams" className="block px-4 py-2 text-sm text-slate-700 hover:bg-indigo-50 hover:text-indigo-600" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                    Remote Teams
                  </Link>
                  <Link href="/solutions#project-management" className="block px-4 py-2 text-sm text-slate-700 hover:bg-indigo-50 hover:text-indigo-600" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                    Project Management
                  </Link>
                </div>
              </div>
              <Link href="/pricing" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300 border-b-2 border-transparent hover:border-indigo-500 py-5" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                Pricing
              </Link>
              <div className="relative group">
                <Link href="/resources" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300 border-b-2 border-transparent hover:border-indigo-500 py-5 flex items-center" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                  Resources
                  <svg className="ml-1 h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                  </svg>
                </Link>
                <div className="absolute z-10 hidden group-hover:block w-56 bg-white shadow-lg rounded-lg py-2 mt-2 border border-slate-200">
                  <Link href="/blog" className="block px-4 py-2 text-sm text-slate-700 hover:bg-indigo-50 hover:text-indigo-600" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                    Blog
                  </Link>
                  <Link href="/docs" className="block px-4 py-2 text-sm text-slate-700 hover:bg-indigo-50 hover:text-indigo-600" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                    Documentation
                  </Link>
                  <Link href="/tutorials" className="block px-4 py-2 text-sm text-slate-700 hover:bg-indigo-50 hover:text-indigo-600" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                    Guides
                  </Link>
                  <Link href="/support" className="block px-4 py-2 text-sm text-slate-700 hover:bg-indigo-50 hover:text-indigo-600" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                    Support
                  </Link>
                </div>
              </div>
              <Link href="/contact" className="text-slate-600 hover:text-indigo-600 font-medium transition duration-300 border-b-2 border-transparent hover:border-indigo-500 py-5" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                Contact
              </Link>
            </div>
          </div>
          <div className="flex items-center space-x-4">
            {isLoggedIn ? (
              <div className="flex items-center space-x-4">
                <span className="hidden md:block text-slate-600 text-sm font-medium truncate max-w-[120px]" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                  {userEmail || 'User'}
                </span>
                <button
                  onClick={logout}
                  className="hidden md:block text-slate-600 hover:text-indigo-600 font-medium transition duration-300"
                  style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}
                >
                  Sign out
                </button>
              </div>
            ) : (
              <Link href="/signin" className="hidden md:block text-slate-600 hover:text-indigo-600 font-medium transition duration-300" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
                Sign in
              </Link>
            )}
            <Link href="#chat-section" className="bg-gradient-to-r from-indigo-600 to-blue-700 text-white px-5 py-2 rounded-lg hover:from-indigo-700 hover:to-blue-800 transition-all duration-300 shadow-md hover:shadow-lg font-medium" style={{ fontFamily: "'Georgia', 'Times New Roman', serif" }}>
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
  );
};

export default Navbar;