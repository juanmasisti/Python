palabra = (input("Ingrese una palabra: ")).replace(' ', '').replace('-', '').lower()
palabra = list(palabra)
no_es_heterograma = False
cant = 0
print(palabra)

for letra in palabra:
    if cant > 1:
        no_es_heterograma = True
    cant = 0
    for aux in palabra:
        if letra == aux:
            cant += 1
 
if no_es_heterograma:
    print("La palabra no es un heterograma")
else:
    print("La palabra es un heterograma")           