from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb
from db.models import Base, Tile, Contents, Specialoptions, Flag

engine = create_engine('sqlite:///db/pine_cones.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class Progression():
    def __init__(self, pine_cones):
        self.pine_cones = pine_cones
    
    def pick_up_pine_cone(self):
        self.pine_cones += 1
    
    def check_completed(self):
        if self.pine_cones == 2:
            return True
        else: return False

user = Progression(0) #quick. and. dirty.

def cli_start():
    """Entry point of the interface"""
    greeting()

def show_map(tile):
    """Print a map of N,E,S,W from the current location"""
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
    """Description of the game, input to start or look at the map"""

    print("Welcome to the pine cone based text adventure!")
    print('''
    select by typing the letter inside ():
    start game: (s)
    quit: (q)
    ''')

    select = input()
    while select != 'q':
        if select == 's':
            start_game()
            select = ''
    farewell()
    
def start_game():
    """Sets the start location, leads into the main game loop"""
    tile = session.query(Tile).get("B3")
    show_help_text()
    prompt_input(tile)

def prompt_input(tile):
    """Main game loop, movement and interaction with tiles"""
    valid_commands = ['m', 'n', 'e', 's', 'w', 'i', 'q', 'h', '']
    select = ''
    while select != 'q':
        #ipdb.set_trace()
        select = input()
        if select in valid_commands:
            if select == 'm':
                show_map(tile)
            if select == 'n' or select == 'e' or select == 's' or select == 'w': 
                attempt = try_to_move(tile, select)
                if attempt != False:
                    tile = attempt
            if select == 'i':
                inspect_location(tile)
            if select == 'h':
                show_help_text()
        else: 
            print("not a valid command!")
    farewell()

def try_to_move(tile, direction):
    """Attempt to move in a cardinal direction. 
    If there is a tile in that direction,
    returns that tile, else returns False    
    """
    if direction == 'n':
        if tile.north != '':
            print(f"moving north! now at {tile.north}")
            return session.query(Tile).get(tile.north)
    if direction == 'e':
        if tile.east != '':
            print(f"moving east! now at {tile.east}")
            return session.query(Tile).get(tile.east)
    if direction == 'w':
        if tile.west != '':
            print(f"moving west! now at {tile.west}")
            return session.query(Tile).get(tile.west)
    if direction == 's':
        if tile.south != '':
            print(f"moving south! now at {tile.south}")
            return session.query(Tile).get(tile.south)
    print("I tried to move. There's nothing in that direction that I can move to!")
    return False

def inspect_location(tile):
    """Secondary game loop, do things specific to tiles, such as
    pick up pine cones, climb trees, meditate, go through portals
    """
    print()
    print("its a tile! I'm not written yet!")
    #TODO write this lol

def farewell():
    """End script"""
    print("Thank you for playing!")
    exit()

def show_help_text():
    """Display generic options for use throughout the game"""
    print('''
    select by typing the letter inside ():
    view map: (m)
    go north: (n)
    go east: (e)
    go south: (s)
    go west: (w)
    inspect current location: (i)
    show this menu: (h)
    quit: (q)
    ''')