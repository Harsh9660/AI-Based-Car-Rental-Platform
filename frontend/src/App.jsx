import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
  const [cars, setCars] = useState([])
  const [selectedCar, setSelectedCar] = useState(null)
  const [days, setDays] = useState(1)
  const [price, setPrice] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    fetchCars()
  }, [])

  const fetchCars = async () => {
    try {
      setLoading(true)
      const response = await axios.get('http://localhost:8000/api/cars')
      setCars(response.data)
    } catch (error) {
      setError('Failed to load cars')
    } finally {
      setLoading(false)
    }
  }

  const calculatePrice = async () => {
    if (!selectedCar) return
    try {
      setLoading(true)
      const response = await axios.get(`http://localhost:8000/api/cars/${selectedCar.id}/price?days=${days}`)
      setPrice(response.data.predicted_price)
    } catch (error) {
      setError('Failed to calculate price')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        <header className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">🚗 AI Car Rental</h1>
          <p className="text-gray-600">Smart pricing with AI technology</p>
        </header>
        
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
            {error}
          </div>
        )}
        
        <div className="grid lg:grid-cols-2 gap-8 max-w-6xl mx-auto">
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h2 className="text-2xl font-semibold mb-6 text-gray-800">Available Cars</h2>
            {loading ? (
              <div className="text-center py-8">Loading...</div>
            ) : (
              <div className="space-y-4">
                {cars.map(car => (
                  <div 
                    key={car.id}
                    className={`p-4 border-2 rounded-lg cursor-pointer transition-all hover:shadow-md ${
                      selectedCar?.id === car.id 
                        ? 'border-primary bg-blue-50 shadow-md' 
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                    onClick={() => setSelectedCar(car)}
                  >
                    <h3 className="font-semibold text-lg">{car.make} {car.model}</h3>
                    <p className="text-gray-600">Year: {car.year}</p>
                    <p className="text-sm text-gray-500">Click to select</p>
                  </div>
                ))}
              </div>
            )}
          </div>

          <div className="bg-white rounded-xl shadow-lg p-6">
            <h2 className="text-2xl font-semibold mb-6 text-gray-800">AI Price Calculator</h2>
            {selectedCar ? (
              <div className="space-y-6">
                <div className="bg-gray-50 p-4 rounded-lg">
                  <p className="font-medium">Selected Vehicle:</p>
                  <p className="text-lg">{selectedCar.make} {selectedCar.model}</p>
                </div>
                
                <div>
                  <label className="block text-sm font-medium mb-2">Rental Days:</label>
                  <input 
                    type="number" 
                    value={days}
                    onChange={(e) => setDays(Math.max(1, e.target.value))}
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
                    min="1"
                  />
                </div>
                
                <button 
                  onClick={calculatePrice}
                  disabled={loading}
                  className="w-full bg-primary text-white p-3 rounded-lg hover:bg-secondary transition-colors disabled:opacity-50"
                >
                  {loading ? 'Calculating...' : '🤖 Calculate AI Price'}
                </button>
                
                {price && (
                  <div className="text-center p-6 bg-gradient-to-r from-green-50 to-emerald-50 rounded-lg border border-green-200">
                    <p className="text-sm text-gray-600 mb-1">Estimated Total Cost</p>
                    <p className="text-3xl font-bold text-green-600">${price.toFixed(2)}</p>
                    <p className="text-sm text-gray-500 mt-1">${(price/days).toFixed(2)} per day</p>
                  </div>
                )}
              </div>
            ) : (
              <div className="text-center py-12 text-gray-500">
                <div className="text-4xl mb-4">🚗</div>
                <p>Select a car to see AI-powered pricing</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App