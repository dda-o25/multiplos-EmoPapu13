"""
Programa que sirve para saber si un numero es multiplo de otro
"""

# Declaraciones


# Entradas
num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))

# Proceso y salidas porque ya intente con todo y quiero probar a ver si juntos funciona
if num2 != 0 and num1 % num2 == 0:
    print(f"El número {num1} es múltiplo del {num2}")
elif num1 != 0 and num2 % num1 == 0:
    print(f"El número {num2} es múltiplo del {num1}")
elif num1 == 0 or num2 == 0:
    print(f"El número 0 es múltiplo del {num1 or num2}")
else:
    print("Ninguno de los números es múltiplo del otro")

