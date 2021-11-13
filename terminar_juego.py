def pedir_numero():
    while True:
        entrada = input("Introduzca un numero entre 0 y 99")  #Aquí tenemos una función que pide al usuario que introduzca un número cualquiera
        try:
            entrada = int(entrada)
        except:
            pass
        else:
            if 0 <= entrada <= 99:
                break
    return entrada

# Parte 1
print("Introduce el numero a adivinar")
numero = pedir_numero()  #Hace referencia a la funcion definida anteriormente bajo el nombre de pedir_numero()

#Parte 2
print("Intente adivinar el numero")
while True:
    intento = pedir_numero() #Aqui tambien se hace referencia a la funcion anterior
    if intento < numero:
        print("Te has quedado corto")
    elif intento > numero:
        print("Te has pasado crack")
    else:
        print("Enhorabuena campeon, lo has acertado")
        break