#coding=utf-8

# Programa que lee un dato de hora y lo convierte a minutos
# Entrada: Valor de la hora
# Salida: El valor de la hora en minutos

print('Programa que lee una hora y lo convierte a minutos')
hora_ingresada = input('Ingrese la hora ')
# hora = int(hora_ingresada)

# Identificamos si en la cadena hay el caracter "."
if '.' in hora_ingresada:
    hora_ingresada = float(hora_ingresada)
else:
    hora_ingresada = int(hora_ingresada)
print('El tipo de variable de la hora es ', type(hora_ingresada))

minutos = hora_ingresada*60
print(f'Las {hora_ingresada} horas convertidas en minutos es {minutos}')
# esa f deja poner llaves, se llama "formato"
print('El tipo de datos de los minutos es', type(minutos))

# elif comprime otro condicional en solo 1