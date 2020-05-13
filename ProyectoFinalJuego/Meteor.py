import  pygame
import random
class Meteor:
    def __init__(self):
        self.meteorImg=[pygame.image.load('img/alien.png'),
                        pygame.image.load('img/animals.png'),
                        pygame.image.load('img/animals1.png'),
                        pygame.image.load('img/education.png'),
                        pygame.image.load('img/food.png'),
                        pygame.image.load('img/game.png'),
                        pygame.image.load('img/nature.png'),
                        pygame.image.load('img/nature1.png'),
                        pygame.image.load('img/pet.png'),
                        pygame.image.load('img/starwars.png')]
        self.posx=[]
        self.posy=[]
        self.vel = []
        self.tam=30

        for i in range(len(self.meteorImg)):
            self.posx.append(random.randint(0,800))
            self.posy.append(random.randint(0,200))
            self.vel.append(random.randint(2,50))
    def move_meteor(self,ancho,alto):
        for i in range(len(self.meteorImg)):
            if self.posy[i] >= 0 and self.posy[i] < alto:
                self.posy[i] += (self.vel[i]/10)
            else:
                self.posx[i] = random.randint(0, ancho -self.tam)
                self.posy[i] = 0

    def meteor_update(self,ventana):
        for i in range(len(self.meteorImg)):
            ventana.blit(self.meteorImg[i],(self.posx[i], self.posy[i]))