# CodigosJuego
Codigos de compu grafica

CONTENIDO DE CADA RAMA:

a1_imagenjp: Implementacion de un jugador (se carga una imagen) y bloques (rivales). Los bloques son estáticos solo se mueve el jugador.

a2_colision: Se maneja lo mismo que en la rama a1_imagenjp, pero en esta rama del juego, el jugador al hacer colision con un enemigo lo elimina.

a3_interactivo: El jugador aparece en la parte inferior, se mueve en x y dispara al dar click. Los rivales se mueven en la parte superior de la ventana, colisonan con los bordes de la ventana en un efecto rebote, estos tambien disparan en tiempos aleatorios hacia abajo. Cuando el rival o el jugador reciben el golpe de la bala, son eliminados por la colision.

a4_finjuego: Se maneja lo mismo que en la rama a3_interactivo, pero en esta rama se implementa la pantalla de fin de juego. Al jugador ser eliminado por un rival, termina el juego y aparece en pantalla "fin del juego".

b1_rivales: Se maneja lo mismo que en la rama a1_imagenjp. Aqui el jugador es un cubo (surface).

b2_colision: El jugador en la parte de abajo, se mueve en x, puede disparar hacia arriba con click. Los rivales en la parte superior de la ventana, se mueven hacia la derecha y desaparecen en el borde de la ventana. Se hace control de memoria con las balas.

b3_disparos: Se maneja lo mismo que en la rama a3_interactivo. Se implementa la pantalla de fin de juego al jugador ser eliminado por una bala de un rival.

c3_completo: Se maneja lo mismo que en la rama a3_interactivo. Se implementa pantalla de inicio con un fondo, texto y musica. Juego principal con efecto de sonido en disparos y destruccion de enemigo, conteo de vidas que se muestran en la ventana. Fin de juego.

d3_entornos: Se carga imagen de fondo y un jugador, el jugador se puede mover por el mapa y seguir recorriendo lo que no se ve del mapa, al llegar a un "limite" a la derecha, el mapa se comienza a mover a la vez que se mueve el jugador. Se tiene en cuenta el limite de tamaño del fondo cargado para que este se muestre hasta ahi. Se maneja tambien un bloque que parece "pegado" al fondo, ya que este se mueve a la par con el fondo.

d4_bloquesAmbiente: Se maneja la colision entre el jugador y los bloques, para que el jugador no pueda atravesar el bloque por ningun lado.

a1_ken: Se implementa sprite de ken, cambia de accion segun la tecla. Tiene implementada la accion del puño con la letra 'c'.

a2_ken: Se maneja lo mismo que en la rama a1_ken. Pero en esta se implementa un bloque, cuando el Ken hace colision en la accion de puño, el bloque se mueve.

gestion_img: Se implementa el recorte de sabanas con una de terrenos como ejemplo.

gestion_sp: Se implementa el sprite de los animales, se usa el gato con efecto de movimiento para las cuatro direcciones.

generador:  Se implementa el concepto de generador. Se crea un bloque que funciona como generador y cada cierto tiempo salen de este ratones que se mueven en alguna de las cuatro direcciones. Se crean lineas que modifican el comportamiento de estos ratones, al hacer colision, cambian su direccion y velocidad. Por ultimo se implementa collide_circle, con esta, cada uno de los ratones puede detectar cuando el gato está cerca, de alli se puede modificar su comportamiento.

plataforma: Se implementan dos plataformas y un jugador, se tiene en cuenta la colision con estas y se agrega en factor gravedad. El jugador puede saltar y vuelve a caer por efecto de gravedad y tambien pasar entre plataformas saltando

mapeo: Carga de mapa por medio de la libreria configparser (la deben instalar) y se muestra graficamente con pygame. Se puede crear el mapa con caracteres y a cada uno de estos asignarle un sprite. Para luego mostrar por medio de una matriz en ventana.








