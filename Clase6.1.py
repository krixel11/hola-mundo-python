# coding = utf-8

conteo = 0
min = 0
max = 20
paso = -2
for variable in range(max,min,paso):
    print(f'El valor de la variable es {variable}')
    conteo += 1
print(f'\nEl programa se ejecutó {conteo} veces.')

for numero in range(1,11):
    print(f'\nLa tabla de multiplicar del numero {numero} es: ')

    for multiplicador in range(1,11):
        print(f'{numero} x {multiplicador} = {numero * multiplicador}')