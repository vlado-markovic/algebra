from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    books = relationship('Book', back_populates='author')

class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    authors = relationship('Author', secondary='publisher_author')
    books = relationship('Book', back_populates='publisher')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)
    availability = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    author = relationship('Author', back_populates='books')
    publisher = relationship('Publisher', back_populates='books')

publisher_author = Table('publisher_author', Base.metadata,
    Column('publisher_id', Integer, ForeignKey('publishers.id')),
    Column('author_id', Integer, ForeignKey('authors.id'))
)
