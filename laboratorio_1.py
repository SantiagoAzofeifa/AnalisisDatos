# -*- coding: utf-8 -*-
"""Laboratorio 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QQMCaVACTNpRTDDrCtr-OGfhngLnFv9D
"""

# Laboratorio 1
# Andrea Chacon
# Jarren Chaves Vizcaino
# Santiago Azofeifa
# Oscar Gutiérrez R
# Grupo 07
import statistics
from statistics import median
print("Promedio de los elementos del vector")
Suma=0
Media=0
Temp=[]
print("Ingrese cantidad de temperaturas")
N=int(input())

for i in range(N):
  temperatura=float(input("Ingrese la temperatura "))
  Temp.append(temperatura)
  Suma=Suma+Temp[i]
Media=Suma/N
Moda = statistics.mode(Temp)
desviacion_estandar = statistics.stdev(Temp)
varianza = statistics.variance(Temp)
print("El promedio de las temperaturas es:", Media)
print( "-> La temperatura mas frecuente es:", Moda)
print("La varianza es:", varianza, "-> La dispercion con respecto al promedio de la temperatura que es:", varianza, " Es decir, la varianza es", varianza)
print("La desviacion estandar es:", desviacion_estandar, "Que es la raiz cuadrada de la dispercion con respecto al promedio es. Por lo tanto, la desviacion de la temperatura es:",desviacion_estandar)
print("Ordenando las temperaturas ascendentemente, la temperatura de en medio es: ")
print(median(Temp))

#Temperaturas (23,23,23,27,29,20,18,31,24,40)

