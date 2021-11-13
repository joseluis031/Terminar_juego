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