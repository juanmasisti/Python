
texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que 
el de una mujer es de $45.000. Además, las mujeres tienen menos 
posibilidades de acceder a puestos de liderazgo en las empresas.
 """
 
lista_palabras = texto.lower().split()
cant_palabras = 0


for palabra in lista_palabras:
    cant_letras = 0
    for letra in palabra:
        if letra != "$":
            cant_letras += 1
    if cant_letras == len(palabra):
        cant_palabras+= 1

print("Cantidad de palabras: ", cant_palabras) 
  
