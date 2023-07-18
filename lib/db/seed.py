from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from gamedescriptions import *

from models import Tile, Contents, Specialoptions, Flag

engine = create_engine('sqlite:///pine_cones.db')
Session = sessionmaker(bind = engine)
session = Session()

if __name__ == '__main__':
    session.query(Tile).delete()
    session.query(Contents).delete()
    session.query(Specialoptions).delete()
    session.query(Flag).delete()

    tileA3 = Tile(coordinates="A3", art="", north="", 
                  east="B3", south="", west="",
                  contents=1)
    tileB3 = Tile(coordinates="B3", art="", north="", 
                  east="C3", south="B4", west="A3",
                  contents=2)
    tileC3 = Tile(coordinates="C3", art="", north="C2", 
                  east="D3", south="C4", west="B3",
                  contents=3)
    tileD3 = Tile(coordinates="D3", art="", north="", 
                  east="E3", south="", west="C3",
                  contents=4)
    tileE3 = Tile(coordinates="E3", art="", north="", 
                  east="", south="", west="D3",
                  contents=5)
    tileB4 = Tile(coordinates="B4", art="", north="B3", 
                  east="C4", south="", west="",
                  contents=6)
    tileC4 = Tile(coordinates="C4", art="", north="C3", 
                  east="", south="", west="B4",
                  contents=7)
    tileC2 = Tile(coordinates="C2", art="", north="", 
                  east="", south="C3", west="",
                  contents=8)
    
    contentsA3 = Contents(id=1, description=oracle(), has_pine_cone=False)
    contentsB3 = Contents(id=2, description=start(), has_pine_cone=False)
    contentsC3 = Contents(id=3, description=baby_tree(), has_pine_cone=False,
                          specialoptions=1)
    contentsD3 = Contents(id=4, description=house(), has_pine_cone=True, 
                          flag=1)
    contentsE3 = Contents(id=5, description=basement(), has_pine_cone=False,
                          specialoptions=2)
    contentsB4 = Contents(id=6, description=portal(), has_pine_cone=False,
                          specialoptions=3)
    contentsC4 = Contents(id=7, description=field(), has_pine_cone=False)
    contentsC2 = Contents(id=8, description=twin_trees(), has_pine_cone=True,
                          flag=2)

    specialoptionsC3 = Specialoptions(id=1, meditate=True)
    specialoptionsE3 = Specialoptions(id=2, dig=True)
    specialoptionsB4 = Specialoptions(id=3, portal=True)

    flagD3 = Flag(id=1, required=True, acquired=False,
                  is_collection=True, description="Blue Pine Cone")
    flagC2 = Flag(id=2, required=True, acquired=False,
                  is_collection=True, description="Yellow Pine Cone")



    session.add_all([tileA3,tileB3,tileB4,tileC3,
                     tileC2,tileC4,tileD3,tileE3,
                     contentsA3,contentsB3,contentsC3,contentsD3,
                     contentsE3,contentsB4,contentsC4,contentsC2,
                     specialoptionsC3,specialoptionsE3,specialoptionsB4,
                     flagD3,flagC2])
    session.commit()
