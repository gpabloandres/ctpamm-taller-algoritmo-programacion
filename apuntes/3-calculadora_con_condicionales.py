#------------------------------------------------
# Fecha: 12-04-23
# Estudiante: Su nombre
# Título: Caculadora con Condicionales IF-ELSE.
#-----------------------------------------------

# Declarar y definir las variables

numero_1 = float(input("Introduce el valor del primer número: "))
numero_2 = float(input("Introduce el valor del segundo número: "))

# Empezar el cálculo

print("¿Qué operación desea realizar?")

# Presentar menú de opciones.

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Guardar en una variable la opción seleccionada

eleccion = input("Ingrese su opción: ")

# Procesar la opción seleccionada.

if eleccion =="1":
    print("La suma de ambos números es igual a: ")
    print(numero_1 + numero_2)

elif eleccion =="2":
    print("La resta de ambos números es igual a: ")
    print(numero_1 - numero_2)

elif eleccion =="3":
    print("La multiplicación de ambos números es igual a: ")
    print(numero_1 * numero_2)

elif eleccion =="4":
    # Evitar dividir por cero.
    if numero_2 == 0:
        print("Operación invalida")
    else:
        print("La división de ambos números es igual a: ")
        print(numero_1 / numero_2)

else:
    print("Opción invalida, vuelva a intentarlo.")