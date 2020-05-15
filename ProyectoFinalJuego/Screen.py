import pygame

class Screen:
    def __init__(self):
        #Creacion del tamaño, Titulo, Icono y el fondo de patalla para el juego 
        self.width =800
        self.heigh=600
        self.title='Lluvia de todo un poco'
        self.icon=pygame.image.load('img/iconspace.png')
        self.background=pygame.image.load('img/Background.jpg')
    #Esta funcion carga el titulo e Icono de la pantalla
    def init_title_icon(self):
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon)
     #Actualizacion de la pantalla 
    def update_background(self,ventana):
        ventana.blit(self.background,(0,0))
