import  pygame
import random # importamos esta libreria random para crear las posiciones de los meteoros


class Meteor:
    def __init__(self):
        #Lista de las imagenes de los Meteoros 
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
       #Creacion de las listas para la posicion x e y. 
       #La velocidad sera igual una lista para que haya distitas velocidades 
        self.posx=[]
        self.posy=[]
        self.vel = []
        # El tamaño aydara en la deteccion de colicion
        self.tam=30
        #Creacion de las posiciones de los Meteoros alearoriamente 
        for i in range(len(self.meteorImg)):
            self.posx.append(random.randint(0,800))
            self.posy.append(random.randint(0,200))
            self.vel.append(random.randint(2,50))
    # Esta funcion define los movimientos que tendran los metoros con una sierta velocidad
    def move_meteor(self,ancho,alto):
        for i in range(len(self.meteorImg)):
            if self.posy[i] >= 0 and self.posy[i] < alto:
                self.posy[i] += (self.vel[i]/10)
            else:
                self.posx[i] = random.randint(0, ancho -self.tam)
                self.posy[i] = 0
    #Actualiza a los Meteoros en la pantalla
    def meteor_update(self,ventana):
        for i in range(len(self.meteorImg)):
            ventana.blit(self.meteorImg[i],(self.posx[i], self.posy[i]))
