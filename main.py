import sys

def mostrar_menu():
    print("\n--- Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("0. Salir")

def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ").strip()
    while True:
        cantidad = input("Ingrese la cantidad: ")
        if cantidad.isdigit():
            if nombre in inventario:
                inventario[nombre] += int(cantidad)
            else:
                inventario[nombre] = int(cantidad)
            print("Producto agregado exitosamente.")
            break
        else:
            print("Cantidad no válida. Ingrese un número entero.")

def eliminar_producto(inventario):
    #El método .strip() elimina los espacios en blanco al inicio y al final de una cadena.
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado correctamente.")
    else:
        print("El producto no existe en el inventario.")

def mostrar_inventario(inventario):
    #devuelve true si el diccionario tiene elementos
    if inventario:
        print("\n--- Inventario ---")
        for producto, cantidad in inventario.items():
            print(f"{producto}: {cantidad}")
    else:
        print("El inventario está vacío.")

def main():
    inventario = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                agregar_producto(inventario)
            case "2":
                eliminar_producto(inventario)
            case "3":
                mostrar_inventario(inventario)
            case "0":
                print("Saliendo del programa...")
                sys.exit(0)
            case _:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
