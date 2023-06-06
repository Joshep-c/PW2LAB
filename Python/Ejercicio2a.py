from interpreter import draw
from chessPictures import *



figura_caballo = Picture(KNIGHT)
figura_caballo2 = Picture(KNIGHT)

figura_caballo3 = figura_caballo.join(figura_caballo2)


draw(figura_caballo3)