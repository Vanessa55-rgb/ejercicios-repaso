#Pide la edad y clasifica: niño, adolescente, adulto, anciano.

Edad = int(input("Digita la edad: "))

if Edad >= 0 and Edad <= 12:
    print("niño")
elif Edad >= 12 and Edad < 18:
    print("adolecente")
elif Edad >= 18 and Edad < 60:
    print("adulto")
elif Edad >= 60 and Edad < 100:
    print("Anciano")