#Escribir un programa que pregunte el correo electrónico del usuario
# en la consola y muestre por pantalla otro correo electrónico con el 
# mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo = input("ingrese su correo: ")
 
print(f"{correo[:correo.find('@')]}@ceu.es.")

