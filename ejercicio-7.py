#Pregunta si una persona tiene licencia y si lleva casco. Si no tiene licencia o no lleva casco, no puede conducir.

licencia = (input("Tienes licencia: "))
Casco = input("LLevas casco: ")

if licencia != "si" or Casco != "si":
    print("No puede conducir")
else:
    print("Puedes conducir")