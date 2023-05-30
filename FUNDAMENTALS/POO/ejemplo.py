class usuario:
    edad = 0
    curso = "Cuarto Medio B"
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0
    def print(self):
        print(f" el nombre de mi instancia {self.name}  y mi curso es el {self.curso}")
        return self
    def printEmail(self):
        print(f" el nombre de mi correo es {self.email} ")
        return self

usuario()
guido= usuario()
monty= usuario()
#acediendo a los metodos de la instancia
guido.print().printEmail()

#acediendo a los atrivutos de la instancia
print(guido.edad)        # salida: Micael
print(monty.curso)        # salida: Michael