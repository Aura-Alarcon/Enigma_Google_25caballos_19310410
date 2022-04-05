# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 03:05:13 2022

@author: Aura Alarcón
"""

import numpy as np #Librería para todos los cálculos numéricos
import random  #Librería para poder generar números, variables o listas de manera aleatoria

listaA = ['ca1','ca2','ca3','ca4','ca5'] #Primer grupo de caballos

listaB = ['cb1','cb2','cb3','cb4','cb5'] #Segundo grupo de caballos

listaC = ['cc1','cc2','cc3','cc4','cc5'] #Tercer grupo de caballos

listaD = ['cd1','cd2','cd3','cd4','cd5'] #Cuarto grupo de caballos

listaE = ['ce1','ce2','ce3','ce4','ce5'] #Quinto grupo de caballos

print ('Caballos a competir') #Primera impresión que muestra todos los grupos y caballos a competir

print('Grupo A \n', listaA)
print('Grupo B \n', listaB)
print('Grupo C \n', listaC)
print('Grupo D \n', listaD)
print('Grupo E \n', listaE)

VelCaballos = np.zeros([5,5]) #Primer arreglo necesario para calcular la velocidad de cada caballo
dimension= VelCaballos.shape #Encuentra las dimensiones del array
for x in range (dimension[0]):
    for y in range(dimension[1]):
        VelCaballos[x,y]=random.randint(1,99) #función dedicada a devolver un numero entero, en este caso, una velocidad aleatoria

print ('Velocidades de los caballos de menor a mayor')
for x in range (5):
    VelCaballos[x].sort #función encargada de ordenar las listas en este caso de manor a mayor de manera aleatoria
    for y in range(5):
        VelCaballos = VelCaballos[np.argsort(VelCaballos[:,-1])]  #Encargado de hacer un ordenamiento de manera indirecta
for x in range(5):
    print('grupo',5-x,'\n:',VelCaballos[x]) 
    
print('5 carreras principales: \n') #Se muestran las primeras 5 carreras
for x in range(5):
    print('El caballo ganador del grupo: ',5-x,VelCaballos[x,4])
    
print('La el caballo ganador de la carrera número 6; \n') #Se muestra el ganador de la carrera 6
print('El caballo más rápido es el caballo con un tiempo de llegada: \n',VelCaballos[4,4])

print('\nCarrera número 7: \n')
#Compara la velocidad de cada ganador de cada lista y acomoda al segundo más rápido
if VelCaballos[3,4] > VelCaballos[4,0] and VelCaballos [3,4] > VelCaballos[4,1] and VelCaballos[3,4] > VelCaballos[4,2] and VelCaballos[3,4] > VelCaballos[4,3]:
    print('El segundo mas rapido: b1, con un tiempo de llegada: \n',VelCaballos[3,4])

elif VelCaballos[4,3] > VelCaballos[3,4]:
    print('El segundo caballo  mas rapido es: a2, con un tiempo de llegada: \n',VelCaballos[4,3])

elif VelCaballos[3,4] == VelCaballos[4,3]:
    print('Empate b1:',VelCaballos[3,4],'y a2',VelCaballos[4,3])

        
        
        
        
        
        
        
        
