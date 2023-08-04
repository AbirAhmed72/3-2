import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getPostById } from "../api";

function Post() {
  const { postId } = useParams();
  const [post, setPost] = useState(null);

  useEffect(() => {
    async function fetchPostDetails() {
      try {
        const response = await getPostById(postId);
        setPost(response.data);
      } catch (error) {
        console.error("Error fetching post details:", error);
      }
    }
    fetchPostDetails();
  }, [postId]);

  return (
    <div>
      <h1>Post Details</h1>
      {post ? (
        <div>
          <h2>{post.username}</h2>
          <p>{post.post_text}</p>
          {post.image_url && <img src={post.image_url} alt="Post" />}
          <p>Posted on: {new Date(post.post_datetime).toLocaleString()}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default Post;
