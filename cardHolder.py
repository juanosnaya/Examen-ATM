class cardHolder():
    def __init__(self,cardNum, pin, nombre, apellido, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.nombre = nombre
        self.apellido = apellido
        self.balance = balance

    def get_cardNum(self):
        return self.cardNum
    def get_pin(self):
        return self.pin
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_balance(self):
        return self.balance
    
    def set_cardNum(self, newVal):
        self.cardNum = newVal
    def set_pin(self, newVal):
        self.pin = newVal
    def set_nombre(self, newVal):
        self.nombre = newVal
    def set_apellido(self, newVal):
        self.apellido = newVal
    def set_balance(self, newVal):
        self.balance = newVal

    def print_out(self):
        print("Tarjeta #:", self.cardNum)
        print("PIN:", self.pin)
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Saldo:", self.balance)