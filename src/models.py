import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'person'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    user_fav = Column(String(100), nullable=False)
    fav_num = Column(Integer, ForeignKey=True)

class Characters(Base):
    __tablename__ = 'Characters'
    character_id = Column(Integer, primary_key=True)
    character_name = Column(String(100), unique=True, nullable=False)
    height = Column(String(6), unique=True, nullable=False)
    mass = Column(String(6), unique=True, nullable=False)
    hair_color = Column(String(6), unique=True, nullable=False)
    skin_color = Column(String(6), unique=True, nullable=False)
    eye_color = Column(String(6), unique=True, nullable=False)
    birth_year = Column(String(8), unique=True, nullable=False)
    gender = Column(String(8), unique=True, nullable=False)
    homeworld =  Column(String(50), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey=True) 
   
class Planets(Base):
    __tablename__ = 'Planets'
    planets_id = Column(Integer, primary_key=True)
    planet_name = Column(String(100), unique=True, nullable=False) 
    diameter = Column(Integer, unique=True, nullable=False)
    rotation_period = Column(String(5), unique=True, nullable=False)
    orbital_period = Column(String(5), unique=True, nullable=False)
    gravity = Column(String(20), unique=True, nullable=False) 
    population = Column(String(20), unique=True, nullable=False)
    climate = Column(String(10), unique=True, nullable=False)
    terrain = Column(String(10), unique=True, nullable=False)
    surface_water =  Column(Integer, unique=True, nullable=False)
    url =  Column(String(5), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey=True)
        
class Starships(Base):
    __tablename__ = 'Starships'
    starships_id = Column(Integer, primary_key=True)
    starships_name = Column(String(100), unique=True, nullable=False) 
    starship_class = Column(String(100), unique=True, nullable=False) 
    model = Column(String(100), unique=True, nullable=False) 
    manufacturer = Column(String(150), unique=True, nullable=False) 
    cost_in_credits = Column(String(100), unique=True, nullable=False) 
    length = Column(Integer, unique=True, nullable=False) 
    crew = Column(Integer, unique=True, nullable=False) 
    passengers = Column(Integer, unique=True, nullable=False) 
    max_atmosphering_speed = Column(String(30), unique=True, nullable=False) 
    hyperdrive_rating = Column(Integer, unique=True, nullable=False) 
    MGLT = Column(Integer, unique=True, nullable=False) 
    user_id = Column(Integer, ForeignKey=True)
    elem_id = Column(Integer, ForeignKey=True, nullable=False)
    
class Favorites(Base):
    __tablename__ = 'Favorites'
    fav_id = Column(Integer, primary_key=True)
    elem_id = Column(Integer, ForeignKey=True, nullable=False)
    fav_num = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey=True)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')