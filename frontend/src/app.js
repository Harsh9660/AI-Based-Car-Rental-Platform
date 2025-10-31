import React from 'react';
import CarList from './components/CarList';
import BookingForm from './components/BookingForm';
import Chatbot from './components/Chatbot';

function App() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">AI-Based Car Rental</h1>
      <CarList />
      <BookingForm />
      <Chatbot />
    </div>
  );
}

export default App;
