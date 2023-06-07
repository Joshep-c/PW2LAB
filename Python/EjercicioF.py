from interpreter import draw
from chessPictures import *

fil1 = square.negative().join(square).horizontalRepeat(4)
fil2 = square.join(square.negative()).horizontalRepeat(4)

fil3 = fil1.under(fil2)

draw(fil3.under(fil3))