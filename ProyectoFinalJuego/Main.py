'''Esta es la clase principal donde se crea el juego'''
import pygame
import sys
from Player import Player #Clase de jugador
from Screen import Screen #Clase de la pantalla
from Meteor import Meteor # Clase del meteoro

pygame.init()
#Crea la ventana, el jugador y a los meteritos 
ventana=screen()
ventana.init_title_icon()
scr=pygame.display.set_mode((ventana.width,ventana.heigh))
jugador=Player()
meteoro=Meteor()

class Utils:
    
    @classmethod
    def  detectar_colision(j,m):
        # Esta funcione es la que dectecta las coliciones entre la nave y el meteorito
        jx=j.pos[0]
        jy=j.pos[1]
        for i in range(len(m.meteorImg)):
            choque_posicion_meteorito_x = m.posx[i]>=jxand m.posx[i]<(jx+j.tam)
            choque_posicion_jugador_x = jx>=m.posx[i] and jx <(m.posx[i]+m.tam)
            choque_posicion_meteorito_y = m.posy[i] >= jy and m.posy[i]< (jy + j.tam)
            choque_posicion_jugador_y = jy >= m.posy[i] and jy < (m.posy[i] + m.tam)
                
            if choque_posicion_meteorito_x orchoque_posicion_jugador_x :
                if  choque_posicion_meteorito_y or choque_posicion_jugador_y:
                    return True
        return False


game_over=False
# El ciclo donde el juego inicializa 
while not game_over:
    ventana.update_background(scr)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
     # funciones de las clases para el movimieto del jugador o del meteorito
    jugador.move_player(ventana.width,ventana.heigh)
    meteoro.move_meteor(ventana.width,ventana.heigh)
    # actualizacion de los meteoros y jugador 
    meteoro.meteor_update(scr)
    jugador.player_update(scr)
    #detecta la colicion y acaba el juego 
    if Utils.detectar_colision(jugador,meteoro):
        game_over=True
    pygame.display.update()
