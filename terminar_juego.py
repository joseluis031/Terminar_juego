import random
MIN = 0  #Defino los parametros entre los que quiero que trabaje la funcion 
MAX = 0
minimo = MIN
maximo = MAX
numero_elegido = random.randint(minimo,maximo)

while True:
    nivel = input ("Seleccione un nivel: facil, medio, avanzado, o maestro:")
    if nivel == "facil":
            maximo = 100
            break
    elif nivel == "medio":
            maximo = 1000
            break
    elif nivel == "avanzado":
            maximo = 1000000
    elif nivel == "maestro":
            maximo = 1000000000000
            break
    
def pedir_numero(invitacion):
    invitacion += " entre " + str(minimo) + " y " + str(maximo) + " :"  #no entiendo muy bien el uso de invitacion
    while True:
        entrada = input(invitacion)  #Aquí tenemos una función que pide al usuario que introduzca un número cualquiera
        try:
            entrada = int(entrada)
        except:
            pass
        if entrada > maximo or entrada < minimo:
            print ("El numero introducido no esta dentro del rango, repita con otro numero")
        else:
            if minimo <= entrada <= maximo:
                break

    return entrada

def ayudas():
    ayuda = input (print("¿Quiere algo de ayuda? si o no????"))
    try:
        if ayuda == "si" or ayuda == "no":
            print("El numero esta entre " + str(minimo) + " y " + str(maximo))
        else:
            print("Tu te lo pierdes...")
    except:
        pass
    return ayuda

# Parte 1
print("Introduce el numero a adivinar")
numero = pedir_numero("Introduzca el numero a adivinar",)  #Hace referencia a la funcion definida anteriormente bajo el nombre de pedir_numero()

#Parte 2
print("Intente adivinar el numero")
while True:
    intento = pedir_numero("Intente adivinar el numero") #Aqui tambien se hace referencia a la funcion anterior
    if intento < numero:
        print("Te has quedado corto")
        minimo = intento + 1 #Esto sirve para ayudar a acertar el numero, reduce posibilidades
    elif intento > numero:
        print("Te has pasado crack")
        maximo = intento - 1
    else:
        print("Enhorabuena campeon, lo has acertado")
        break