import React from 'react';

const Notification = ({ notifications }) => {
  // Check if notifications is an array, otherwise, set it to an empty array
  const notificationList = Array.isArray(notifications) ? notifications : [];

  return (
    <div>
      <h3>Notifications:</h3>
      {notificationList.length > 0 ? (
        <ul>
          {notificationList.map((notification, index) => (
            <li key={index}>
              <p>{notification.notification_text}</p>
              <p>{notification.notification_datetime}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>No notifications available.</p>
      )}
    </div>
  );
};

export default Notification;
