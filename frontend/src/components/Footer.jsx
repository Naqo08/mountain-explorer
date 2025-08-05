import React from "react";

const Footer = () => {
  return ( 
    <footer className="bg-dark text-white py-5">
      <div className="container">
        <div className="row">
          <div className="col-md-5 mb-4"> 
            <h5 className="fw-bold">🏔️ Mountain Explorer</h5>
            <p className="text-white-50"> 
              Discover the world's most magnificent peaks and plan your next mountain adventure.
            </p>
          </div>
          <div className="col-md-1"></div>
          <div className="col-md-2 mb-4">
            <h5 className="text-uppercase text-white-50">Quick Links</h5> 
            <ul className="list-unstyled">
              <li><a href="#" className="text-white text-decoration-none">All Mountains</a></li>
              <li><a href="#" className="text-white text-decoration-none">By Continent</a></li> 
              <li><a href="#" className="text-white text-decoration-none">Climbing Guides</a></li>
              <li><a href="#" className="text-white text-decoration-none">Safety Tips</a></li>
            </ul>
          </div>
          <div className="col-md-2 mb-4">
            <h5 className="text-uppercase text-white-50">Connect</h5>
            <ul className="list-unstyled">
              <li><a href="#" className="text-white text-decoration-none">About Us</a></li>
              <li><a href="#" className="text-white text-decoration-none">Contact</a></li>
              <li><a href="#" className="text-white text-decoration-none">Newsletter</a></li>
              <li><a href="#" className="text-white text-decoration-none">Privacy Policy</a></li>
            </ul>
          </div>
        </div>
        <div className="text-center text-white-50 pt-4 mt-4 border-top border-secondary">
          &copy; 2025 Mountain Explorer. All rights reserved.
        </div>
      </div>
    </footer>
  );
};

export default Footer;