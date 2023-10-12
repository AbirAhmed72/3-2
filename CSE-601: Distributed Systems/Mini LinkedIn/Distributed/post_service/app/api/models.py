from sqlalchemy import Column, Integer, String
from post_service.app.api.database import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    post_text = Column(String, nullable=False)
    image_url = Column(String(255))
    user_id = Column(Integer, nullable=False)  # Store user_id locally
    # Other post fields
