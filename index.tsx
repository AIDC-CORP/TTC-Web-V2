import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './i18n';

const rootElement = document.getElementById('root');
if (!rootElement) {
  throw new Error("Could not find root element to mount to");
}

const root = ReactDOM.createRoot(rootElement);

// Render app - i18n will load asynchronously and components handle ready state
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
