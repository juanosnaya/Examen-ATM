from cardHolder import cardHolder
#Menú del ATM
def print_menu():

    print("Por favor seleccione una opción:")
    print ("1.Abono a cuenta")
    print ("2.Retiro de efectivo")
    print ("3.Consulta de saldo")
    print ("4.Salir")
#Definir deposito y añadirlo a los fondos del usuario
def deposit(cardHolder):
    try:
        deposit = float(input("¿Cuanto dinero quieres depositar?:"))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Gracias por su depósito. Su saldo sería de: ", str(cardHolder.get_balance()))
    except:
        print("Invalido, intente de nuevo")
#Definir retiro y sustraerlo de los fondos del usuario
def retiro(cardHolder):
    try:
        retiro = float(input("¿Cuanto dinero quieres retirar?: "))
        #Revisar que usuario tenga suficientes fondos
        if(cardHolder.get_balance() < retiro):
            print("Fondos insuficientes")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - retiro)
            print("Listo, gracias por su visita")
    except:
        print("Invalido, intente de nuevo")

def revisar_fondos(cardHolder):
    print("Tu saldo es de: ", cardHolder.get_balance())

if __name__ == "__main__":
    current_user = cardHolder("","","","","")

    #Creacion de base de datos
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("1234567891011121", 1234, "Juan", "Perez", 100.10))
    list_of_cardHolders.append(cardHolder("2234567891011121", 2234, "Jenny", "Lopez", 10.35))
    list_of_cardHolders.append(cardHolder("3234567891011121", 3234, "Jason", "Herdez", 200.00))
    list_of_cardHolders.append(cardHolder("4234567891011121", 4234, "Julia", "Lourdez", 1100.00))
    list_of_cardHolders.append(cardHolder("5234567891011121", 5234, "Jacinto", "Cano", 0.10))
    list_of_cardHolders.append(cardHolder("6234567891011121", 6234, "Juana", "Habana", 100.68))

    #Pedir a usuario su tarjeta
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Por favor, ingresa el numero de tu tarjeta: ")
            #Revisar si existe en el sistema
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch [0]
                break
            else:
                print("Esa tarjeta no existe, intentalo de nuevo")               
        except:
            print("Esa tarjeta no existe, intentalo de nuevo")

    #Pedir su PIN al usuario
    while True:
        try:
            userPin = int(input("Por favor, ingrese su PIN: ").strip())
            if(current_user.get_pin() == userPin):
                break
            else:
                print("PIN Invalido. Por favor intenta de nuevo.")
        except:
            print("PIN Invalido. Por favor intenta de nuevo.")

    #Mostrar opciones
    print("Bienvenido ", current_user.get_nombre())
    option = 0
    while (True):
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalido, intente de nuevo")

        if(option == 1):
            deposit(current_user)
        elif(option ==2):
            retiro(current_user)
        elif(option == 3):
            revisar_fondos(current_user)
        elif(option == 4):
            break
        else:
            option = 0

    print("Gracias por su visita")