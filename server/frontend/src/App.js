import React from 'react';
import { Routes, Route } from 'react-router-dom';
import LoginPanel from './components/Login/Login'; // Import the LoginPanel component
import Dealers from './components/Dealers/Dealers';
import Dealer from "./components/Dealers/Dealer";
import PostReview from "./components/Dealers/PostReview";

function App() {
  return (
    <Routes>
      {/* Route for the login page */}
      <Route path="/login" element={<LoginPanel />} />

      {/* Add a default route for the root URL */}
      <Route path="/" element={<LoginPanel />} />

      {/* Add more routes here as needed */}
        <Route path="/dealers" element={<Dealers/>} />
         {/* Add more routes here as needed */}
        <Route path="/dealer/:id" element={<Dealer/>} />
{/* Add more routes here as needed */}
        <Route path="/postreview/:id" element={<PostReview/>} />
    </Routes>
  );
}

export default App;
