import pygame
from colors import *
from picture import *
from pieces import *
from pygame import *

def draw_tower(w, h):
    WIDTH, HEIGHT = w, h
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ajedrez")
    

apertura = True
count = 0

while apertura:
    pygame.init()
    draw_tower(800, 800)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_RETURN):
                running = False
        pygame.display.update()

    pygame.quit()
    count += 1
    if count == 7:
        apertura = False






    


    



