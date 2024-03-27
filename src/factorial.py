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
while True:
    if len(sys.argv) == 1:
        try:
            rango = input("Por favor, ingrese un rango (desde-hasta) para calcular los factoriales: ")
            if rango.startswith("-"):
                desde = 1
                hasta = int(rango.split("-")[1])
            elif rango.endswith("-"):
                desde = int(rango.split("-")[0])
                hasta = 15 #Se le define un limite fijo ya que no es necesario tanta iteracion
            elif "-" in rango:
                desde, hasta = map(int, rango.split("-"))
            else:
                raise ValueError
            break
        except ValueError:
            print("¡Debe ingresar un rango válido en el formato 'desde-hasta', '-hasta' o 'desde-'!")
    else:
        rango = sys.argv[1]
        if rango.startswith("-"):
            desde = 1
            hasta = int(rango.split("-")[1])
        elif rango.endswith("-"):
            desde = int(rango.split("-")[0])
            hasta = 60
        elif "-" in rango:
            desde, hasta = map(int, rango.split("-"))
        break

print("Los factoriales en el rango", desde, "-", hasta, "son:")
for num in range(desde, hasta + 1):
    print("Factorial", num, "! es", factorial(num))



