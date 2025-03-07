# coding = utf-8
# Lista ejercicio 100 numeros mostrar 10 por linea tabulados caca abuelita miedo payaso esponja horror terror

import random

def visualizarlista(lalista):
    for posicion in range(0, len(lalista)):
        if (posicion + 1) % 10 == 0:
            print()
        else:
            print(lalista[posicion], '\t', end="")

def obtenerpares(lalista):
    listapares = []
    for i in range(0, len(lalista)):
        if lalista[i] % 2 == 0:
            listapares.append(lalista[i])
    return listapares

def obtenerimpares(lalista):
    listaimpares = []
    for i in range(0, len(lalista)):
        if lalista[i] % 2 != 0:
            listaimpares.append(lalista[i])
    return listaimpares


print('Programa para generar una lista de 100 números enteros aleatorios')

# Aquí generamos la lista
lalista = []
for i in range (0,99):
    lalista.append(random.randrange(0, 100))

print(f'Hola')
visualizarlista(lalista)

# Sublista numeros pares

listapares = obtenerpares(lalista)
print('\nPillá webon')
visualizarlista(listapares)

listaimpares = obtenerimpares(lalista)
print('\nAl+o')
visualizarlista(listaimpares)

