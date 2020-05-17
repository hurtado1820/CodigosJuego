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
        self.accion = 1
        self.con = 0
        self.lim = [3,3,2,4,1,3,4,4,6,0]
        self.image = self.m[self.accion][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        #efecto de movimiento
        if self.con < self.lim[self.accion]:
            self.con += 1
        else:
            self.con = 0
            self.accion = 1
        self.image = self.m[self.accion][self.con]



if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    jugadores = pygame.sprite.Group()

    im_animales = pygame.image.load("ken.png")
    #Recorte de sabana
    m = []
    for j in range(10):
        fila = []
        for c in range(7):
            cuadro = im_animales.subsurface(70*c,80*j,70,80)
            fila.append(cuadro)
        m.append(fila)

    j = Jugador([100,100],m)
    jugadores.add(j)
    fin = False
    reloj = pygame.time.Clock()
    cad = []

    while not fin:
        #Gestion de eventos
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
                if event.key == pygame.K_c:
                    j.accion = 2
                    j.con = 0
                    cad += 'c'
                if event.key == pygame.K_z:
                    cad += 'z'
                if event.key == pygame.K_x:
                    cad += 'x'
            if event.type == pygame.KEYUP:
                j.velx = 0
                j.vely = 0

        if len(cad) <= 3:
            print (cad)
            if cad == 'zxc':
                print ("hado ken")
        else:
            cad = ''
        jugadores.update()
        ventana.fill(NEGRO)
        #mostrar en pantalla el sprite
        jugadores.draw(ventana)
        pygame.display.flip()


        reloj.tick(10)
