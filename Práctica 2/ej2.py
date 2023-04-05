from collections import Counter
import re

palabras = re.findall(r'\w+', open('README.md').read().lower())         #Uso de expresiones regulares
l = Counter(palabras).most_common(1)            
print("La palabra que aparece más veces en el texto de numpy es: ", l)