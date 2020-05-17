import pygame
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



if __name__ == '__main__':
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    jugadores = pygame.sprite.Group()

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

        jugadores.update()
        ventana.fill(NEGRO)
        #mostrar en pantalla el sprite
        jugadores.draw(ventana)
        pygame.display.flip()


        reloj.tick(10)
