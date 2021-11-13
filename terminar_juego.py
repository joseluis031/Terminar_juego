
MIN = 0  #Defino los parametros entre los que quiero que trabaje la funcion 
MAX = 99
minimo = MIN
maximo = MAX
def pedir_numero(invitacion, minimo, maximo):
    invitacion += " entre " + str(minimo) + " y " + str(maximo) + " :"  #no entiendo muy bien el uso de invitacion
    while True:
        entrada = input(invitacion)  #Aquí tenemos una función que pide al usuario que introduzca un número cualquiera
        try:
            entrada = int(entrada)
        except:
            pass
        else:
            if minimo <= entrada <= maximo:
                break
    return entrada

# Parte 1
print("Introduce el numero a adivinar")
numero = pedir_numero("Introduzca el numero a adivinar",)  #Hace referencia a la funcion definida anteriormente bajo el nombre de pedir_numero()

#Parte 2
print("Intente adivinar el numero")
while True:
    intento = pedir_numero("Intente adivinar el numero", minimo, maximo) #Aqui tambien se hace referencia a la funcion anterior
    if intento < numero:
        print("Te has quedado corto")
        minimo = intento + 1 #Esto sirve para ayudar a acertar el numero, reduce posibilidades
    elif intento > numero:
        print("Te has pasado crack")
        maximo = intento - 1
    else:
        print("Enhorabuena campeon, lo has acertado")
        break