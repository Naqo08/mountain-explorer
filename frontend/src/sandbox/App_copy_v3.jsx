import React, { useState, useEffect } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import MountainGrid from '../components/MountainGrid';
import MountainModal from '../components/MountainModal';

// Define the URL where your FastAPI backend is running
const BACKEND_URL = "http://127.0.0.1:8000";

function App() {
  const [mountains, setMountains] = useState([]);
  const [filteredMountains, setFilteredMountains] = useState([]);
  const [selectedContinent, setSelectedContinent] = useState('All');
  const [selectedMountain, setSelectedMountain] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // This effect will run once when the app loads to fetch data
  useEffect(() => {
    const fetchMountains = async () => {
      try {
        console.log('Fetching mountains from:', `${BACKEND_URL}/api/mountains`);
        const response = await fetch(`${BACKEND_URL}/api/mountains`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Fetched mountains:', data);
        setMountains(data);
        setError(null);
      } catch (error) {
        console.error("Failed to fetch mountains:", error);
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };
    fetchMountains();
  }, []);

  // This effect handles the filtering logic
  useEffect(() => {
    if (selectedContinent === 'All') {
      setFilteredMountains(mountains);
    } else {
      setFilteredMountains(mountains.filter(m => m.continent === selectedContinent));
    }
  }, [selectedContinent, mountains]);

  const continents = ['All', ...new Set(mountains.map(m => m.continent))];

  if (loading) {
    return (
      <div className="d-flex justify-content-center align-items-center" style={{ minHeight: '100vh' }}>
        <div className="spinner-border" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="d-flex justify-content-center align-items-center" style={{ minHeight: '100vh' }}>
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p>Failed to load mountains: {error}</p>
          <hr />
          <p className="mb-0">Please make sure the backend server is running on {BACKEND_URL}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="d-flex flex-column" style={{ minHeight: '100vh' }}>
      <Header />
      <main className="container my-5 flex-grow-1">
        <div className="text-center p-md-5 mb-4">
          <h1 className="display-4 fw-bold">Discover Famous Mountains</h1>
          <p className="lead text-muted">
            Explore majestic peaks, learn fascinating facts, and plan your next mountain adventure.
          </p>
        </div>

        <div className="row mb-4 align-items-center">
          <div className="col-md-3">
            <label htmlFor="continent-filter" className="form-label fw-bold">Filter by Continent:</label>
          </div>
          <div className="col-md-9">
            <select
              id="continent-filter"
              className="form-select"
              value={selectedContinent}
              onChange={(e) => setSelectedContinent(e.target.value)}
            >
              {continents.map(continent => (
                <option key={continent} value={continent}>{continent}</option>
              ))}
            </select>
          </div>
        </div>

        <MountainGrid
          mountains={filteredMountains}
          onCardClick={(mountain) => setSelectedMountain(mountain)}
          backendUrl={BACKEND_URL}
        />
      </main>
      <Footer />
      <MountainModal
        mountain={selectedMountain}
        onClose={() => setSelectedMountain(null)}
        backendUrl={BACKEND_URL}
      />
    </div>
  );
}

export default App;