from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

engine = create_engine('sqlite:///pine_cones.db')

class Tile(Base):
    __tablename__ = 'tiles'

    coordinates = Column(String(2), primary_key=True)
    art = Column(String())
    north = Column(String(2), ForeignKey("tiles.coordinates"))
    east = Column(String(2), ForeignKey("tiles.coordinates"))
    south = Column(String(2), ForeignKey("tiles.coordinates"))
    west = Column(String(2), ForeignKey("tiles.coordinates"))
    contents = Column(Integer(), ForeignKey("contents.id"))
    #TODO relationships

    def __repr__(self):
        return f"Coordinates: {self.coordinates}" #TODO add relevant info
    
class Contents(Base):
    __tablename__ = 'contents'

    id = Column(Integer(), primary_key=True)
    description = Column(String())
    has_pine_cone = Column(BOOLEAN())
    specialoptions = Column(Integer(), ForeignKey("specialoptions.id"))
    flag = Column(Integer(), ForeignKey("flags.id"))

    def __repr__(self):
        return f"Description: {self.description}" #TODO add relevant info

class Specialoptions(Base):
    __tablename__ = 'specialoptions'

    id = Column(Integer(), primary_key=True)
    climb = Column(BOOLEAN())
    dig = Column(BOOLEAN())
    chop = Column(BOOLEAN())
    meditate = Column(BOOLEAN())
    portal = Column(BOOLEAN())

    def __repr__(self):
        return f"Options: climb: {self.climb}," \
        + f"dig: {self.dig}," \
        + f"chop: {self.chop}," \
        + f"meditate: {self.meditate}," \
        + f"portal: {self.portal}," \
        
class Flag(Base):
    __tablename__ = 'flags'

    id = Column(Integer(), primary_key=True)
    required = Column(BOOLEAN())
    acquired = Column(BOOLEAN())
    is_collection = Column(BOOLEAN())
    allows = Column(String())
    description = Column(String())

    def __repr__(self):
        return f"Description: {self.description}," \
        + f"required: {self.required}," \
        + f"acquired: {self.acquired}" \
        + f"allows: {self.allows}"


