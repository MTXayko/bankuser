class CuentaBancaria:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        CuentaBancaria.accounts.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $ 5")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        return f"{self.balance}"

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def imprimir_todas_cuentas(cls):
        for account in cls.accounts:
            account.mostrar_info_cuenta()

class Usuario:

    def __init__(self, name):
        self.name = name
        self.account = {
            "comprobacion" : CuentaBancaria(0.02,1000),
            "ahorros" : CuentaBancaria(.05,3000)
        }
        

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, comprobacion Balance: {self.account['comprobacion'].mostrar_info_cuenta()}")
        print(f"Usuario: {self.name}, Ahorros Balance: {self.account['ahorros'].mostrar_info_cuenta()}")
        return self

    def transferir_dinero(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.mostrar_balance_usuario
        user.mostrar_balance_usuario()
        return self


Matias = Usuario("Matias")

Matias.account['comprobacion'].deposito(400)
Matias.mostrar_balance_usuario()