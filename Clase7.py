# coding = utf-8
# F U N C I O N E S

from datetime import date
from datetime import datetime

def saludar():
    print('Hola a todo el que ejecute este programa')

def multiplicacion(numero):
        for multiplicador in range(1,11):
             print(f'{numero} x {multiplicador} = {numero * multiplicador}')

def potencia(numero):
     cubo = numero ** 3
     return cubo

def obtenerfecha():
    fechadato = datetime.now()
    fechaformateada = fechadato.strftime("%d-%m-%Y %H:%M:%S")
    return fechaformateada

print('Programa para demostrar el uso de funciones')
for ciclo in range(1,11):
    saludar()

entero = False
while entero is False:
    try:
        numero = int(input('\nIngrese un número entero: '))
        print(f'\nLa tabla de multiplicar del numero {numero} es: ')

        multiplicacion(numero)

        valorcubico = potencia(numero)
        print(f'\nEl valor cúbico del {numero} es {valorcubico}')
        entero = True
    except ValueError:
        print('Tontp eso no es un número entero')
        continue

datofecha = obtenerfecha()
print(datofecha)