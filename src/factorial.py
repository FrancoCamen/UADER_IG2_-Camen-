#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num):     
    if num < 0: 
        print("Factorial de un número negativo no existe")
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

def calcular_factorial_entre_rango(desde, hasta):
    for num in range(desde, hasta + 1):
        print("Factorial de", num, "! es", factorial(num))

while True:
    if len(sys.argv) == 1:
        try:
            rango = input("Por favor, ingrese un rango de números en el formato desde-hasta (ej. 4-8): ")
            desde, hasta = map(int, rango.split("-"))
            calcular_factorial_entre_rango(desde, hasta)
            break
        except ValueError:
            print("¡Formato incorrecto! Debe ingresar un rango válido en el formato desde-hasta.")
    else:
        rango = sys.argv[1]
        desde, hasta = map(int, rango.split("-"))
        calcular_factorial_entre_rango(desde, hasta)
        break


