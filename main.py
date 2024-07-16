import pygame
import sys
from pygame import *
from setting import *

pygame.init()
frame = pygame.display.set_mode(frame_Size)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    frame.fill(frame_BgColor)
    pygame.display.update()
