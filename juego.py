import pygame
import random

ANCHO = 800
ALTO = 600
NEGRO = 0,0,0
VERDE = 0,255,0
ROJO = 255,0,0
AZUL = 0,0,255
AMARILO = 255,255,0
BLANCO = 255,255,255

class Jugador (pygame.sprite.Sprite):
    def __init__ (self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 50
        self.m = m
        #Direccion hacia abajo
        self.dir = 0
        self.con = 0
        self.image = self.m[self.dir][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        #efecto de movimiento
        if self.velx != self.vely:
            if self.con < 2:
                self.con += 1
            else:
                self.con = 0

            self.image = self.m[self.dir][self.con]


class Generador (pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([100,100])
        #self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.temp = random.randrange(100)

    def update(self):
        self.temp -= 1

class Raton (pygame.sprite.Sprite):
    def __init__ (self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 50
        self.id = 0
        self.m = m
        self.dir = 0
        self.con = 9
        self.image = self.m[self.dir][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        if self.con < 11:
            self.con += 1
        else:
            self.con = 9
        self.image = self.m[self.dir][self.con]
        self.rect.x += self.velx
        self.rect.y += self.vely

class Linea (pygame.sprite.Sprite):
    def __init__ (self,pos,dims):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(dims)
        #self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = 0

    def info_dir(self):
        #direccion abajo
        vx = 0
        vy = 0
        if self.dir == 0:
            vx = 0
            vy = 5
        if self.dir == 1:
            vx = -5
            vy = 0
        if self.dir == 2:
            vx = 5
            vy = 0
        if self.dir == 3:
            vx = 0
            vy = -5
        return [vx,vy]


if __name__ == '__main__':
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    jugadores = pygame.sprite.Group()
    generadores = pygame.sprite.Group()
    ratones = pygame.sprite.Group()
    lineas = pygame.sprite.Group()

    im_animales = pygame.image.load("animales.png")
    #Recorte de sabana
    m = []
    for j in range(8):
        fila = []
        for c in range(12):
            cuadro = im_animales.subsurface(32*c,32*j,32,32)
            fila.append(cuadro)
        m.append(fila)

    j = Jugador([100,100],m)
    jugadores.add(j)

    g= Generador([300,300])
    generadores.add(g)

    l = Linea([200,100],[300,5])
    l.dir = 2
    lineas.add(l)

    l2 = Linea([700,300],[5,300])
    l2.dir = 0
    lineas.add(l2)

    l3 = Linea([300,500],[400,5])
    l3.dir = 1
    lineas.add(l3)

    nro = 1
    fin = False
    reloj = pygame.time.Clock()

    while not fin:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx = 5
                    j.vely = 0
                    j.dir = 2
                if event.key == pygame.K_LEFT:
                    j.velx = -5
                    j.vely = 0
                    j.dir = 1
                if event.key == pygame.K_UP:
                    j.velx = 0
                    j.vely = -5
                    j.dir = 3
                if event.key == pygame.K_DOWN:
                    j.velx = 0
                    j.vely = 5
                    j.dir = 0
            if event.type == pygame.KEYUP:
                j.velx = 0
                j.vely = 0

        #Control creacion de ratones
        for g in generadores:
            if g.temp < 0:
                direccion = random.randrange(500)
                r = Raton(g.rect.center,m)
                r.id = nro
                nro += 1
                if direccion < 125:
                    r.velx = 5
                    r.dir = 2
                elif direccion < 250:
                    r.velx = -5
                    r.dir = 1
                elif direccion < 375:
                    r.vely = 5
                    r.dir = 0
                elif direccion < 500:
                    r.vely = -5
                    r.dir = 3
                ratones.add(r)
                g.temp = random.randrange(100)

        for r in ratones:
            if pygame.sprite.collide_circle(r,j):
                print ("cerca", r.id)
            ls_cl = pygame.sprite.spritecollide(r,lineas,False)
            for l in ls_cl:
                r.velx,r.vely = l.info_dir()
                r.dir = l.dir
            if r.rect.x < -50:
                ratones.remove(r)
            if r.rect.y < -50:
                ratones.remove(r)
            if r.rect.x > ANCHO:
                ratones.remove(r)
            if r.rect.y > ALTO:
                ratones.remove(r)

        jugadores.update()
        generadores.update()
        ratones.update()
        ventana.fill(NEGRO)
        #mostrar en pantalla el sprite
        generadores.draw(ventana)
        jugadores.draw(ventana)
        ratones.draw(ventana)
        lineas.draw(ventana)
        pygame.display.flip()


        reloj.tick(10)
