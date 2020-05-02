class Ave:
    def __init__(self, tipo, color, genero, lugar, salud):
        self.tipo = tipo  # tipo de ave 
        self.color = color  # color 
        self.genero=genero # si es macho o hembre 
        self.lugar= lugar # de donde es el ave
        self.salud=salud #para ver si esta enfermo 
    def __str__(self):
        return ("\033[1;36m"+
              'Tipo: {}\n'
              'Color: {}\n'
              'Genero: {}\n'
              'Lugar: {}\n'
              'Salud: {}\n'
              .format(self.tipo,self.color,self.genero,self.lugar,self.salud))
    def IrVeterrinario(self):
        if self.salud=='mala'or self.salud=='Mala':
            print('\033[;31m Debe ir al veterinario')
        else:
            print('\033[;31m No es necesario ir al veterinario')
print('\033[;32m_________________ Clase AVES____________________')
ave1=Ave('picaflor',['azul','verde','negro'],'hembra','America','buena')
print(ave1)
ave1.IrVeterrinario()
