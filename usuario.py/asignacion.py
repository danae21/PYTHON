class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0

    def hacer_deposito(self, monto):
        self.monto += monto
    
    def sacar_plata(self,monto):
        self.monto -=monto

    def mostrar_info(self):
        print(f"{self.nombre} tiene ${self.monto}")
    
    def transferir_dinero(self, monto,otro_usuario):
        self.monto -= monto
        otro_usuario.monto += monto
        self.mostrar_info()
        otro_usuario.mostrar_info()
    



carla=Usuario("Carla")
danae=Usuario("Danae")
carla.hacer_deposito(1000)

carla.transferir_dinero(200,danae)

danae.hacer_deposito(1000)
danae.mostrar_info()