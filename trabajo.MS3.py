#Eres parte del equipo de desarrollo de software de una tienda que desea mejorar la gestión de su inventario digital. Te han asignado la tarea de crear un programa en Python 
# que permita al equipo añadir, consultar, actualizar y eliminar productos del inventario de manera eficiente, así como calcular el valor total del inventario. Tu programa debe interactuar con el usuario para realizar las siguientes operaciones:
#Añadir productos:
#Cada producto debe estar definido por su nombre, precio y cantidad disponible
# Esta información será almacenada de modo que el inventario pueda crecer dinámicamente
#Consultar productos:
#Se debe poder buscar un producto por su nombre y obtener detalles como su precio y cantidad disponible
#       Si el producto no está en el inventario, se debe notificar adecuadamente
#  Actualizar precios:
#     El programa debe permitir al usuario seleccionar un producto e introducir un nuevo precio, asegurando que este se actualice correctamente en el inventario
#Eliminar productos:
#   El programa debe permitir al usuario eliminar productos del inventario de manera segura
#Calcular el valor total del inventario:
#    El programa debe calcular el valor total de los productos en inventario y mostrarlo al usuario
#   Para ello, utilizarás una función anónima (lambda) que facilite este cálculo.
#Tu programa debe diseñarse modularmente, con funciones bien definidas que gestionen cada operación mencionada. Además, debes almacenar los productos en un diccionario, donde el nombre del producto sea la clave, y el precio y la cantidad sean los valores asociados, almacenados en una tupla.
#El flujo del programa debe ser interactivo, permitiendo que el usuario escoja qué operación desea realizar. Además, asegúrate de manejar posibles errores, como la búsqueda de productos que no existen o intentos de añadir productos con datos inválidos.
#Finalmente, el código debe ser legible, bien estructurado y comentado. No olvides probar exhaustivamente tu solución con distintos escenarios para asegurar que funciona correctamente en todo tipo de casos. 

#directorio de inventario

inventario={}

# verifica si un valor es un número decimal
def numerodecimal(valor):
    if not valor:
        return False
    if valor[0] in '+-':
        valor = valor[1:]
    punto = 0
    for c in valor:
        if c == '.':
            punto += 1
            if punto > 1:
                return False
        elif not c.isdigit():
            return False

    return True if valor and valor != '.' else False
#verificar si el numero  no sea menor a 0 y mayor a 6
def confirmacion(valor):
    if not valor:
        return False
    if valor[0] in '+-':
        signo = valor[0]
        valor = valor[1:]
    else:
        signo = '+'
    if not valor.isdigit():
        return False
    numero = int(valor)
    if signo == '-':
        numero = -numero

    return 0 < numero < 6
# Verifica si un valor es un número entero
def numentero(valor):
    if not valor:
        return False
    if valor[0] in '+-':
        valor = valor[1:]
    return valor.isdigit() and valor != ''
    
    
# verifica respuestas
def respuesta():
    while True:
        respuesta = input("¿Desea continuar? (si/no): ").strip().lower()
        if respuesta in ["si"] or ['no']:
            return respuesta 
        else:
            print("Respuesta no válida. Por favor, ingrese 'si' o 'no'.")
            

def add_product(nombre, precio, cantidad):
        inventario[nombre]={"precio": float(precio), "cantidad" : int(cantidad)}

        print(f"Producto {nombre}, Agregado con exito.")
        
def consultar (nombre):
    if nombre not in inventario:
        print("Este producto no esta en el inventario")
    else:
        precio=inventario[nombre]["precio"]
        cantidad=inventario[nombre]["cantidad"]
        print(f"Producto: {nombre} | Precio: {precio:.2f} | Cantidad: {cantidad}")
        

# Actualizar el precio de un producto existente
def actualizar_precio(nombre, nuevo_precio):
    if nombre not in inventario:
        print("Este producto no esta en el inventario")
    else:
        inventario[nombre]["precio"]=nuevo_precio
        print(f"El precio del producto {nombre} ha sido actualizado a {nuevo_precio:.2f}")
        
#funcion para eliminar un producto
def eliminar(nombre):
    if nombre not in inventario:
        print("Este producto no esta en el inventario")
    else:
        inventario.pop(nombre)
        print(f"El producto {nombre} ha sido eliminado del inventario.")
# Calcular el valor total del inventario
def calcular_valor_total():
    if not inventario:
        print("El inventario está vacío.")
    else:
        valor_total = sum(map(lambda item: item["precio"] * item["cantidad"], inventario.values()))
        print(f"El valor total del inventario es: ${valor_total:.2f}")

# Mostrar menú principal
def mostrar_menu():
    print("\n Sistema de Gestión de Inventario")
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Salir")

# Ejecutar el sistema
def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()
        if confirmacion(opcion) == False:
            print("Error, la opción debe ser un número entre 1 y 6.")
        if opcion == "1":
            while True:
                while True:
                    nombre=input("Ingrese el Nombre del producto :").lower()
                    if nombre not in inventario:
                        print("registrado con exito")
                        break
                    else:
                        print(f"este producto ya esta registrado'{nombre}")
                    
                precio=input("Ingrese el valor del producto :").strip()
                while True:
                    if not numerodecimal (precio) or float(precio) <= 0:
                        print("Error el numero debe de ser un numero decimal positivo.")
                        
                    elif numerodecimal(precio) or float(precio) >=0:
                        print("precio ingresado y registrado con exito")
                        break
                cantidad=input("Ingrese la cantidad de productos: ").strip()
                while True:
                    if not numentero(cantidad) or int (cantidad) <0:
                        print("Error, la cantidad debe de ser un numero entero positivo.")
                        
                    elif numentero(cantidad) or int (cantidad) >0:
                        print("Cantidad ingresada con exito")
                        break
                add_product(nombre, precio, cantidad)
                print(inventario)
                if respuesta()== "no" :
                    break
        
        elif opcion == "2":
            nombre=input("Ingrese el nombre del producto a consultar: ").lower()
            consultar(nombre)
        elif opcion == "3":
            while True:
                nombre=input("Ingrese el nombre del producto a actualizar: ").lower()
                if nombre not in inventario:
                    print("Este producto no esta en el inventario")
                    return
                print(f"Producto: {nombre} | Precio: {inventario[nombre]['precio']:.2f} | Cantidad: {inventario[nombre]['cantidad']}")
                while True:
                    nuevo_precio=float(input("Ingrese el nuevo precio: "))
                    if not numerodecimal(nuevo_precio) or float(nuevo_precio) <= 0:
                        print("Error, el precio debe de ser un numero decimal positivo.")
                        return
                    elif numerodecimal(nuevo_precio) or float(nuevo_precio) >=0:
                        print("precio ingresado y registrado con exito")
                        break
                actualizar_precio(nombre, nuevo_precio)
                if respuesta()== "si" :
                    break
                
        elif opcion == "4":
            while True:
                nombre=input("Ingrese el nombre del producto a eliminar: ").lower()
                if nombre not in inventario:
                    print("Este producto no esta en el inventario")
                    return
                print(f"El producto {nombre} ha sido eliminado del inventario.")
                eliminar(nombre) 
                if respuesta()== "si" :   
                    break
        elif opcion == "5":
            calcular_valor_total()
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
    
ejecutar()
