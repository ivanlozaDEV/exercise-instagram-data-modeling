import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    firstname = Column(String(250), nullable= False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique= True, nullable= False)

    posts = relationship('Post', backref='author')
    comments = relationship('Comment', backref='author')
    followers = relationship('Follower', backref='followers')
    
    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))

    comments = relationship('Comment', backref= 'post')
    media = relationship('Media', backref='post')
   

class Comment(Base):
    __tablename__= 'comments'

    id = Column(Integer, primary_key= True)
    commented_text = Column(String)

    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    

class Follower(Base):
    __tablename__ = 'followers'

    id = Column(Integer, primary_key= True)

    user_id = Column(Integer, ForeignKey('user.id'))
   

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    media_type = Column(Enum('image', 'video'))

     
    post_id = Column(Integer, ForeignKey('post.id'))






## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
