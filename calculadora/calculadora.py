print("********************************s****** ")
print("******Sistema Gestión de Usuarios****** ")
print("********************************s****** ")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")

option = input("Elige una opción: ")


class operaciones:
    resultados =[]
    def __init__(self, num1, num2):
        self.num1= num1
        self.num2= num2
    def suma(self):
        resultado = self.num1+self.num2
        mostrar_resultado = print(f"El resultado es: {resultado}")
        return mostrar_resultado
    def resta(self):
        return self.num1-self.num2
    

num1= int(input("Ingresa numero 1: "))
num2= int(input("Ingresa numero 2: "))

calculadora = operaciones(num1,num2)



if option == "1":
    calculadora.suma()

if option == "2":
    calculadora.resta()

if option == "3":
    calculadora.multiplicar()

if option == "4":
    calculadora.dividir()
