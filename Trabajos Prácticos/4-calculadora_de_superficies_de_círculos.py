#------------------------------------------------------------------------------------
# Fecha: 04-04-23
# Estudiante: Pablo
# Título: Calculadora de superficies de círculos
#------------------------------------------------------------------------------------

print("Calculadora de superficies de círculos\n")

# Declaro y defino las variables.
pi = float(input("Introduzca pi: ")) #3.14
radio = int(input("Introduzca el tamaño del radio: "))

# Calculo la superficie del círculo
respuesta = pi * (radio ** 2)

# Muestro la respuesta
print("La superficie del círculo es: ")
print(respuesta)