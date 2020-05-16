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
        self.image = pygame.Surface([40,40])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = ALTO - self.rect.height
        self.velx = 0
        self.vely = 0
        self.vidas = 0
        self.bloques = None

    def RetPos(self):
        x = self.rect.x
        y = self.rect.y
        return [x,y]

    def update(self):
        #Colision en x
        self.rect.x += self.velx
        ls_col = pygame.sprite.spritecollide (self,self.bloques,False)
        for b in ls_col:
            if (self.rect.right > b.rect.left) and (j.velx > 0):
                self.rect.right = b.rect.left
                self.velx = 0
                #j.velx=-5 hace efecto rebote
            if (self.rect.left < b.rect.right) and (j.velx < 0):
                self.rect.left = b.rect.right
                self.velx = 0

        #Colision en y
        self.rect.y += self.vely
        ls_col = pygame.sprite.spritecollide (self,self.bloques,False)
        for b in ls_col:
            if (self.rect.top < b.rect.bottom) and (j.vely < 0):
                self.rect.top = b.rect.bottom
                self.vely = 0

            if (self.rect.bottom > b.rect.top) and (j.vely > 0):
                self.rect.bottom = b.rect.top
                self.vely = 0


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
    bloques = pygame.sprite.Group()

    j=Jugador([200,200])
    jugadores.add(j)

    bl = Bloque([300,100],100,20)
    bloques.add(bl)
    bl2 = Bloque([100,150],30,60)
    bloques.add(bl2)

    j.bloques = bloques

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

        for j in jugadores:
            if j.vidas < 0:
                #jugadores.remove(j)
                #fin = True
                fin_juego = True


        #Refresco
        jugadores.update()
        ventana.fill(NEGRO)
        jugadores.draw(ventana)
        bloques.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)
