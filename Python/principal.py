import pygame
from colors import *
from picture import Picture
from pieces import *
from pygame.locals import *

def ejercicio_1(w, h):
    WIDTH, HEIGHT = w, h
    BACKGROUND_COLOR = color[' ']
    PIECE_COLOR = color['_']
    
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ajedrez")

    knight_picture = Picture(KNIGHT)
    pixels = []

    for row in knight_picture.img:
        row_pixels = []
        for pixel in row:
            row_pixels.append(color[pixel])
        pixels.append(row_pixels)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_RETURN):
                running = False

        window.fill(BACKGROUND_COLOR)

        # Dibujar la imagen en la ventana
        for y, row in enumerate(pixels):
            for x, pixel_color in enumerate(row):
                pygame.draw.rect(window, pixel_color, (x, y, 1, 1))

        pygame.display.update()

    pygame.quit()

apertura = True
count = 0

while apertura:
    pygame.init()
    ejercicio_1(800, 800)

    count += 1
    if count == 7:
        apertura = False




    


    



