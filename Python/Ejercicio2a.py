from interpreter import draw
from chessPictures import *

fil = knight.join(knight.negative())
fil2 = fil.verticalMirror()

draw(fil.up(fil2))