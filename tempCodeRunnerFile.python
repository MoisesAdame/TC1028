#Librerías
import csv                          #Analizar docs en csv
import matplotlib                   #Crear gráficas
import matplotlib.pyplot as plt     
import numpy as np                  #Análisis de arrays de grandes tamaños
import pprint                       #print de diccionarios de forma entendible 
import math as mt                   #funciones matemáticas (ya en numpy u-funcs)

open_doc = open("ElectricCars.csv")
read_doc = csv.reader(open_doc)
main_data = np.array(list(read_doc))

#Ejemplo de Uso
#Para obtener una lista de la velocidad máxima (Usando numpy)
vel_max = main_data[:,3]
pprint.pprint(vel_max)
