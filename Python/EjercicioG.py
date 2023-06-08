from interpreter import draw
from chessPictures import *

fil1 = square.negative().join(square).horizontalRepeat(4)
fil2 = square.join(square.negative()).horizontalRepeat(4)

fil3 = fil1.under(fil2).verticalRepeat(4)
        
pieces = rock.negative()
pieces = pieces.join(knight)
pieces = pieces.join(bishop)

draw(fil3, pieces)