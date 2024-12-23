#Escribir un programa que pregunte al usuario la fecha de su nacimiento
# en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
# Adaptar el programa anterior para que también funcione cuando el día o 
# el mes se introduzcan con un solo carácter.

nacimiento = input('ingrese su fecha de nacimiento dd/mm/aaaa: ')

print('dia',nacimiento[:2])
print('dia',nacimiento[3:5])
print('dia',nacimiento[6:])