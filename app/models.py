
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, func

from app import db


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True ,nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    posts: Mapped[list['Post']] = relationship(back_populates='user')



class Post(db.Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    imagem: Mapped[str] = mapped_column(String(255), nullable=True)
    data: Mapped[datetime] = mapped_column(server_default=func.now())
    content: Mapped[str] = mapped_column(nullable=True)
    author: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='posts')
