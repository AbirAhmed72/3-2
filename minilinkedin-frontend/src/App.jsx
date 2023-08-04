import React, { useContext, useEffect, useState } from "react";

import Register from "./components/Register";
import Login from "./components/Login";
import Header from "./components/Header";
// import Table from "./components/Table";
import Post from "./components/Post";
import Notifications from "./components/Notifications";
import { UserContext } from "./context/UserContext";
import Home from "./components/Home";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
const App = () => {
  const [message, setMessage] = useState("");
  const [token] = useContext(UserContext);

  const getWelcomeMessage = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch("/", requestOptions);
    const data = await response.json();

    if (!response.ok) {
      console.log("something messed up");
    } else {
      setMessage(data.message);
    }
  };

  useEffect(() => {
    getWelcomeMessage();
  }, []);

  return (
    <>
      <Header title={message} />
      <div className="columns">
        <div className="column"></div>
        <div className="column m-5 is-two-thirds">
          {!token ? (
            <div className="columns">
              <Register /> <Login />
            </div>
          ) : (
            <Routes>
                <Route exact path="/" component={Home} />
                <Route exact path="/notifications" component={Notifications} />
                <Route exact path="/post/:postId" component={Post} />
              </Routes>
            
          )}
        </div>
        <div className="column"></div>
      </div>
    </>
  );
};

export default App;
