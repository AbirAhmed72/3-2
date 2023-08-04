import React, { useEffect, useState } from "react";
import { getPosts } from "../api";

function Home() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    getPosts()
      .then((response) => setPosts(response.data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div>
      <h1>Home</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.pid}>
            <p>{post.post_text}</p>
            {post.image_url && <img src={post.image_url} alt="Post" />}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Home;
