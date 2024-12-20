from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    posts = relationship("Post", back_populates="owner")


class Post(Base):
    __tablename__ = "Posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("Users.id"))

    owner = relationship("User", back_populates="posts")