from itertools import cycle
import random
import sys
import pygame


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

if __name__ == "__main__":    
    pygame.init()
    IMAGES, SOUNDS, HITMASKS = {}, {}, {}
    #BACKGROUNDS = ('fondo.png')
   # IMAGES['background'] = pygame.image.load(BACKGROUNDS).convert()
    #Indicamos la dimension de la pantlla de juego
    window = pygame.display.set_mode([1024,688])
    pygame.display.set_caption("Pacman")  
    #Inicializamos la pantalla con fondo negro
    screen = pygame.display.get_surface()
    #screen.blit(BACKGROUNDS, (0,0)) 
    
    screen.fill ([0,0,0])
    #creamos una copia de la pantalla para evitar su repintado completo cuando
    #    se redibujen los sprites
    background = screen.copy()
    #creamos los sprites
    sprites = pygame.sprite.RenderUpdates()
    sprite1 = MiSprite("imagenesPacman/pacman.gif", [0,0], [0,1])
    sprites.add ( sprite1 )
    sprite2 = MiSprite("imagenesPacman/fantasma.gif",[100,0], [0, 1] )
    sprites.add ( sprite2 )
    #sprite3 = MiSprite ("imagenesPacman/fruta.gif", [0, 100], [0,0])
    #sprites.add ( sprite3 )
    #sprite4 = MiSprite ("imagenesPacman/bola.gif", [100, 100], [0,0] )
    #sprites.add(sprite4)

    #bucle de redibujado de los screens
    reloj = pygame.time.Clock() 
    #SCREEN.blit(IMAGES['background'], (0,0)) 
    while True: 
        screen = pygame.display.get_surface () 
        sprites.update ()
        sprites.clear (screen, background) 
        pygame.display.update (sprites.draw (screen))
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_DOWN:
                    sprite1.update()
    pygame.display.flip()
        