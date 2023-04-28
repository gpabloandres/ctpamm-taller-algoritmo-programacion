#------------------------------------------------
# Fecha: 14-04-23
# Estudiante: Su nombre
# Título: Bucles FOR y WHILE.
#-----------------------------------------------

# Declarar y definir las variables.

marcas = ["Fiat", "Ford", "VW", "Chevrolet"]
# Esto es una lista.

#print(colores)

# Usar bucle FOR para recorrer la lista de colores.

for marca in marcas:
    if marca == "Fiat":
        continue    
    print(f"-marca {marca}")
    
# Usar bucle WHILE.

# Variable para el bucle.
i = 1

while i < 5:
    i = i + 1
    print(f"El valor del bucle es: {i}")