from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Base, Tile, Contents, Specialoptions, Flag

engine = create_engine('sqlite:///db/pine_cones.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def cli_start():
    """Entry point of the interface"""
    greeting()
    show_map("B3")
    #TODO decide where to put logic for stuff. my brain has still exploded.

def show_map(coordinates):
    """Print a map of N,E,S,W from the current location"""
    tile = session.query(Tile).get(coordinates)
    print(tile)
    contents = session.query(Contents).get(tile.contents)
    print(contents)

    # this is gross. but it works.
    north = ' X'
    if (tile.north != ''):
        north = tile.north
    east = ' X'
    if (tile.east != ''):
        east = tile.east
    south = ' X'
    if (tile.south != ''):
        south = tile.south
    west = ' X'
    if (tile.west != ''):
        west = tile.west
    print('''
      ┌─────┐
      | %s  |
┌─────┼─────┼─────┐
| %s  |  X  | %s  |
└─────┼─────┼─────┘
      | %s  |
      └─────┘
          '''%(north, west, east, south))

def greeting():
    print("TODO! Make me say something fun!")
    # select = input()