import random

def adivinaNumero(x):
    print('====================================')
    print('Bienvenido jugador a las adivinanzas')
    print('====================================')
    print()
    print('*Debes adivinar el numero generado por el pc')
    print()

    numAleatorio = random.randint(1, x)
    prediccion = 0

    while prediccion != numAleatorio:
        #el usuario debe ingresar un numero
        prediccion = int(input(f'Ingresa un numero entre 1 y {x}: '))

        if prediccion < numAleatorio:
            print('Intentalo nuevamente, numero muy pequeño')
        elif prediccion > numAleatorio:
            print('Intentalo nuevamente, numero muy alto')

    print(f'Adivinaste el numero!!!{numAleatorio}')
    
#llamar funcion 
adivinaNumero(10)