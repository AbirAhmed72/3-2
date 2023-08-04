import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';

const API_BASE_URL = 'http://127.0.0.1:8000'; // Replace with your actual backend API base URL

const HomePage = () => {
  const [posts, setPosts] = useState([]);
  const [loggedIn, setLoggedIn] = useState(false);
  const [postText, setPostText] = useState('');
  const [selectedImage, setSelectedImage] = useState(null);
  const [notifications, setNotifications] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const access_token = localStorage.getItem('access_token');
    if (access_token) {
      setLoggedIn(true);
      fetchPosts(access_token);
      fetchNotifications(access_token);
    }
  }, []);

  const fetchPosts = (access_token) => {
    axios
      .get(`${API_BASE_URL}/post`, {
        headers: {
          Authorization: `Bearer ${access_token}`,
        },
      })
      .then((response) => {
        setPosts(response.data);
      })
      .catch((error) => {
        console.error('Error fetching posts:', error);
      });
  };

  const fetchNotifications = (access_token) => {
    axios
      .get(`${API_BASE_URL}/notification`, {
        headers: {
          Authorization: `Bearer ${access_token}`,
        },
      })
      .then((response) => {
        setNotifications(response.data);
      })
      .catch((error) => {
        console.error('Error fetching notifications:', error);
      });
  };

  const handleLogout = () => {
    // Clear the access token from local storage
    localStorage.removeItem('access_token');
    // Navigate to the login page after logout
    navigate('/login');
  };

  const handlePostTextChange = (event) => {
    setPostText(event.target.value);
  };

  const handleImageChange = (event) => {
    setSelectedImage(event.target.files[0]);
  };

  const handleSubmitPost = () => {
    const formData = new FormData();
    formData.append('post_text', postText); // Make sure 'postText' holds the user's post text
    if (selectedImage) {
      formData.append('image', selectedImage); // Make sure 'selectedImage' holds the user's selected image
    }

    const access_token = localStorage.getItem('access_token');

    // Make a POST request to create a new post
    axios
      .post(`${API_BASE_URL}/post`, formData, {
        headers: {
          Authorization: `Bearer ${access_token}`,
          'Content-Type': 'multipart/form-data', // Set the correct content type for the form data
        },
      })
      .then((response) => {
        // Refresh the posts after successful submission
        fetchPosts(access_token);
      })
      .catch((error) => {
        console.error('Error submitting post:', error.response);
      });
  };

  return (
    <div>
      {loggedIn ? (
        <div>
          <h2>Welcome to Your Home Page</h2>
          <button onClick={handleLogout}>Logout</button>
          <div>
            <h3>Create a New Post</h3>
            <textarea
              rows={4}
              cols={50}
              value={postText}
              onChange={handlePostTextChange}
              placeholder="Enter your post text"
            />
            <input type="file" onChange={handleImageChange} />
            <button onClick={handleSubmitPost}>Submit Post</button>
          </div>
          {posts.length > 0 ? (
            <div>
              <h3>Posts from Other Users:</h3>
              {/* Render the posts */}
              {posts.map((post) => (
                <div key={post.pid}>
                  <p>{post.username}</p>
                  <p>{post.post_text}</p>
                  {post.image_url && <img src={post.image_url} alt="Post" />}
                </div>
              ))}
            </div>
          ) : (
            <p>No posts available.</p>
          )}
          {notifications.length > 0 && (
            <div>
              <h3>Notifications ({notifications.length})</h3>
              {/* Render the notifications */}
              {notifications.map((notification, index) => (
                <div key={index}>
                  <p>{notification.notification_text}</p>
                  <p>{notification.notification_datetime}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      ) : (
        <div>
          <h2>Welcome to the Homepage</h2>
          <p>You are not logged in.</p>
          <p>
            <Link to="/login">Login</Link> or <Link to="/register">Register</Link> to view posts.
          </p>
        </div>
      )}
    </div>
  );
};

export default HomePage;
