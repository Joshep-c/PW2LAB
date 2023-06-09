import pygame, sys
from pygame.locals import *
from colors import *

def parseLine(DISPLAY, y, s):
  x = 0
  for c in s:
    pygame.draw.line(DISPLAY, color[c], (x, y), (x, y))
    x += 1

def draw(*pictures):
  pygame.init()
  
  DISPLAY=pygame.display.set_mode((464, 464))
  DISPLAY.fill(BLUE)
  canvas = [DISPLAY]

  for picture in pictures:
    canva = pygame.Surface((640, 480), pygame.SRCALPHA)
    img = picture.img
    n = len(img)
    for i in range(0, n):
      parseLine(canva, i, img[i])
    canvas.append(canva)

  while True:
    for i in range(len(canvas)-1):
      canvas[i].blit(canvas[i+1], (0,0))

    for event in pygame.event.get():
      if event.type==QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.update()