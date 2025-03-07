import random
# coding = utf-8
# Generar un número del 1 al 100 y que el usuario lo pueda adivinar
print('Programa para adivinar un número aleatorio entre 1 y 100')

numero = random.randint(1, 100)
limiteinf = 1
limitesup = 100


intentos = 0
dato = 0

while dato != numero:
    dato = int(input(f'Ingrse un número del {limiteinf} al {limitesup} '))
    intentos += 1
    if dato < limiteinf or dato > limitesup:
        print(f'Error. El número ingresado debe estar entre {limiteinf} y {limitesup}')
        continue
    if dato < numero:
        print(f'El número {dato} es menor al número secreto. Inténtelo de nuevo')
    elif dato > numero:
        print(f'El número {dato} es mayor al número secreto. Inténtelo de nuevo')

print(f'El número {dato} es el número correcto. Felicidades, lo has adivinado en {intentos} intentos')         