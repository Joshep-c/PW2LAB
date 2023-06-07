from interpreter import draw
from chessPictures import *

fil = knight.join(knight.negative())
fil2 = knight.negative().join(knight)

draw(fil.under(fil2))