#Pide 5 números y crea una lista solo con los pares.

numerospares = []

for i in range (5):
    numero = int(input(f"Digita el numero {i+1}: "))
    if numero % 2 == 0:
        numerospares.append(numero)

print("Numeros pares ingresados son : ", numerospares)