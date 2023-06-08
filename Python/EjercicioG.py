from interpreter import draw
from chessPictures import *
import copy

def add_pawn():
    pawns = pawn.horizontalRepeat(8)
    return pawns

def negative_pieces(arr):
    arr_negative = []
    for i in arr:
        arr_negative.append(i.negative())

    return arr_negative
        
def add_main_list():
    list_prim = []
    list_prim.append(rock)
    list_prim.append(knight)
    list_prim.append(bishop)

    main_list = copy.deepcopy(list_prim)
    main_list.append(queen)
    main_list.append(king)
    main_list.extend(list(reversed(list_prim)))

    return main_list

def add_pieces(assignment):

    #Crear un Picture con los peones blancos
    picture_pawns = pawn.horizontalRepeat(8)

    #Crear un lista con las piezas principales en blanco
    main_list = add_main_list()

    #Creacion de una lista con piezas principales y peones negros
    main_list_black = negative_pieces(main_list)
    picture_pawns_black = picture_pawns.negative()
    

    pieces_black = main_list_black[0]

    for i in range(len(main_list)-1):
        pieces_black = pieces_black.join(main_list_black[i+1])

        if(i == 6):
            pieces_black = pieces_black.under(picture_pawns_black)
            space = square.negative().join(square).horizontalRepeat(4)
            space2 = square.join(square.negative()).horizontalRepeat(4)
            space_vacio = space.under(space2).verticalRepeat(2)
            pieces_black = pieces_black.under(space_vacio)

    pieces = picture_pawns

    pieces_white = main_list[0]
    for i in range(len(main_list)-1):
        pieces_white = pieces_white.join(main_list[i+1])
        
    pieces = pieces.under(pieces_white)
    
    pieces = pieces.up(pieces_black)

    return pieces




picture1 = square.negative().join(square).horizontalRepeat(4)
picture2 = square.join(square.negative()).horizontalRepeat(4)

picture_complete = picture1.under(picture2).verticalRepeat(4)
        
pieces = add_pieces("negative")

draw(picture_complete, pieces)