class Basquetbolista:
    def __init__(self, nombre, edad, equipo, numero, posicion, estadoFisco):
        self.nombre=nombre  # Nombre del jugador 
        self.edad =edad  # Edad del jugador 
        self.equipo=equipo # Equipo que pertenece
        self.numero= numero # Numero de Polera
        self.posicion=posicion # En que posiscion juega en el basquet
        self.estadoFisico=estadoFisco # Evaluacion de su fisico 
    def __str__(self):#imprime al jugador 
        return ("\033[1;36m"+
              'Nombre: {}\n'
              'Edad: {}\n'
              'Equipo: {}\n'
              'Numero: {}\n'
              'Posicion: {}\n'
              'Estado Fisico: {}'
              .format(self.nombre,self.edad,self.equipo,self.numero,self.posicion,self.estadoFisico))
    def Evaluacion(self): # evaluacion del  estado fisico del jugador en un rango del 1 al 5
        if self.estadoFisico<3:
            print('''\033[1;33m Necesita mejorar la dieta aumentar el ejercico en el gym
            debe mejorar el estado fisico y la alimentacios''')
        elif self.estadoFisico==3:
            print('''\033[1;33m Mantener la dieta aumentar el ejercico en el gym
            forlecer el estado fisico''')
        else:
            print('''\033[1;33m No necesita cambios en su dieta 
            el estado fisico esta optimo ''')
    def cambiodeEquipo(self,nuevoEquipo,nuevoNuemero):# es el cambio del jugado a otro equipo
        self.equipo=nuevoEquipo
        self.numero=nuevoNuemero    
print('\033[;32m*************Clase Basquetbolista*********')
jugador=Basquetbolista(nombre=input('introdusca el nombre '),edad=int(input('introdusca la edad ')),equipo=input('introdusca el equipo '),numero=input('introdusca el numero '),posicion=input('introdusca posicio '),estadoFisco=int(input('introdusca el estado fisico rango [1-5] ')))
print(jugador)
jugador.Evaluacion()
op=input('\033[1;32m ¿Se desea cambiar de equipo S/N?')
if op == 'S' or op == 's':
    e=input('nuevo equipo ')
    nu=input('nuevo numero ')
jugador.cambiodeEquipo(e,nu)
print(jugador)