import React, { useState } from 'react';
import axios from 'axios';

const BookingForm = () => {
  const [userId, setUserId] = useState('');
  const [carId, setCarId] = useState('');
  const [startDate, setStartDate] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('/api/bookings', {
        user_id: userId,
        car_id: carId,
        start_date: startDate
      });
      setMessage('Booking successful! Price: $' + res.data.price);
    } catch (error) {
      setMessage('Booking failed: ' + error.message);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="my-4">
      <input type="text" placeholder="User ID" value={userId} onChange={e => setUserId(e.target.value)} required className="border p-2 mr-2" />
      <input type="text" placeholder="Car ID" value={carId} onChange={e => setCarId(e.target.value)} required className="border p-2 mr-2" />
      <input type="date" value={startDate} onChange={e => setStartDate(e.target.value)} required className="border p-2 mr-2" />
      <button type="submit" className="bg-blue-600 text-white p-2 rounded">Book</button>
      {message && <p className="mt-2">{message}</p>}
    </form>
  );
};

export default BookingForm;
