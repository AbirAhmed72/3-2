import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/navbarStyles.css';

const Navbar = ({ handleLogout, notifications }) => {
  return (
    <div>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <button onClick={handleLogout}>Logout</button>
          </li>
          <li>
            <Link to="/notifications">
              Notifications ({notifications.length})
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Navbar;
