lista_palabras = input("Ingrese una frase: ")
string = input("Ingrese una palabra: ")
cant_palabras = 0

lista_palabras = lista_palabras.lower().split() #Genera una lista con cada palabra de la frase.

for palabra in lista_palabras: # Recorre cada palabra de la frase.
    if (palabra == string):
        cant_palabras+= 1 #Si es igual al string ingresado anteriormente aumento en 1 la variable.

print("Cantidad de veces que aparece la palabra: ", cant_palabras)