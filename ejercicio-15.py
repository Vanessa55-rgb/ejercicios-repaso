#Ordenar una lista de palabras alfabéticamente y luego al revés.
palabras = ["vanessa","gato","clima"]
print("las palabras son: ",palabras)

palabras.sort() #sort Organizar palabras alfabeticamente 
print(palabras)
print("Ordenadas alfabeticamente: ",palabras)
#or palabras.reverse
palabras.sort(reverse=True)
print("las palabras en orden alfabetico alreves son: ",palabras)
