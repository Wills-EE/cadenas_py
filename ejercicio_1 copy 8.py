#Escribir un programa que pregunte por consola el precio de un producto
# en euros con dos decimales y muestre por pantalla el número de euros
# y el número de céntimos del precio introducido.

producto = input("cual es el precio en € ?: ")
#find encuentra la primera apariciom caracter
print(f'el precio es {producto[:producto.find('.')]} € con {producto[producto.find('.')+1:]}centimos')
