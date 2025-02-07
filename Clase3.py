#coding=utf-8
# Bucles For and While.


# Programa que imprima los números del 1 al 10 de manera ascendente

print('Programa que visualiza los números del 1 al 10\n')

# Partes de un ciclo de control
# Variable de control y su asignación inicial
# Condición del ciclo que hace que mientras sea verdadero se ejecute
# Sentencia de salida del ciclo

numero = 1
while numero <= 10:
    print (numero)
    numero = numero + 1

print('\nEnd', numero)

# Imprimir pares
numero2 = 10
while numero2 >= 1:
    print (numero2)
    numero2 = numero2 - 2

print('\nEnd', numero2, '\n')
# Imprimir los primeros 12 múltiplos de 7

multiplos = int(input('Ingrese los múltiplos '))
contador = 1

if multiplos >= 0:
    while contador <= multiplos:
        print (f'7 x {contador} = {contador * 7}')
        contador += 1
else:
    print('erro')
