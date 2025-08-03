import React, { useState, useEffect} from 'react';
import Header from "../components/Header";
import Footer from "../components/Footer";
import MountainGrid from '../components/MountainGrid';
import MountainModal from '../components/MountainModal';
// import { mockMountains } from "./data/mockMountains"; 

// Define the URL where FastAPI backend is running
const BACKEND_URL = "http://127.0.0.1:8000/";

function App() {
  const [mountains, setMountains] = useState(mockMountains);
  const [filteredMountains, setFilteredMountains] = useState(mountains);
  const [selectedContinent, setSelectedContinent] = useState('All');
  const [selectedMountain, setSelectedMountain] = useState(null);

  // Run once when the app loads to fetch data
  useEffect(() => {
    const fetchMountains = async () => {
      try {
        const response = await fetch(`${BACKEND_URL}/api/mountains`);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setMountains(data);
      } catch (error) {
        console.log("Failed to fetch mountains:", error);
      }
    };
    fetchMountains();
  }, []);

  // Handles the filtering logic
  useEffect(() => {
    if (selectedContinent === 'All') {
      setFilteredMountains(mountains);
    } else {
      setFilteredMountains(mountains.filter(m => m.continent === selectedContinent));
    }
  }, [selectedContinent, mountains]);

  const continents = ['All', ...new Set(mountains.map(m => m.continent))];

  return (
    <div className="d-flex flex-column" style={{minHeight: '100vh'}}>
      <Header />

      {/* Main content area */}
      <main className='container my-5 flex-grow-1'>
        <div className='text-center p-md-5 mb-4'>
          <h1 className='display-4 fw-bold'>Discover Famous Mountains</h1>
          <p className='lead text-muted'> 
            Explore majestic peaks, learn fascinating facts, and plan your next mountain adventure.
          </p>
        </div>

        {/* Filter Dropdown */}
        <div className='row mb-4 align-items-center'>
          <div className='col-md-3'>
            <label htmlFor="continent-filter" className='form-label fw-bold'>Filter by Continent:</label>
          </div>
          <div className='col-md-9'>
            <select  
            id="continent-filter"
            className='form-select'
            value={selectedContinent}
            onChange={(e) => setSelectedContinent(e.target.value)}
            >
            {continents.map(continent => (
              <option key={continent} value={continent}>{continent}</option>
            ))}
            </select>
          </div>
        </div>

        
        {/* <div className="row mb-4 align-items-center">
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
        </div>        */}

        <MountainGrid 
          mountains={filteredMountains}
          // Pass a function to set the selected mountain when a card is clicked
          onCardClick={(mountain) => setSelectedMountain(mountain)}
          backendUrl={BACKEND_URL} // Pass the backend URL to the grid
        />
      </main>
      <Footer />
      
      {/* Render the modal and pass the selected mountain and close function */}
      <MountainModal 
        mountain={selectedMountain}
        onClose={() => setSelectedMountain(null)}
        backendUrl={BACKEND_URL} // Pass the backend URL to the modal
      />
    </div>
  );
}

export default App;