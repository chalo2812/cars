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
#BACKGROUNDS_LIST = (
#    'imagenesCars/dinaco.jpg',
#    'imagenesCars/fly.jpg',
#    'imagenesCars/hippy.jpg',
#    'imagenesCars/luigi.jpg',
#    'imagenesCars/ramon.jpg',
#    'imagenesCars/sargento.jpg',
#    'imagenesCars/Doc.jpg',
#    'imagenesCars/sheriff.jpg',
#);

def main():
    global SCREEN, FPSCLOCK
    FPSCLOCK = pygame.time.Clock()
    pygame.init();
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Mario')
    IMAGES['background'] = pygame.image.load(BACKGROUNDS).convert()
    posx = 0;
    posy = 0;
    SCREEN.blit(IMAGES['background'], (0,0));
    while True:
        for event in pygame.event.get():

            if event.type == KEYDOWN: 
                #if event.key == K_SPACE:
                #    posx=0; posy=0
                #    randBg = random.randint(0, len(BACKGROUNDS_LIST) - 1) 
                #    IMAGES['background'] = pygame.image.load(BACKGROUNDS_LIST[randBg]).convert() 
                #    SCREEN.blit(IMAGES['background'], (0,0)) 
                if event.key == K_RETURN:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load(BACKGROUNDS).convert()
                    SCREEN.blit(IMAGES['background'], (posx,posy)) 
                if event.key == K_h:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/honguito.jpeg').convert()                
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_q:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/Bowser.png').convert()                
                    SCREEN.blit(IMAGES['background'], (0,0))					
                if event.key == K_d:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/donkey kong.jpg').convert()                
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_f:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/fantasma.jpg').convert()                
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_a:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/princess.jpg').convert()                
                    SCREEN.blit(IMAGES['background'], (0,0))	
                if event.key == K_p:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/planta.jpg').convert()                
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_r:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/rojo.jpg').convert()                
                    SCREEN.blit(IMAGES['background'], (0,0))                
                if event.key == K_t:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/man honguito.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_m:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/mario.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_k:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/waluigi.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_w:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/Wario.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_y:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/Yoshi.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_i:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/interrogacion.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_s:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/shroom.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))               
                if event.key == K_l:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/luigi.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_c:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/planta2.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))					
                if event.key == K_z:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/tubo.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))	
                if event.key == K_x:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/Koopa.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))						
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
