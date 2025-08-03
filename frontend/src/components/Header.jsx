import React from "react";

const Header = () => (
  <header className="py-3 mb-1 border-bottom bg-white sticky-top">
    <div className="container d-flex flex-wrap justify-content-between align-items-center">
      <a href="/" className="d-flex align-items-center mb-md-0 me-md-auto text-dark text-decoration-none">
        <span className="fs-4 fw-bold">🏔️ Mountain Explorer</span>
      </a>
      <ul className="nav nav-pills">
        <li className="nav-item"><a href="#" className="nav-link text-dark">Explore</a></li>
        <li className="nav-item"><a href="#" className="nav-link text-dark">About</a></li>
        <li className="nav-item"><a href="#" className="nav-link text-dark">Contact</a></li>
      </ul>
    </div>
  </header>
);

export default Header;


