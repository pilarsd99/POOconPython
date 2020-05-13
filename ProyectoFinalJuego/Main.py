import pygame
import sys
from Player import Player
from Screen import screen
from Meteor import Meteor
pygame.init()
ventana=screen()
ventana.init_TitleIcon()
scr=pygame.display.set_mode((ventana.width,ventana.heigh))
jugador=Player()
meteoro=Meteor()

def  detectar_colision(j,m):
    jx=j.pos[0]
    jy=j.pos[1]
    for i in range(len(m.meteorImg)):
        if (m.posx[i]>=jx and m.posx[i]<(jx+j.tam)) or (jx>=m.posx[i] and jx <(m.posx[i]+m.tam)):
            if (m.posy[i] >= jy and m.posy[i]< (jy + j.tam)) or (jy >= m.posy[i] and jy < (m.posy[i] + m.tam)):
                return True
    return False


game_over=False
while not game_over:
    ventana.update_Background(scr)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    jugador.move_player(ventana.width,ventana.heigh)
    meteoro.move_meteor(ventana.width,ventana.heigh)
    meteoro.meteor_update(scr)
    jugador.player_update(scr)
    if detectar_colision(jugador,meteoro):
        game_over=True
    pygame.display.update()