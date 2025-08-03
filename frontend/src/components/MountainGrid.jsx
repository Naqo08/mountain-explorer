import React from 'react';
import MountainCard from './MountainCard';

const MountainGrid = ({ mountains, onCardClick, backendUrl }) => (
  <div className="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
    {Array.isArray(mountains) && mountains.map((mountain) => (
      <MountainCard 
        key={mountain.id}
        mountain={mountain} 
        onCardClick={() => onCardClick(mountain)}
        backendUrl={backendUrl} 
      />
    ))}
  </div>
);

export default MountainGrid;
