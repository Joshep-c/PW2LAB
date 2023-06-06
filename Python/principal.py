import pygame
from colors import *
from picture import *
from pieces import *

WIDTH, HEIGHT = 800, 800
BACKGROUND_COLOR = color[' ']
PIECE_COLOR = color['_']

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ajedrez")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()


pygame.quit()





