import pygame
class screen:
    def __init__(self):
        self.width =800
        self.heigh=600
        self.title='Lluvia de todo un poco'
        self.icon=pygame.image.load('img/iconspace.png')
        self.background=pygame.image.load('img/Background.jpg')

    def init_TitleIcon(self):
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon)
    def update_Background(self,ventana):
        ventana.blit(self.background,(0,0))