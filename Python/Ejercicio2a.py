from interpreter import draw
from chessPictures import *

fil = knight
fil1 = king
fil2 = fil.rotate()

draw(fil.join(fil2))