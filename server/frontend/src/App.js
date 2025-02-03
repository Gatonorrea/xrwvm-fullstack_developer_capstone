import React from 'react';
import { Routes, Route } from 'react-router-dom';
import LoginPanel from './components/Login/Login'; // Import the LoginPanel component
import Dealers from './components/Dealers/Dealers';

function App() {
  return (
    <Routes>
      {/* Route for the login page */}
      <Route path="/login" element={<LoginPanel />} />

      {/* Add a default route for the root URL */}
      <Route path="/" element={<LoginPanel />} />

      {/* Add more routes here as needed */}
        <Route path="/dealers" element={<Dealers/>} />
    </Routes>
  );
}

export default App;
