#------------------------------------------------
# Fecha: 19-04-23
# Estudiante: Su nombre
# Título: Proyecto 1- Lista de compras.
#-----------------------------------------------

# Definir y declarar variables
#Crear una lista
lista_articulos = list()

while True:
    print("**********Menú************")
    print("1- Agregar artículos")
    print("2- Borrar artículos")
    print("3- Ver lista de artículos")
    print("4- Salir")
    print("**************************")
    
    opcion = int(input("Seleccione una opción del menú: "))

    # Revisar si la opción ingresada es válida.
    if opcion <=0 or opcion >4:
        print("¡Ingrese una opción válida!\n")
        continue 
    elif opcion == 1:
        print("*****Agregar un artículo a la lista*****")
        articulo = input("Indica el nombre del artículo: ")
        lista_articulos.append(articulo)
        print(f"¡El artículo {articulo} fué agregado exitosamente!\n")
    elif opcion == 2:
        print("*****Borrar un artículo de la lista*****")
        articulo = input("Indica el nombre del artículo a eliminar: ")
        lista_articulos.remove(articulo)
        print(f"¡El artículo fué borrado exitosamente!\n")
    elif opcion == 3:
        print("***Imprimir los artículos de la lista***")
        print("Los artículos de su lista son: ")
        for articulo in lista_articulos:
            print(articulo)
    else:
        break
print("¡Gracias por utilizar nuestra lista en Python!")