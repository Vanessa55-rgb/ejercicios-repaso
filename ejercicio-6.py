#Pide la hora. Si es menor que 12 o mayor que 18, muestra "No es hora de trabajar".

Hora = int(input("Digita la hora: "))

if Hora < 12 or Hora > 18:
    print("No es hora de trabajar")
else:
    print("Hora de trabajar")