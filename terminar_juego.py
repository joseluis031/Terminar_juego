import random
MIN = 0  #Defino los parametros entre los que quiero que trabaje la funcion 
MAX = 0
minimo = MIN
maximo = MAX
intentos_maximos = 0

while True: #Defino las "caracteristicas" del juego dependiendo de la dificultad que elija el usuario
    nivel = input ("Seleccione un nivel: facil, medio, avanzado, o maestro:")
    if nivel == "facil":
            maximo = 100
            intentos_maximos = 10
            break
    elif nivel == "medio":
            maximo = 1000
            intentos_maximos = 20
            break
    elif nivel == "avanzado":
            maximo = 1000000
            intentos_maximos = 50
    elif nivel == "maestro":
            maximo = 1000000000000
            intentos_maximos = 100
            break
numero_elegido = random.randint(minimo,maximo)

def pedir_numero(invitacion):
    invitacion += " entre " + str(minimo) + " y " + str(maximo) + " :"
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

def ayudas(): #Defino una funcion por si el usuario quiere una ayuda
    ayuda = input ("¿Quiere algo de ayuda? si o no????")
    ayuda = ayuda.lower() #Para quitar el none que me salia
    try:
        if ayuda == "si":
            print("El numero esta entre " + str(minimo) + " y " + str(maximo))
        elif ayuda == "no":
            print("Tu te lo pierdes...")
    except:
        pass
    return ayuda

help = ayudas()
intentos = 1
#Parte 2 (Comienzo del juego)
print("Que comienze el juego, intenta adivinar el numero aleatorio")
while True:
    intento = pedir_numero("Intente adivinar el numero") #Aqui tambien se hace referencia a la funcion anterior
    if intento < numero_elegido:
        print("Te has quedado corto")
        minimo = intento + 1 #Esto sirve para ayudar a acertar el numero, reduce posibilidades
        intentos += 1 #Esto suma 1 a los intentos que llevas hasta alcanzar el numero maximo de intentos que tienes
    elif intento > numero_elegido:
        print("Te has pasado crack")
        maximo = intento - 1
        intentos += 1
    else:
        print("Enhorabuena campeon, lo has acertado")
        print("Ha necesitado ", intentos, "intentos para adivinarlo")
        break

if intentos == intentos_maximos:
    print("No te quedan mas oportunidades, has perdido :(") 