import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Link, Routes, Navigate } from 'react-router-dom';
import './App.css';
import axios from 'axios'; // Import Axios

const API_BASE_URL = 'http://127.0.0.1:8000'; // Replace with your actual backend API base URL

function ItemList() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    // Fetch items from the backend using Axios
    axios.get(`${API_BASE_URL}/api/items`)
      .then(response => setItems(response.data))
      .catch(error => console.error('Error fetching items:', error));
  }, []);

  return (
    <div>
      <h2>Item List</h2>
      <ul>
        {items.map((item, index) => (
          <li key={index}>
            <strong>{item.name}</strong>: {item.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>MVC App</h1>
          <nav>
            <Link to="/">Home</Link>
            <Link to="/items">Items</Link>
          </nav>
        </header>
        <Routes>
          <Route path="/" element={<h2>Welcome to the MVC App</h2>} />
          <Route path="/items" element={<ItemList />} />
          <Route path="/*" element={<Navigate to="/" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
