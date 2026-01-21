import Head from 'next/head';
import { useEffect } from 'react';
import { AuthProvider } from '../src/contexts/AuthContext';
import Navbar from '../src/components/Navbar';
import HeroSection from '../src/components/HeroSection';
import StatsSection from '../src/components/StatsSection';
import ChatContainer from '../src/components/ChatContainer';
import FeaturesSection from '../src/components/FeaturesSection';
import CTASection from '../src/components/CTASection';
import Footer from '../src/components/Footer';

export default function Home() {
  useEffect(() => {
    const handleAnchorClick = (e) => {
      const href = e.currentTarget.getAttribute('href');
      if (href.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          window.scrollTo({
            top: target.offsetTop - 80,
            behavior: 'smooth'
          });
        }
      }
    };

    const anchors = document.querySelectorAll('a[href^="#"]');
    anchors.forEach(anchor => {
      anchor.addEventListener('click', handleAnchorClick);
    });

    return () => {
      anchors.forEach(anchor => {
        anchor.removeEventListener('click', handleAnchorClick);
      });
    };
  }, []);

  return (
    <AuthProvider>
      <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100">
        <Head>
          <title>TaskBot AI - Advanced SaaS Todo Management</title>
          <meta name="description" content="Advanced AI-powered SaaS Todo Management Platform with Natural Language Processing" />
          <link rel="icon" href="/favicon.ico" />
        </Head>

        <Navbar />

        <main className="container mx-auto px-4 py-8">
          <div className="max-w-6xl mx-auto">
            <HeroSection />
            <StatsSection />
            <ChatContainer />
            <FeaturesSection />
          </div>
        </main>

        <CTASection />
        <Footer />
      </div>
    </AuthProvider>
  );
}