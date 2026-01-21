import React, { useState } from 'react';
import Link from 'next/link';

const HeroSection = () => {
  const [isVideoModalOpen, setIsVideoModalOpen] = useState(false);
  const serifFont = "'Georgia', 'Times New Roman', serif";

  return (
    <div className="text-center mb-16">
      <div className="inline-block px-4 py-1.5 bg-gradient-to-r from-indigo-100 to-blue-100 text-indigo-700 rounded-full text-sm font-medium mb-6">
        <span className="flex items-center justify-center">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-4 w-4 mr-2"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M5 13l4 4L19 7"
            />
          </svg>
          AI-Powered Productivity Suite
        </span>
      </div>

      <h1
        className="text-4xl md:text-5xl text-slate-900 mb-6 leading-tight font-light tracking-wide"
        style={{ fontFamily: serifFont }}
      >
        <span className="block">Transform Your Productivity with</span>
        <span
          className="block bg-gradient-to-r from-indigo-600 to-blue-700 bg-clip-text text-transparent mt-2 font-normal"
          style={{ fontFamily: serifFont }}
        >
          AI-Powered Task Management
        </span>
      </h1>

      <p
        className="mt-6 text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed font-light"
        style={{ fontFamily: serifFont }}
      >
        The ultimate SaaS solution for teams looking to streamline their workflow.
        Our AI assistant understands natural language commands to create, manage,
        and track your tasks effortlessly.
      </p>

      <div className="mt-10 flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4">
        <button
          className="bg-gradient-to-r from-indigo-600 to-blue-700 text-white px-8 py-4 rounded-xl hover:from-indigo-700 hover:to-blue-800 transition-all duration-300 shadow-lg hover:shadow-xl font-medium text-lg"
          style={{ fontFamily: serifFont }}
        >
          <Link href="#chat-section">
            Start Free 14-Day Trial
          </Link>
        </button>

        <button
          onClick={() => setIsVideoModalOpen(true)}
          className="border border-slate-300 text-slate-700 px-8 py-4 rounded-xl hover:border-indigo-500 hover:text-indigo-600 transition-all duration-300 font-medium text-lg flex items-center justify-center"
          style={{ fontFamily: serifFont }}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-5 w-5 mr-2"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"
            />
          </svg>
          Watch Demo
        </button>
      </div>

      <div className="mt-8 flex flex-col sm:flex-row justify-center items-center text-slate-500 text-sm">
        <div className="flex items-center mb-2 sm:mb-0">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-5 w-5 text-green-500 mr-1"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M5 13l4 4L19 7"
            />
          </svg>
          <span>No credit card required</span>
        </div>

        <span className="hidden sm:inline mx-3">•</span>

        <div className="flex items-center">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-5 w-5 text-green-500 mr-1"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M5 13l4 4L19 7"
            />
          </svg>
          <span>Cancel anytime</span>
        </div>
      </div>

      {/* Professional SAAS Demo Modal with Scroll Indicators */}
      {isVideoModalOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-80 backdrop-blur-sm flex items-center justify-center z-50 p-4">
          <div className="relative w-full max-w-4xl">
            <button
              onClick={() => setIsVideoModalOpen(false)}
              className="absolute -top-4 -right-4 bg-white rounded-full shadow-lg text-gray-800 text-2xl z-20 hover:bg-gray-100 transition-colors w-10 h-10 flex items-center justify-center"
              aria-label="Close"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
            <div className="bg-white rounded-2xl overflow-hidden shadow-2xl border border-slate-200 max-h-[90vh]">
              <div className="bg-gradient-to-r from-indigo-600 to-blue-700 px-6 py-4">
                <h3 className="text-xl font-bold text-white" style={{ fontFamily: serifFont }}>
                  TaskBot AI Demo
                </h3>
              </div>
              <div className="aspect-w-16 aspect-h-9 bg-gray-900 relative">
                <video
                  src="/TaskBot-demo (2).mp4"
                  controls
                  autoPlay
                  className="w-full h-auto"
                  onError={(e) => {
                    console.error("Video failed to load:", e);
                    // Show fallback content when video fails to load
                    const videoElement = e.target;
                    const fallbackElement = videoElement.nextElementSibling;
                    if (fallbackElement) {
                      fallbackElement.style.display = 'block';
                    }
                  }}
                  onLoadedMetadata={(e) => {
                    // Check if video has valid duration, if not show fallback
                    if (e.target.duration === 0 || isNaN(e.target.duration)) {
                      const videoElement = e.target;
                      const fallbackElement = videoElement.nextElementSibling;
                      if (fallbackElement) {
                        fallbackElement.style.display = 'block';
                      }
                    }
                    // Set playback rate to 1.5x
                    e.target.playbackRate = 1.5;
                  }}
                  onPlay={(e) => {
                    // Ensure playback rate is 1.5x when video starts playing
                    e.target.playbackRate = 1.5;
                  }}
                >
                  Your browser does not support the video tag.
                </video>
                {/* Fallback content that shows when video is empty or invalid */}
                <div id="demo-fallback" className="absolute inset-0 bg-gray-900 p-6 flex items-center justify-center opacity-100" style={{ display: 'none' }}>
                  <div className="text-center">
                    <p className="text-slate-600 mb-4" style={{ fontFamily: serifFont }}>
                      Video could not be loaded.
                    </p>
                    <p className="text-slate-600 text-sm" style={{ fontFamily: serifFont }}>
                      Please ensure the video file exists and is accessible.
                    </p>
                  </div>
                </div>
              </div>
              
              {/* Scroll Indicator */}
              <div className="flex justify-center py-2 bg-white">
                <div className="flex space-x-2">
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.3s' }}></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default HeroSection;