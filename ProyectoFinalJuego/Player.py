import  pygame
class Player:
    def __init__(self):
        #Creacion de la nave o jugador con una imagen
        self.playerImg=pygame.image.load('img/nave.png')
        #Tamaño para la deteccion de colicion
        self.tam=32
        #Posicion en donde iniciara la nave
        self.pos=[370,540]
        #Velocidad a la ira la nave 
        self.vel=2
     #Movimieto de la nave en la pantalla
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
    #Actualizacion de la nave en la Pantalla
    def player_update(self,screem):
        screem.blit(self.playerImg,(self.pos[0],self.pos[1]))
