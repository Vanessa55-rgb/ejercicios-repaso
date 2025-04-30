#Pide una nota (0-10). Muestra si perdio, aprobado o sobresaliente.

Nota = float(input("Digita la nota final: "))

if Nota <= 4:
    print("Perdio")
elif Nota > 4 and Nota <= 7:
    print("Aprovo")
elif Nota > 7 and Nota <= 10 :
    print("Sobresaliente")
else:
    print("Nota inválida")
