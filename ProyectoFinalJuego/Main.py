'''Esta es la clase principal donde se crea el juego'''
import pygame
import sys
from Player import Player #Clase de jugador
from Screen import screen #Clase de la pantalla
from Meteor import Meteor # Clase del meteoro

pygame.init()
#Crea la ventana, el jugador y a los meteritos 
ventana=screen()
ventana.init_TitleIcon()
scr=pygame.display.set_mode((ventana.width,ventana.heigh))
jugador=Player()
meteoro=Meteor()

def  detectar_colision(j,m):
    # Esta funcione es la que dectecta las coliciones entre la nave y el meteorito
    jx=j.pos[0]
    jy=j.pos[1]
    for i in range(len(m.meteorImg)):
        if (m.posx[i]>=jx and m.posx[i]<(jx+j.tam)) or (jx>=m.posx[i] and jx <(m.posx[i]+m.tam)):
            if (m.posy[i] >= jy and m.posy[i]< (jy + j.tam)) or (jy >= m.posy[i] and jy < (m.posy[i] + m.tam)):
                return True
    return False


game_over=False
# El ciclo donde el juego inicializa 
while not game_over:
    ventana.update_Background(scr)
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
    if detectar_colision(jugador,meteoro):
        game_over=True
    pygame.display.update()
