import pygame
import random

ANCHO=500
ALTO=300
NEGRO=[0,0,0]
VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
AMARILLO=[255,255,0]
BLANCO=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60,60])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = ALTO - self.rect.height
        self.velx = 0
        self.vely = 0
        self.vidas = 0

    def RetPos(self):
        x = self.rect.x
        y = self.rect.y
        return [x,y]

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

class Bloque(pygame.sprite.Sprite):
    def __init__ (self,pos, d_an, d_al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([d_an,d_al])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

if __name__ == '__main__':
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    #Grupos
    jugadores = pygame.sprite.Group()

    j=Jugador([200,200])
    jugadores.add(j)

    reloj = pygame.time.Clock()
    fin = False
    fin_juego = False

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


        #Control

        for j in jugadores:
            if j.vidas < 0:
                #jugadores.remove(j)
                #fin = True
                fin_juego = True


        #Refresco
        jugadores.update()
        ventana.fill(NEGRO)
        jugadores.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)
