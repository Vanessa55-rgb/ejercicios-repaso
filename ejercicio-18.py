#Agregar un número en una posición específica.

numeros = [1,55,25,35,6]

numeroIntroducido = int(input("Ingresa el numero que deseas introducir: "))
pocisionIntroducida = int(input("Ingresa la posicion del numero: (0-5)"))

numeros.insert(pocisionIntroducida,numeroIntroducido)
print(numeros)
