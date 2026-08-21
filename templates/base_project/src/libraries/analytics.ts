import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import ReactGA from 'react-ga4';
import configuration from '../configuration.json';

export function initAnalytics(): void {
  ReactGA.initialize(configuration.analytics.googleid);
}

export function AnalyticsTracker(): null {
  const location = useLocation();
  useEffect(() => {
    ReactGA.send({ 
      hitType: 'pageview', 
      page: location.pathname + location.search 
    });
  }, [location]);
  return null;
}