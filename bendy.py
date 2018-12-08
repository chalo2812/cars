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
    'imagenesBendy/Alice Angel.png',
    'imagenesBendy/Bendy.jpg',
    'imagenesBendy/Bendy ani.gif',
    'imagenesBendy/Tinta.jpg'
)

def main():
    global SCREEN, FPSCLOCK
    FPSCLOCK = pygame.time.Clock()
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Bendy')
    IMAGES['background'] = pygame.image.load(BACKGROUNDS).convert()
    posx = 0;
    #pygame.mixer.music.load('tumblr_m9v2ujdS2q1r5dxz2o1.mp3');
    posy = 0;
    SCREEN.blit(IMAGES['background'], (0,0));
    #pygame.mixer.music.play(1, 0);
    while True:
        for event in pygame.event.get():

            if event.type == KEYDOWN: 
                if event.key == K_SPACE:
                    posx=0; posy=0
                    randBg = random.randint(0, len(BACKGROUNDS_LIST) - 1) 
                    IMAGES['background'] = pygame.image.load(BACKGROUNDS_LIST[randBg]).convert() 
                    SCREEN.blit(IMAGES['background'], (0,0)) 
                if event.key == K_RETURN:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load(BACKGROUNDS).convert()
                    SCREEN.blit(IMAGES['background'], (posx,posy)) 
                if event.key == K_RIGHT:
                    if posx < 846:
                        posx = posx + 20
                    SCREEN.blit(IMAGES['background'], (posx,posy))
                if event.key == K_LEFT:
                    if posx > 0:
                        posx = posx - 20
                    SCREEN.blit(IMAGES['background'], (posx,posy))
                if event.key == K_DOWN:
                    if posy < 358:
                        posy = posy + 30
                    SCREEN.blit(IMAGES['background'], (posx,posy))
                if event.key == K_UP:
                    if posy > 0:
                        posy=posy - 30
                    SCREEN.blit(IMAGES['background'], (posx,posy))
                if event.key == K_ESCAPE:
                    #pygame.mixer.music.stop();
                    pygame.quit();
                    sys.exit();
                if event.type == QUIT:
                    #pygame.mixer.music.stop();
                    pygame.quit();
                    sys.exit();
        pygame.display.flip()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
