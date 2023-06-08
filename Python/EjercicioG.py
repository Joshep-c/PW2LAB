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
        

def add_pieces(num):
    list_prim = []
    list_prim.append(rock)
    list_prim.append(knight)
    list_prim.append(bishop)


    main_list = copy.deepcopy(list_prim)
    main_list.append(queen)
    main_list.append(king)
    main_list.extend(list(reversed(list_prim)))

    if num == "negative":
        main_list = negative_pieces(main_list)
      
    pieces = main_list[0]

    for i in range(len(main_list)-1):
        pieces = pieces.join(main_list[i+1])

    return pieces



fil1 = square.negative().join(square).horizontalRepeat(4)
fil2 = square.join(square.negative()).horizontalRepeat(4)

fil3 = fil1.under(fil2).verticalRepeat(4)
        
pieces = add_pieces("negative")

draw(fil3, pieces)