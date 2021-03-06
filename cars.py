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
    'imagenesCars/hippy.jpg',
    'imagenesCars/luigi.jpg',
    'imagenesCars/ramon.jpg',
    'imagenesCars/sargento.jpg',
    'imagenesCars/Doc.jpg',
    'imagenesCars/sheriff.jpg',
)

def main():
    global SCREEN, FPSCLOCK
    FPSCLOCK = pygame.time.Clock()
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Cars')
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
                if event.key == K_r:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/rayo.jpg').convert()                
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_d:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/derby1.jpg').convert()                
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_w:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/Wingo.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_o:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/Miss_Fritter.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_s:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/sally.jpg').convert()                
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_1:
                    posx=0; posy=0
                    #IMAGES['background'] = pygame.image.load('imagenesCars/red.jpg').convert()
                    IMAGES['background'] = pygame.image.load('imagenesPacman/Pac_Man.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_2:
                    posx=0; posy=0
                    #IMAGES['background'] = pygame.image.load('imagenesCars/Jackson_Storm.jpg').convert()
                    IMAGES['background'] = pygame.image.load('imagenesPacman/Pacman 240.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_f:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/franchesco.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_t:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/mate.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_m:
                    posx=0; posy=0
                    #IMAGES['background'] = pygame.image.load('imagenesCars/mate.jpg').convert()
                    IMAGES['background'] = pygame.image.load('imagenesMario/mario.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_c:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/cruz.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_j:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/Wario.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_n:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/Yoshi.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_b:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/interrogacionjj.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_y:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesMario/shroom.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_z:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/rayo lodo.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_x:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesPacman/bola.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))                
                if event.key == K_0:
                    posx=0; posy=0
                  	#IMAGES['background'] = pygame.image.load('imagenesCars/cruz lodo.jpg').convert()
                    IMAGES['background'] = pygame.image.load('imagenesPacman/pink.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_3:
                    posx=0; posy=0
                    #IMAGES['background'] = pygame.image.load('imagenesCars/dj.jpg').convert()
                    IMAGES['background'] = pygame.image.load('imagenesPacman/blinky.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_4:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/ambulancia.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_5:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/cruz 95.jpg').convert()
                    SCREEN.blit(IMAGES['background'],(0,0))
                if event.key == K_e:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/boost.jpg').convert()
                    SCREEN.blit(IMAGES['background'],(0,0))
                if event.key == K_a:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/apb.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_8:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/Chick.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_q:
                    posx=0; posy=0;
                    IMAGES['background'] = pygame.image.load('imagenesCars/cruz final.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_k:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/mack.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_g:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/guido.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))         
                if event.key == K_h:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/Holley_Shiftwell.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))      
                if event.key == K_6:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/doc final.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))       
                if event.key == K_7:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/Doc.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_9:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesCars/Snot_rod_side.jpg').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_v:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesPacman/Clyde.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_p:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesPacman/inky.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_i:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesPacman/fantas.png').convert()
                    SCREEN.blit(IMAGES['background'], (0,0))
                if event.key == K_u:
                    posx=0; posy=0
                    IMAGES['background'] = pygame.image.load('imagenesPacman/pacman izq.jpg').convert()
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
