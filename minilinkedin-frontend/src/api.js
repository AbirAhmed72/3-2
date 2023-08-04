import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000'; // Replace this with your backend API URL

export function setAuthToken(token) {
  if (token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  } else {
    delete axios.defaults.headers.common['Authorization'];
  }
}

export function registerUser(userData) {
  return axios.post(`${BASE_URL}/register`, userData);
}

export function loginUser(formData) {
  return axios.post(`${BASE_URL}/token`, formData);
}

export function createPost(postData) {
  return axios.post(`${BASE_URL}/post`, postData);
}

export function getPosts() {
  return axios.get(`${BASE_URL}/post`);
}

export function getNotifications() {
  return axios.get(`${BASE_URL}/notification`);
}

// Add other API request functions as needed
