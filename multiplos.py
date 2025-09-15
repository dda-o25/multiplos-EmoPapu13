"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones


# Entradas
numero_1=int(input("Ingrese el primer numero: "))
numero_2=int(input("Ingresa el segundo numero: "))

# Proceso
if numero_2 != 0:
    num_final=(numero_1%numero_2==0)
else:
    multiplo_no=False

# Salidas
if num_final:
    print(numero_1, "es multiplo de", numero_2)
else:
    print("ninguno de los dos numeros son multiplos")
