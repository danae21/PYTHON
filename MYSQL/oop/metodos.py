class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0
        

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawl(self,amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


danae = User("danae")
carla = User("carla")
ignacio = User("ignacio")

danae.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawl(45).display_user_balance()

carla.make_deposit(1000).make_deposit(1000).make_withdrawl(500).make_withdrawl(300).display_user_balance()

ignacio.make_deposit(1500).make_withdrawl(1000).make_withdrawl(5000).make_withdrawl(3000).display_user_balance()


ignacio.transfer_money(400, danae)   
    #Codigo