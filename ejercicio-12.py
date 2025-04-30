#Dada una lista de frutas, pide al usuario una fruta que quiera eliminar.

frutas = ["pera","manzana","arroz"]
print(frutas)

eliminarFruta = input("Digita la fruta que deseas eliminar: ")

if eliminarFruta in frutas:
    frutas.remove(eliminarFruta) #remove eliminar
print(frutas)    