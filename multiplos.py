"""
Programa que sirve para saber si un numero es multiplo de otro
"""

# Declaraciones


# Entradas
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))

# Proceso
if num1 == 0 or num2 == 0:
    mensaje = "No se puede dividir entre 0"
else:
    if num1 % num2 == 0:
        mensaje = f"{num1} es multiplo de {num2}"
    else:
        mensaje = f"{num1} no es multiplo de {num2}"

# Salidas
print(mensaje)
