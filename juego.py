import pygame
import random

ANCHO=1200
ALTO=900
NEGRO=[0,0,0]
VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
AMARILLO=[255,255,0]
BLANCO=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bola.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

class Rival(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60,60])
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx

if __name__ == '__main__':
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    #Grupos
    jugadores = pygame.sprite.Group()
    rivales = pygame.sprite.Group()

    j=Jugador([200,200])
    jugadores.add(j)

    n=10
    for i in range(n):
        x = random.randrange(0,(ANCHO-60))
        y = random.randrange(0,(ALTO-60))
        vx = random.randrange(2,10)
        r = Rival([x,y])
        r.velx = vx
        rivales.add(r)

    reloj = pygame.time.Clock()
    fin = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx = 5
                    j.vely = 0
                if event.key == pygame.K_LEFT:
                    j.velx = -5
                    j.vely = 0
                if event.key == pygame.K_UP:
                    j.velx = 0
                    j.vely = -5
                if event.key == pygame.K_DOWN:
                    j.velx = 0
                    j.vely = 5
            if event.type == pygame.KEYUP:
                j.velx = 0
                j.vely = 0
        #Refresco
        jugadores.update()
        ventana.fill(NEGRO)
        jugadores.draw(ventana)
        rivales.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)
