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
    'imagenesCars/dinaco.jpg',
    'imagenesCars/fly.jpg',
    'imagenesCars/franchesco.jpg',
    'imagenesCars/hippy.jpg',
    'imagenesCars/luigi.jpg',
    #'imagenesCars/mate.jpg',
    'imagenesCars/ramon.jpg',
    #'imagenesCars/rayo.jpg',
    #'imagenesCars/red.jpg',
    #'imagenesCars/sally.jpg',
    'imagenesCars/sargento.jpg',
    #'imagenesCars/apb.jpg',
    
    'imagenesCars/Doc.jpg',
    #'imagenesCars/Chick.jpg',
    'imagenesCars/sheriff.jpg',
    #'imagenesCars/cruz lodo.jpg'
    #'imagenesCars/cruz.jpg',
    #'imagenesCars/Jackson_Storm.jpg'
)

def main():
    global SCREEN, FPSCLOCK
    FPSCLOCK = pygame.time.Clock()
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Cars')
    pygame.mixer.music.load('estrellita.mp3')
    IMAGES['background'] = pygame.image.load(BACKGROUNDS).convert()
    posx = 0
    posy = 0
    SCREEN.blit(IMAGES['background'], (0,0)) 
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
                if event.key == K_r:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/rayo.jpg').convert()                
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_w:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/Miss_Fritter.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_s:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/sally.jpg').convert()                
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_1:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/red.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_2:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/Jackson_Storm.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_m:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/mate.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_c:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/cruz.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_z:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/rayo lodo.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_0:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/cruz lodo.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_a:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/apb.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_8:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/Chick.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_k:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/mack.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_g:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/guido.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))         
                if event.key == K_RIGHT:
                    if posx < 846:
                        posx=posx + 50
                    SCREEN.blit(IMAGES['background'], (posx,posy))
                if event.key == K_LEFT:
                    if posx > 0:
                        posx=posx - 50
                    SCREEN.blit(IMAGES['background'], (posx,posy))
                if event.key == K_DOWN:
                    if posy < 358:
                        posy=posy + 50     
                    SCREEN.blit(IMAGES['background'], (posx,posy))
                if event.key == K_UP:
                    if posy > 0:
                        posy=posy - 50
                    SCREEN.blit(IMAGES['background'], (posx,posy))  
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()