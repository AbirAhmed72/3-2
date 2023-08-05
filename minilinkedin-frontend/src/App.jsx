import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import axios from 'axios';
import React, { useEffect, useState } from 'react';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/register">
          <RegistrationPage />
        </Route>
        <Route path="/login">
          <LoginPage />
        </Route>
        <Route path="/notifications">
          <NotificationPage />
        </Route>
        <Route path="/">
          <HomePage />
        </Route>
      </Routes>
    </Router>
  );
}

function RegistrationPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = async () => {
    try {
      const response = await axios.post('/register', { username, password });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Registration Page</h1>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleRegister}>Register</button>
    </div>
  );
}

function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      const response = await axios.post('/token', { username, password });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Login Page</h1>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

function HomePage() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await axios.get('/post');
        setPosts(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchPosts();
  }, []);

  return (
    <div>
      <h1>Home Page</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>
            <p>{post.text}</p>
            {post.image && <img src={post.image} alt="post" />}
          </li>
        ))}
      </ul>
    </div>
  );
}

function NotificationPage() {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    const fetchNotifications = async () => {
      try {
        const response = await axios.get('/notification');
        setNotifications(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchNotifications();
  }, []);

  const handleNotificationClick = async (notificationId) => {
    try {
      const response = await axios.get(`/notification/${notificationId}/post`);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Notification Page</h1>
      <ul>
        {notifications.map((notification) => (
          <li key={notification.id} onClick={() => handleNotificationClick(notification.id)}>
            <p>{notification.text}</p>
            <p>{notification.datetime}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;