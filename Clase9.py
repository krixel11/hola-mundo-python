# coding = utf-8

# LISTAS DE DATOS :REYRISA:

print('Programa para demostrar el funcionamiento y manipulación de una lista.')

una_lista = [15, 20, 40, 0, -30]

print('\nMi lista tiene los valores: ', una_lista)

print(f'Mi lista tiene {len(una_lista)} valores') # Mostrar cuantos elementos tiene

print('\nMi lista colo cando un elemento por linea utilizando un ciclo for elaborado es:')
for elemento in range(0,len(una_lista)):
    print(una_lista[elemento])

# Cambiar el valor de un elemento de la lista
una_lista[3] = 10
print('La lista con elemento actualizado es ', una_lista)

# Agregar valor
una_lista.append(12)
print('La lista con elemento actualizado es ', una_lista)

# Remover un elemento de la lista

una_lista.remove(10)
print('La lista con elemento actualizado es ', una_lista)

# Remover un elemento con posicion

una_lista.pop(3)
print('La lista con elemento actualizado es ', una_lista)

# Extender una lista agregando mas caca
una_lista.extend([5, 1000, -24])
print('La lista con elemento actualizado es ', una_lista)