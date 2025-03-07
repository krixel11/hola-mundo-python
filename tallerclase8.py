# coding = utf-8

salir = False

# Función convertir horas y minutos a segundos.
def convertir_a_segundos():
    # Variable de control, si el usuario ingresa un dato erróneo no lo manda directamente al menú sino que lo devuelve hasta terminar.
    procesoCompleto = False
    while procesoCompleto is False:
        try:
            horas = int(input('\nInserte las horas que desea convertir a segundos como número entero '))
            minutos = float(input('Inserte los minutos que desea convertir a segundos '))
            segsh = horas * 3600
            segsm = minutos * 60
            total = segsh + segsm
            print(f'\nSus {horas} horas y {minutos} minutos convertidos a segundos son',"%.2f"%total, 'segundos.')
            procesoCompleto = True
        except ValueError:
            print('\nTodavía no sabes qué es un entero?')
            continue
        
# Función para convertir segundos a horas y minutos
def convertir_desde_segundos():
    hora = 0
    procesoCompleto = False
    while procesoCompleto is False:
        try:
            segundos = int(input('\nInserte sus segundos como un número entero y los convertiremos a horas '))
            mins = segundos/60
            # Variable para convertir, digamos, 80 minutos en 1 hora y 20 minutos, no se me ocurrió hacerlo de otra forma, pero funciona
            while mins >= 60:
                hora += 1
                mins -= 60
            print(f'\nSus {segundos} segundos convertidos a horas y minutos son {hora} horas y',"%.2f"%mins, 'minutos')
            procesoCompleto = True
        except ValueError:
            print('\nSi no sabes que es un número entero solo dices')
            continue

print('Programa que convierte el tiempo de horas y minutos a segundos y vice versa')

while salir is False:
    try:
        option = int(input('\n¿Qué deseas hacer? 1. Para convertir desde segundos a horas y minutos. 2. Para convertir de horas y minutos a segundos. 3. Para salir '))
        if option == 1:
            convertir_desde_segundos()
        elif option == 2:
            convertir_a_segundos()
        elif option == 3:
            print('\nLindo día')
            salir = True
        else:
            print('\nID no válido')
    except ValueError:
        print('\nNúmero entero.')
        continue        

