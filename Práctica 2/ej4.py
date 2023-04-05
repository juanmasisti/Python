
evaluar = """ título: Experiences in Developing a Distributed Agent-based 
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance 
computing resources provides the promise of capturing unprecedented details 
of large-scale complex systems. However, the specialized knowledge required 
for developing such ABMs creates barriers to wider adoption and utilization. 
Here we present our experiences in developing an initial implementation of 
Repast4Py, a Python-based distributed ABM toolkit. We build on our 
experiences in developing ABM toolkits, including Repast for High 
Performance Computing (Repast HPC), to identify the key elements of a useful 
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages 
and the Python C-API to create a scalable modeling system that can exploit 
the largest HPC resources and emerging computing architectures.
"""

l = evaluar.lower().split('resumen:')   # Separo el texto en titulo y resumen

titulo = l[0].lower().split('título: ')  # Separo el contenido del titulo:
titulo = titulo[1].lower().split()  # Separo cada palabra del titulo 

oraciones = l[1].lower().split('.')  # Dentro del resumen separo las oraciones


if (len(titulo) <=10):
    print("titulo: ok")
else:
    print("titulo: no cumple")

facil = 0
aceptables = 0
dicifil = 0
muy_dificil = 0

for oracion in oraciones:       
    palabras = oracion.lower().split()          #Separo las palabras de cada oracion
    if (len(palabras) <= 12):           
        facil+= 1
    elif (len(palabras) >= 13 and len(palabras)<= 17):
        aceptables+=1
    elif (len(palabras) >= 18 and len(palabras)<= 25):
        dicifil+=1
    else:
        muy_dificil+=1
        
print("• Cantidad de oraciones fáciles de leer: ", facil)
print("• Cantidad de oraciones aceptables para leer: ", aceptables)   
print("• Cantidad de oraciones dificil de leer: ", dicifil)  
print("• Cantidad de oraciones muy dificil de leer: ", muy_dificil)                  