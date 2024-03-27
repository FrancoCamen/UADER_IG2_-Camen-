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
        print("Factorial de un numero negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 


while True:
    if len(sys.argv) == 1:
        try:
            num = int(input("Por favor, ingrese un numero: "))
            print("Factorial", num, "! es", factorial(num))
            break
        except ValueError:
            print("¡Debe ingresar un numero entero!")
    else:
        num = int(sys.argv[1])
        print("Factorial", num, "! es", factorial(num))
        break

