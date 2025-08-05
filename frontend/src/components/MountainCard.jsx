import React from 'react';

const MountainCard = ({ mountain, onCardClick, backendUrl }) => {
  const imageUrl = `${backendUrl}${mountain.image}`;

  return (
    <div className="col" onClick={onCardClick}>
      <div className="card h-100 border-0 shadow-sm" style={{ cursor: 'pointer' }}>
        <img src={imageUrl} className="card-img-top" alt={mountain.name} style={{ height: '200px', objectFit: 'cover' }} />
        <div className="card-body">
          <h5 className="card-title fw-bold">{mountain.name}</h5>
          <div className="card-text text-secondary">
            <small>△ {mountain.height} m</small>
            <small className="ms-3">📍 {mountain.location}</small>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MountainCard;