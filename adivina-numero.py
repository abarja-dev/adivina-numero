'''
Script sencillo que propone un juego simple, saca un número aleatorio y pide al usuario que lo adivine en 9 intentos
'''

from random import randint

# variables necesarias

numero = randint(1, 100)
nombre = input('Hola, ¿cómo te llamas?: ')


# función que crea un bucle para solicitar un número y compararlo con el número correcto

def juego():
    intentos = 0
    while intentos <= 8:
        try:
            respuesta = int(input('¿En qué número estoy pensando?: '))
        except ValueError:
            print('Eso no es un número válido, inténtalo de nuevo.')
            continue

        if respuesta not in range(1, 101):
            print('Ese número no está entre 1 y 100! Tramposo!')
            continue

        intentos += 1

        if respuesta > numero:
            print('El número que buscas es menor')

        elif respuesta < numero:
            print('El número que buscas es mayor')

        elif respuesta == numero:
            print(f'¡Felicidades {nombre}! Has acertado en {intentos} intentos!')
            break

    else:
        print(f'GAME OVER. El número correcto era {numero}')


# Función principal del juego, donde se presenta, pide el nombre al usuario y lanza el juego

def adivinanumero():
    print(f'Bienvenido {nombre}! Vamos a jugar a un juego, voy a pensar en un número entre el 1 y el 100'
          f' y tu tienes 9 intentos para adivinarlo, suerte!')
    juego()

adivinanumero()