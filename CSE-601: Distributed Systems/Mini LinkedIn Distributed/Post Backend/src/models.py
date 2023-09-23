# # models.py
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint
# from database import Base

# from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, DateTime

# class User(Base):
#     __tablename__ = 'users'
#     uid = Column(Integer, primary_key=True, index=True)
#     username = Column(String(100), nullable=False)
#     password_hashed = Column(String)
#     posts = relationship('Post', back_populates='users')
#     notifications = relationship('Notification', back_populates='users')


# class Post(Base):
#     __tablename__ = 'posts'
#     pid = Column(Integer, primary_key=True, index=True)
#     post_text = Column(String, nullable=False)
#     image_url = Column(String(255))
#     created_at = Column(TIMESTAMP)
#     username = Column(String(100), ForeignKey('users.username'), nullable=False)

#     # Relationship with User table
#     users = relationship('User', back_populates='posts')
#     notifications = relationship('Notification', back_populates='posts')


# class Notification(Base):
#     __tablename__ = 'notifications'
#     nid = Column(Integer, primary_key=True, index=True)
#     username = Column(String(100), ForeignKey('users.username'), nullable=False)
#     pid = Column(Integer, ForeignKey('posts.pid'), nullable=False)
#     notification_text = Column(String(50), nullable=False)
#     is_read = Column(Boolean, default=False)
#     created_at = Column(TIMESTAMP)

#     # Relationship with User table
#     users = relationship('User', back_populates='notifications')
#     # Relationship with Post table
#     posts = relationship('Post', back_populates='notifications')

from datetime import datetime


# You can remove these imports as they are not needed when using MongoDB.
# from database import Base

# Define your models for MongoDB collections
class User:
    def __init__(self, username: str, password_hashed: str):
        self.username = username
        self.password_hashed = password_hashed

class Post:
    def __init__(self, post_text: str, image_url: str, created_at: datetime, username: str):
        self.post_text = post_text
        self.image_url = image_url
        self.created_at = created_at
        self.username = username

class Notification:
    def __init__(self, username: str, pid: int, notification_text: str, is_read: bool, created_at: datetime):
        self.username = username
        self.pid = pid
        self.notification_text = notification_text
        self.is_read = is_read
        self.created_at = created_at
