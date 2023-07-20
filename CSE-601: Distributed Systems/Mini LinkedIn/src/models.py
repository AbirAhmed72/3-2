from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint
from database import Base

from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, DateTime

class User(Base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)

class Post(Base):
    __tablename__ = 'posts'
    pid = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    post_text = Column(String, nullable=False)
    image_url = Column(String(255))
    created_at = Column(TIMESTAMP)

    # Relationship with User table
    user = relationship('User', back_populates='posts')

class Notification(Base):
    __tablename__ = 'notifications'
    nid = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    pid = Column(Integer, ForeignKey('posts.post_id'), nullable=False)
    notification_text = Column(String(50), nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP)

    # Relationship with User table
    user = relationship('User', back_populates='notifications')
    # Relationship with Post table
    post = relationship('Post', back_populates='notifications')