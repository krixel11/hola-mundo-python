# coding = utf-8
print('Programa para calcular IMC')
datos_erroneos = True
while datos_erroneos is True:
    try:
        Peso = float(input('\nIngrese su peso en kg: '))
    except ValueError:
        print('\nEl dato del peso es erróneo.')
        continue
    try:
        Altura = float(input('Ingrese su altura en metros: '))
    except ValueError:
        print('\nEl dato de la altura es erróneo')
        continue
    imc = Peso/Altura**2
    print(f'\nSu IMC es: {imc}')
    datos_erroneos = False

if imc < 18.5:
    print('\nSu persona tiene bajo peso')
elif imc >= 18.5 and imc < 25:
    print('\nSu persona tiene peso normal')
elif imc >= 25 and imc < 29.9:
    print('\n')
else:
    print('\n Su persona está en el estado de estar en obesidad')