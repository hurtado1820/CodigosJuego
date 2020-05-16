import pygame
ANCHO = 1200
ALTO = 900
NEGRO = 0,0,0
VERDE = 0,255,0
ROJO = 255,0,0
AZUL = 0,0,255
AMARILO = 255,255,0
BLANCO = 255,255,255

if __name__ == '__main__':
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    fondo = pygame.image.load ("terrenogen.png")
    pos_x = 32*6
    #Recorte, posicion x,y, alto,ancho
    cuadro = fondo.subsurface(pos_x,0,32,32)

    fin = False

    while not fin:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        ventana.blit (cuadro,[0,0])
        pygame.display.flip()
