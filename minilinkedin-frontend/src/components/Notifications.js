import React, { useEffect, useState } from "react";
import { getNotifications } from "../api";
import { Link } from "react-router-dom";

function Notifications() {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    // Fetch notifications when the component mounts
    fetchNotifications();
  }, []);

  const fetchNotifications = async () => {
    try {
      const response = await getNotifications();
      setNotifications(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Notifications</h2>
      <ul>
        {notifications.map((notification) => (
          <li key={notification.notification_datetime}>
            <Link to={`/post/${notification.post_id}`}>
              <p>{notification.notification_text}</p>
              <p>
                Notification Date:{" "}
                {new Date(notification.notification_datetime).toLocaleString()}
              </p>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Notifications;
