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
 # Calcular el valor total del inventario:
 #    El programa debe calcular el valor total de los productos en inventario y mostrarlo al usuario
#   Para ello, utilizarás una función anónima (lambda) que facilite este cálculo.
#Tu programa debe diseñarse modularmente, con funciones bien definidas que gestionen cada operación mencionada. Además, debes almacenar los productos en un diccionario, donde el nombre del producto sea la clave, y el precio y la cantidad sean los valores asociados, almacenados en una tupla.
#El flujo del programa debe ser interactivo, permitiendo que el usuario escoja qué operación desea realizar. Además, asegúrate de manejar posibles errores, como la búsqueda de productos que no existen o intentos de añadir productos con datos inválidos.
#Finalmente, el código debe ser legible, bien estructurado y comentado. No olvides probar exhaustivamente tu solución con distintos escenarios para asegurar que funciona correctamente en todo tipo de casos. 

#funciones

#funcion menu interactivo
def menu():
    print("Bienvenido a shoppe")
    print("que deseas realizar?" , "escoge el numero de la opcion que deseas hacer")  
    print ("\n1.Añadir productos" )
    print("\n2.Consultar productos") 
    print("\n3.Actualizar productos")
    print("\n4.Eliminar productos")
    print("\n5.Calcular valor total ")
    print("\n6. Salir")
    opciones=(input("Ingresa el numero de la opcion que deseas realizar"))
    match opciones:
        case "1":
            anadir_producto()
                      
inventario={}

#validar el si el numero es entero
def numentero(valor):           
    return valor.isdigit()


#validar si el numero es decimal
def numerodecimal(valor):
    if valor.count()==1:
        entero, decimal = valor.split()
        return entero.isdigit() and decimal.isdigit()
    return False

def anadir_producto():
    nombre=input("Ingresa el nombre del producto: ").lower()
    if not nombre in inventario:
        print("registrado con exito")
    else:
        print(f"este producto ya esta registrado'{nombre}")
        return
    precio=input("ingresa el precio del producto: ").strip()
    while True:
        if not numerodecimal (precio) or float(precio) <= 0:
            print(f"Error el numero debe de ser un numero decimal positivo.")
            return
        elif numerodecimal(precio) or float(precio) >=0:
            print("precio ingresado y registrado con exito")
            break
    cantidad=(input("ingresa la cantidad del producto")).strip()
    while True:
        if not numentero(cantidad) or int (cantidad) <0:
            print("Error, la cantidad debe de ser un numero entero positivo.")
            return
        elif numentero(cantidad) or int (cantidad) >0:
            print("Cantidad ingresada con exito")
            break
        inventario[nombre]={"precio": float(precio), "cantidad" : int(cantidad)}
        print(f"Producto {nombre}, Agregado con exito.")
        menu()
        
def consultar ():
    nombre=input("ingresa el nombre del producto que deseas consultar: ").lower()
    if not nombre in inventario:
        print("Este producto no esta en el inventario")
