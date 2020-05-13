import  pygame
class Player:
    def __init__(self):
        self.playerImg=pygame.image.load('img/nave.png')
        self.tam=32
        self.pos=[370,540]
        self.vel=2
    def move_player(self,ancho,height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.pos[0] > 0:
            self.pos[0] -= self.vel
        if keys[pygame.K_RIGHT] and self.pos[0] < ancho - self.tam:
            self.pos[0] += self.vel
        if keys[pygame.K_UP] and self.pos[1]>0:
            self.pos[1]-=self.vel
        if keys[pygame.K_DOWN] and self.pos[1] < 540:
            self.pos[1]+= self.vel

    def player_update(self,screem):
        screem.blit(self.playerImg,(self.pos[0],self.pos[1]))