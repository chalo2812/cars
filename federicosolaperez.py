from itertools import cycle
import random
import sys
import pygame

from pygame.locals import *

FPS = 30
SCREENWIDTH  = 846#282 * 3
SCREENHEIGHT = 358#179 * 2 
# amount by which base can maximum shift to left
PIPEGAPSIZE  = 100 # gap between upper and lower part of pipe
#BASEY        = SCREENHEIGHT * 0.79
# image, sound and hitmask  dicts
IMAGES, SOUNDS, HITMASKS = {}, {}, {}
BACKGROUNDS = ('naipe_doble.jpg')
BACKGROUNDS_LIST = (

)

def main():
    global SCREEN, FPSCLOCK
    FPSCLOCK = pygame.time.Clock()
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Federico Sola Perez')
    IMAGES['background'] = pygame.image.load(BACKGROUNDS).convert()
    posx = 0;
    #pygame.mixer.music.load('tumblr_m9v2ujdS2q1r5dxz2o1.mp3');
    posy = 0;
    SCREEN.blit(IMAGES['background'], (0,0));
    #pygame.mixer.music.play(1, 0);
    while True:
        for event in pygame.event.get():

            if event.type == KEYDOWN: 

                if event.key == K_ESCAPE:
                    pygame.quit();
                    sys.exit();
                if event.type == QUIT:

                    pygame.quit();
                    sys.exit();
        pygame.display.flip()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
