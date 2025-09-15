"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones


# Entradas
numero_1=int(input("Ingrese el primer numero: "))
numero_2=int(input("Ingresa el segundo numero: "))

# Proceso
if numero_2 == 0:
    multiplo=False
    mensaje_final="No se puede dividir entre 0 bro"
else:
    if numero_1 % numero_2 == 0:
        multiplo=True
        mensaje_final=numero_1, "si es multiplo de", numero_2
    else:
        multiplo=False
        mensaje_final=numero_1, "no es multiplo de ", numero_2

# Salidas
print(mensaje_final)
