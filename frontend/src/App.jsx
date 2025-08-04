import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import MountainGrid from './components/MountainGrid';
import MountainModal from './components/MountainModal';

const BACKEND_URL = "http://127.0.0.1:8000";

function App() {
  const [mountains, setMountains] = useState([]);
  const [filteredMountains, setFilteredMountains] = useState([]);
  const [activeFilter, setActiveFilter] = useState('All Continents');
  const [selectedMountain, setSelectedMountain] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMountains = async () => {
      try {
        const response = await fetch(`${BACKEND_URL}/api/mountains`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();
        setMountains(data);
        setError(null);
      } catch (e) {
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };
    fetchMountains();
  }, []);

  useEffect(() => {
    if (activeFilter === 'All Continents') {
      setFilteredMountains(mountains);
    } else {
      setFilteredMountains(mountains.filter(m => m.continent === activeFilter));
    }
  }, [activeFilter, mountains]);

  const continents = ['All Continents', ...new Set(mountains.map(m => m.continent))];

  if (loading) {
    return <div className="d-flex vh-100 justify-content-center align-items-center"><div className="spinner-border"></div></div>;
  }
  if (error) {
    return <div className="d-flex vh-100 justify-content-center align-items-center"><div className="alert alert-danger">Failed to load data: {error}</div></div>;
  }

  return (
    <div className="d-flex flex-column" style={{ minHeight: '100vh' }}>
      <Header />
      <main className="container my-3 flex-grow-1">
        {/* Hero Section with rounded corners */}
        <div className="mb-4" style={{
          background: 'linear-gradient(to bottom, #87CEEB 0%, #4682B4 50%, #2F4F4F 100%)',
          borderRadius: '0.5rem',
          color: 'white'
        }}>
          <div className="text-center pt-5 pb-4">
            <h1 className="display-5 fw-bold">Discover Famous Mountains Around the World</h1>
            <p className="lead" style={{ color: '#e6f3ff' }}>
              Explore majestic peaks, learn fascinating facts, and plan your next mountain adventure with our comprehensive mountain database.
            </p>
          </div>

          {/* Filter Section */}
          <div className="d-flex justify-content-between align-items-center border-top border-light border-opacity-25 pt-3 pb-3 px-4">
            <h5 className="mb-0 text-white">Filter Mountains</h5>
            <div className="btn-group" role="group">
              {continents.map(continent => (
                <button
                  key={continent}
                  type="button"
                  className={`btn btn-sm ${activeFilter === continent ? 'btn-light' : 'btn-outline-light'}`}
                  onClick={() => setActiveFilter(continent)}
                >
                  {continent}
                </button>
              ))}
            </div>
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

// import React, { useState, useEffect } from 'react';
// import Header from './components/Header';
// import Footer from './components/Footer';
// import MountainGrid from './components/MountainGrid';
// import MountainModal from './components/MountainModal';

// const BACKEND_URL = "http://127.0.0.1:8000";

// function App() {
//   const [mountains, setMountains] = useState([]);
//   const [filteredMountains, setFilteredMountains] = useState([]);
//   const [activeFilter, setActiveFilter] = useState('All Continents');
//   const [selectedMountain, setSelectedMountain] = useState(null);
//   const [loading, setLoading] = useState(true);
//   const [error, setError] = useState(null);

//   useEffect(() => {
//     const fetchMountains = async () => {
//       try {
//         const response = await fetch(`${BACKEND_URL}/api/mountains`);
//         if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
//         const data = await response.json();
//         setMountains(data);
//         setError(null);
//       } catch (e) {
//         setError(e.message);
//       } finally {
//         setLoading(false);
//       }
//     };
//     fetchMountains();
//   }, []);

//   useEffect(() => {
//     if (activeFilter === 'All Continents') {
//       setFilteredMountains(mountains);
//     } else {
//       setFilteredMountains(mountains.filter(m => m.continent === activeFilter));
//     }
//   }, [activeFilter, mountains]);

//   const continents = ['All Continents', ...new Set(mountains.map(m => m.continent))];

//   if (loading) {
//     return <div className="d-flex vh-100 justify-content-center align-items-center"><div className="spinner-border"></div></div>;
//   }
//   if (error) {
//     return <div className="d-flex vh-100 justify-content-center align-items-center"><div className="alert alert-danger">Failed to load data: {error}</div></div>;
//   }

//   return (
//     <div className="d-flex flex-column" style={{ minHeight: '100vh' }}>
//       <Header />
      
//       <main className="container my-3 flex-grow-1">
//         {/* Background section with container width */}
//         <div style={{
//           background: 'linear-gradient(to bottom, #87CEEB 0%, #4682B4 50%, #2F4F4F 100%)',
//           color: 'white',
//           margin: '0 -15px', // Offset container padding
//           padding: '0 15px'   // Add back the padding for content
//         }}>
//           {/* Hero section */}
//           <div className="text-center pt-5 pb-4">
//             <h1 className="display-5 fw-bold">Discover Famous Mountains Around the World</h1>
//             <p className="lead" style={{ color: '#e6f3ff' }}>
//               Explore majestic peaks, learn fascinating facts, and plan your next mountain adventure with our comprehensive mountain database.
//             </p>
//           </div>

//           {/* Filter section */}
//           <div className="d-flex justify-content-between align-items-center pb-4 border-bottom">
//             <h5 className="mb-0" style={{ color: '#e6f3ff' }}>Filter Mountains</h5>
//             <div className="btn-group" role="group">
//               {continents.map(continent => (
//                 <button
//                   key={continent}
//                   type="button"
//                   className={`btn ${activeFilter === continent ? 'btn-light' : 'btn-outline-light'}`}
//                   onClick={() => setActiveFilter(continent)}
//                 >
//                   {continent}
//                 </button>
//               ))}
//             </div>
//           </div>
//         </div>

//         <div className="mt-4">
//           <MountainGrid
//             mountains={filteredMountains}
//             onCardClick={(mountain) => setSelectedMountain(mountain)}
//             backendUrl={BACKEND_URL}
//           />
//         </div>
//       </main>
      
//       <Footer />
//       <MountainModal
//         mountain={selectedMountain}
//         onClose={() => setSelectedMountain(null)}
//         backendUrl={BACKEND_URL}
//       />
//     </div>
//   );
// }

// export default App;