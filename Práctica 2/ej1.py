import re

l = re.split('[\s()]', open("texto.txt").read())        #Uso de expresiones regulares para cada salto de linea
for elem in l:                                       
    if "https" in elem: 
        print(elem)
