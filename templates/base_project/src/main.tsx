import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { Navigate } from 'react-router-dom';
import { HelmetProvider } from 'react-helmet-async';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

import { initTheme } from './libraries/theme.ts';
import { initFullscreen } from './libraries/fullscreen.ts';
import { initLanguage } from './libraries/language.ts';
import { initAnalytics, AnalyticsTracker } from './libraries/analytics.ts';

import './font.scss'
import './theme.scss'
import './index.scss'

initTheme();
initFullscreen();
initLanguage();
initAnalytics();

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <HelmetProvider>
      <Router>
        <AnalyticsTracker />
        <Routes>
          
          <Route path="/" element={<Navigate to="/{{language_short}}/" replace />} />
          <Route path="*"" element={<Navigate to="/" replace />} />

        </Routes>
      </Router>
    </HelmetProvider>
  </StrictMode>
);