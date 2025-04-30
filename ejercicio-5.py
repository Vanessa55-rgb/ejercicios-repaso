#Pide dos números. Si ambos son mayores que 0, muestra "Ambos son positivos".

Numero1 = int(input("ingresa n1: "))
Numero2 = int(input("Ingresa n2: "))

if Numero1 > 0 and Numero2 > 0:
    print("Ambos numeros son positivos")
else:
    print("AL menos uno no es positivo")