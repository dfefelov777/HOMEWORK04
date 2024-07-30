"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os
from sqlalchemy.ext.asyncio import  create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import Column, Integer, String, ForeignKey

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:example@localhost:5433/blog"

engine = create_async_engine(PG_CONN_URI,echo=True)

Base = declarative_base()

Session= sessionmaker(
    bind=engine,
    class_= AsyncSession,
    expire_on_commit=False
)

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(32),nullable=False,unique=True)
    email=Column(String,nullable=True,unique=True)
    posts = relationship(
        # to class name
        "Post",
        back_populates="user"
    )

class Post(Base):
    __tablename__="posts"
    id=Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title=Column(String(32),nullable=False,unique=True)
    body=Column(String,nullable=True,unique=True)
    users = relationship(
        # to class name
        "User",
        back_populates="posts"
    )



