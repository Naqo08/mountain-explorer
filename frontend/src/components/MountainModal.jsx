import React, { useState } from "react";

const MountainModal = ({ mountain, onClose, backendUrl }) => {
  const [aiFacts, setAiFacts] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  if (!mountain) return null;

  const handleGenerateFacts = () => {
    setIsLoading(true);
    setAiFacts('');
    fetch(`${backendUrl}/api/mountains/${mountain.id}/ai-facts`)
      .then(res => res.json())
      .then(data => {
        setAiFacts(data.facts || 'Could not retrieve AI facts.');
      })
      .catch((error) => {
        console.error("Error fetching AI facts:", error);
        setAiFacts('An error occurred while fetching data.');
      })
      .finally(() => setIsLoading(false));
  };

  const imageUrl = `${backendUrl}${mountain.image}`;

  return (
    <>
      <div className="modal-backdrop fade show"></div>
      <div className="modal fade show" style={{ display: 'block' }} tabIndex="-1" onClick={onClose}>
        <div className="modal-dialog modal-dialog-centered modal-lg" onClick={(e) => e.stopPropagation()}>
          <div className="modal-content">
            <div className="modal-header border-0">
              <h4 className="modal-title fw-bold">{mountain.name}</h4>
              <button type="button" className="btn-close" onClick={onClose}></button>
            </div>
            <div className="modal-body">
              <img src={imageUrl} className="img-fluid rounded mb-3" alt={mountain.name} />
              <ul className="list-group list-group-flush mb-3">
                <li className="list-group-item"><strong>Location:</strong> {mountain.location}</li>
                <li className="list-group-item"><strong>Height:</strong> {mountain.height} m</li>
                <li className="list-group-item"><strong>Range:</strong> {mountain.range}</li>
                <li className="list-group-item"><strong>First Ascent:</strong> {mountain.first_ascent}</li>
              </ul>
              <div className="d-grid gap-2">
                <button className="btn btn-dark" type="button" onClick={handleGenerateFacts} disabled={isLoading}>
                  {isLoading ? (
                    <>
                      <span className="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                      Generating...
                    </>
                  ) : (
                    '✨ Generate AI Facts'
                  )}
                </button>
              </div>
              {aiFacts && (
                <div className="alert alert-secondary mt-3" role="alert">
                  {aiFacts.split('\n').map((line, index) => (
                    <div key={index} style={{ marginBottom: '8px' }}>
                      {line}
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default MountainModal;