# coding = utft-8

# Programa para generar un fractal hacia abajo

print('Primer arbolito: Ladeado a la izquierda')

ramas = 1
while ramas <= 10:
    print('*' * ramas)
    ramas += 1

print('\nArbolito ladeado a la derecha')
espacios = 9
ramas = 1
while ramas <= 10:
    print((' ' * espacios) + ('*' * ramas))
    ramas += 1
    espacios -= 1

print('\nArbolito ladeado a la izquierda al revés')

ramas = 10
while ramas >= 1:
    print('*' * ramas)
    ramas -= 1

print('\nArbolito ladeado a la derecha al revés')
espacios = 0
ramas = 10
while ramas >= 1:
    print((' ' * espacios) + ('*' * ramas))
    ramas -= 1
    espacios += 1

print('\nArbolito Centrado')
espacios = 10
ramas = 1
while ramas <= 20:
    print((' ' * espacios) + ('*' * ramas))
    ramas += 2
    espacios -= 1

print('\nArbolito Centrado al revés')
espacios = 1
ramas = 19
while ramas >= 1:
    print((' ' * espacios) + ('*' * ramas))
    ramas -= 2
    espacios += 1