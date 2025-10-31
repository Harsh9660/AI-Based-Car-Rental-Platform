import React, { useEffect, useState } from 'react';
import axios from 'axios';

const CarList = () => {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    axios.get('/api/cars')
      .then(res => setCars(res.data))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h2 className="text-xl font-semibold mb-2">Available Cars</h2>
      <ul>
        {cars.map(car => (
          <li key={car.car_id} className="border p-2 mb-2 rounded">
            {car.make} {car.model} ({car.type})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CarList;
