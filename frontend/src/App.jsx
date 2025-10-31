import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
  const [cars, setCars] = useState([])
  const [selectedCar, setSelectedCar] = useState(null)
  const [days, setDays] = useState(1)
  const [price, setPrice] = useState(null)

  useEffect(() => {
    fetchCars()
  }, [])

  const fetchCars = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/cars')
      setCars(response.data)
    } catch (error) {
      console.error('Error fetching cars:', error)
    }
  }

  const calculatePrice = async () => {
    if (!selectedCar) return
    try {
      const response = await axios.get(`http://localhost:8000/api/cars/${selectedCar.id}/price?days=${days}`)
      setPrice(response.data.predicted_price)
    } catch (error) {
      console.error('Error calculating price:', error)
    }
  }

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-center mb-8">AI Car Rental Platform</h1>
        
        <div className="grid md:grid-cols-2 gap-8">
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-semibold mb-4">Available Cars</h2>
            <div className="space-y-3">
              {cars.map(car => (
                <div 
                  key={car.id}
                  className={`p-3 border rounded cursor-pointer ${selectedCar?.id === car.id ? 'border-blue-500 bg-blue-50' : 'border-gray-200'}`}
                  onClick={() => setSelectedCar(car)}
                >
                  <h3 className="font-medium">{car.make} {car.model}</h3>
                  <p className="text-gray-600">Year: {car.year}</p>
                </div>
              ))}
            </div>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-semibold mb-4">Price Calculator</h2>
            {selectedCar ? (
              <div className="space-y-4">
                <p>Selected: {selectedCar.make} {selectedCar.model}</p>
                <div>
                  <label className="block text-sm font-medium mb-1">Days:</label>
                  <input 
                    type="number" 
                    value={days}
                    onChange={(e) => setDays(e.target.value)}
                    className="w-full p-2 border rounded"
                    min="1"
                  />
                </div>
                <button 
                  onClick={calculatePrice}
                  className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
                >
                  Calculate Price
                </button>
                {price && (
                  <div className="text-center p-4 bg-green-50 rounded">
                    <p className="text-2xl font-bold text-green-600">${price.toFixed(2)}</p>
                  </div>
                )}
              </div>
            ) : (
              <p className="text-gray-500">Select a car to calculate price</p>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App