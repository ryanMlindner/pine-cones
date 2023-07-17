from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Base, Tile, Contents, Specialoptions, Flag

engine = create_engine('sqlite:///db/book_stores.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def cli_start():
    input = ''
    greeting()
    show_options("B3")
    #TODO decide where to put logic for stuff. my brain has exploded.

def show_options(coordinates):
    #TODO modularize options for each set of NESW and options? or...
    pass

def greeting():
    print("TODO! Make me say something fun!")