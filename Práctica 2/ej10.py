import re

#A
def devolver_notas_alumnos(nombres, notas_1, notas_2):
    """ Esta función devuelve un diccionario donde la clave es el nombre del alumno y el valor es una tupla con las 2 notas. """
    return {key:(value1,value2) for (key, value1, value2) in zip(nombres, notas_1, notas_2)}    
    # Recibo por parametro los nombres y las 2 notas. Utilizando el zip transformo estas tres listas en un iterable para poder utilizar al formar el diccionario.
    # Recorremos este iterable a través de un for, asignado como clave el nombre del alumno (con la variable key) y como valor una tupla con la primer (value1) y segunda nota (value2). 
    # Devolviendo asi lo pedido.

#B
def calcular_promedio_de_notas(notas):
    """ Esta función devuelve un diccionario donde la clave es el nombre del alumno y el valor es el promedio de sus 2 notas."""
    return {key:(tupla[0]+tupla[1])/2 for (key, tupla) in notas.items()}    

#C
def calcular_promedio_general(notas): 
    """" Esta funcion devuelve una lista con el promedio general del curso. """
    return sum(notas.values())/len(notas)

#D
def estudiante_max(notas_promedio):
    """ Esta función devuelve al estudiante con mayor promedio de nota. """
    return max(notas_promedio, key=notas_promedio.get) 

#E
def estudiante_min(notas):
    """ Esta función devuelve al estudiante con menor nota obtenida. """
    return min(notas, key=notas.get) 

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

nombres_limpio = re.sub("['\n ]", '', nombres).split(',')  #Con el sub elimino elementos del string (salto de linea y comilla simple)

notas_alumnos = devolver_notas_alumnos(nombres_limpio, notas_1,notas_2) #Diccionario con los nombres como clave y las tuplas con las 2 notas.
print(" ➡ Diccionario de notas: \n", notas_alumnos)
promedio_notas_alumnos = calcular_promedio_de_notas(notas_alumnos) #Diccionario con el nombre como clave y la nota promedio como valor.
print("\n ➡ Promedio de cada uno de los estudiantes: ", promedio_notas_alumnos)
print("\n ➡ Promedio de toda la clase: ", f"{calcular_promedio_general(promedio_notas_alumnos):.2f}")
print("\n ➡ Estudiante con mayor promedio de nota: ", estudiante_max(promedio_notas_alumnos))
print("\n ➡ Estudiante con la menor nota obtenida: ", estudiante_min(notas_alumnos))
