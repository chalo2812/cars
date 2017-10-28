from itertools import cycle
import random
import sys
import pygame

from pygame.locals import *

FPS = 30
SCREENWIDTH  = 553
SCREENHEIGHT = 531
# amount by which base can maximum shift to left
PIPEGAPSIZE  = 100 # gap between upper and lower part of pipe
#BASEY        = SCREENHEIGHT * 0.79
# image, sound and hitmask  dicts
IMAGES, SOUNDS, HITMASKS = {}, {}, {}
BACKGROUNDS = ('fondo-pacman.jpg')
BACKGROUNDS_LIST = (

)

class MiSprite ( pygame.sprite.Sprite ):
    '''Todos los objetos que se representan en pantalla son sprites'''
    def __init__(self, fichero_imagen, pos_inicial, velocidad):
        pygame.sprite.Sprite.__init__(self) 
        
        #Un sprite debe tener definida las propiedades "image" y "rect"
        #    Image representa la imagen a visualizar. Es de tipo "surface".
        #    Rect es un rectangulo que representa la zona de la pantalla que ocupara la imagen
        self.image = pygame.image.load(fichero_imagen).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos_inicial
        self.velocidad = velocidad
    
    def update (self):
        #Esta funcion es llamada repetidamente para hacer cualquier cambio
        #   en el sprite. Por ejemplo, para cambiar su posicion
        
        #la funcion move_ip desplaza el rectangulo que ocupa el sprite
        self.rect.move_ip ( self.velocidad[0], self.velocidad[1]) 

def main():
    global SCREEN, FPSCLOCK
    FPSCLOCK = pygame.time.Clock()
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Federico Sola Perez')
    IMAGES['background'] = pygame.image.load(BACKGROUNDS).convert()
    posx = 0;
    posy = 0;
    SCREEN.blit(IMAGES['background'], (0,0))
    #pygame.mixer.music.play(1, 0);
    sprites = pygame.sprite.RenderUpdates();
    #sprite1 = MiSprite("imagenesPacman/pacman.png", [220,390], [50,0]);
    sprite1 = MiSprite("imagenesPacman/pacman.png", [220,390], [2,0]);
    sprites.add ( sprite1 );
    sprite2 = MiSprite("imagenesPacman/fantasma.gif",[100,0], [0, 50] )
    sprites.add ( sprite2 );
    while True:
        screen = pygame.display.get_surface (); 
        sprites.update()
        sprites.clear (screen, SCREEN) 
        pygame.display.update (sprites.draw (screen))
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
	pygame.display.flip()

if __name__ == '__main__':
    main()
