import re

jupyter_info = """ JupyterLab is a web-based interactive development 
environment for Jupyter notebooks, 
code, and data. JupyterLab is flexible: configure and arrange the user 
interface to support a wide range 
of workflows in data science, scientific computing, and machine learning. 
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing 
ones.
"""
palabras = jupyter_info.lower().split()        #Separo cada palabra del jupyter_info
letra = input("Ingrese una letra: \n ")

if letra.isalpha():         # Esta funcion devuelve si la letra es parte del alfabeto.
    for palabra in palabras:
        if (letra in palabra[0]):
            print(palabra)
else:
    print("Error: el caracter ingresado no es una letra")                   

