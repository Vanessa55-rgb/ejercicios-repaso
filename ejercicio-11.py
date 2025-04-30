#Crea una lista vacía y permite al usuario añadir 3 nombres.
nombres = []

for i in range(3): # RANGE ES LIMITE DE REPETICIONES 
    nombre = input("Digita nombres: ")
    nombres.append(nombre)
print("Los nombres son: ",nombres)