import pygame
import random

ANCHO=1200
ALTO=500
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
        #self.rect.y += self.vely

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
        self.tmp = random.randrange(40,100)

    def RetPos(self):
        x = self.rect.x + 20
        y = self.rect.bottom
        return [x,y]

    def update(self):
        self.tmp -= 1
        if self.rect.x > (ANCHO - self.rect.width):
            self.rect.x = ANCHO - self.rect.width
            self.velx = -5
        if self.rect.x < 0:
            self.rect.x = 0
            self.velx = 5
        self.rect.x += self.velx

class Bala(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vely = 0

    def update(self):
        self.rect.y += self.vely

if __name__ == '__main__':
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    #Grupos
    jugadores = pygame.sprite.Group()
    rivales = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    balas_r = pygame.sprite.Group()

    j=Jugador([200,200])
    jugadores.add(j)

    n=10
    for i in range(n):
        x = random.randrange(0,(ANCHO-60))
        y = random.randrange(0,(ALTO-100))
        vx = random.randrange(2,10)
        r = Rival([x,y])
        r.velx = vx
        rivales.add(r)

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = j.RetPos()
                b = Bala(pos)
                b.vely = -10
                balas.add(b)

        #Control
        ls_obj = pygame.sprite.spritecollide(j,rivales,True)

        for r in rivales:
            if r.tmp <= 0:
                pos = r.RetPos()
                b = Bala(pos)
                b.vely = 8
                balas_r.add(b)
                r.tmp = random.randrange(40,100)

        #Limpieza de memoria
        for b in balas:
            ls_r = pygame.sprite.spritecollide(b,rivales,True)
            if b.rect.y < -50:
                balas.remove(b)
            if r in ls_r:
                balas.remove(b)

        for b in balas_r:
            ls_j = pygame.sprite.spritecollide(b,jugadores,False)
            if b.rect.y > (ALTO + 100):
                balas_r.remove(b)
            for j in ls_j:
                j.vidas -= 1

        for j in jugadores:
            if j.vidas < 0:
                #jugadores.remove(j)
                #fin = True
                fin_juego = True


        #Refresco
        if not fin_juego:
            jugadores.update()
            rivales.update()
            balas.update()
            balas_r.update()
            ventana.fill(NEGRO)
            jugadores.draw(ventana)
            rivales.draw(ventana)
            balas.draw(ventana)
            balas_r.draw(ventana)
            pygame.display.flip()
            reloj.tick(40)
        else:
            pygame.font.init()
            fuente = pygame.font.Font(None, 32)
            msj = fuente.render("Fin de juego",True,BLANCO)
            ventana.fill (NEGRO)
            ventana.blit(msj,[200,200])
            pygame.display.flip()
