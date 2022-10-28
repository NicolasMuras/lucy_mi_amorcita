import os
import sys

from administracion import Administracion
from carrito import Carrito
from catalogo import Catalogo
from tarjetas import SistemaTarjetas


"""
    Lo mejor para entender que hace cada cosa, es ir a la nota que voy a dejar en cada funcion.

    Todas las funciones:
    - Reciben parametros. (Entrada)
    - Hacen algo           (Procesamiento)

    Y algunas, pero no todas, nos retornan valores.
    - Devuelven resultado. (Salida)

    Sin embargo, agrege algunas notas aqui, a modo de orientacion general.
"""

"""
Aca se inicializan objetos utilizados por el sistema.
El objetivo es poder acceder a estos objetos desde los modulos.
"""
catalogo = Catalogo() # Se inicializa el objeto catalogo.
sistema_tarjetas = SistemaTarjetas() # Se inicializa el sistema de tarjetas.
administracion = Administracion(sistema_tarjetas) # Se inicializa el sistema de administracion.
carrito = Carrito() # Se inicializa el carrito.


def modulo_productos_y_promociones():
    os.system('clear') # De nuevo, se limpia la consola cada vez que se ingresa a un nuevo modulo.

    def print_menu():
        print("------------------------------ PRODUCTOS Y PROMOCIONES -----------------------------\n")
        print("[1] Agregar producto al catalogo\n")
        print("[2] Agregar promocion\n")
        print("[3] Listar productos\n")
        print("[4] Listar promociones\n")
        print("[5] Volver\n")
        print("------------------------------------------------------------------------------------\n")
    print_menu()
    opcion = input("Elige una opcion: ")

    while opcion != '5':
        
        if opcion == '1':
            print("\n[*] Agregar producto: \n\n")
            nombre = input("Nombre: ")
            precio = input("Precio: ")
            catalogo.agregar_producto(nombre, precio)                   # Accedemos a la funcion "agregar_producto" de nuestro catalogo.
            print("\n[+] Producto agregado con exito.\n")

        if opcion == '2':
            print("\n[*] Agregar promocion: \n\n")
            nombre = input("Nombre: ")
            promocion = input("Promocion: ")
            validacion = catalogo.agregar_promocion(nombre, promocion)  # Accedemos a la funcion "agregar_promocion" de nuestro catalogo.
            if validacion == "[ERROR] El producto no existe.":          # Si la funcion "agregar_promocion" devuelve este error, entonces hacemos print del error.
                print("\n[ERROR] El producto no existe.\n")
            else:                                                       # Si todo va bien, entonces imprimimos el mensaje de que la promocion fue agregada con exito.
                print("\n[+] Promocion agregada con exito.\n")

        if opcion == '3':
            catalogo.listar_productos()

        if opcion == '4':
            catalogo.listar_promociones()
    
        # Al final del ciclo, volvemos a imprimir el menu y le solicitamos al usuario elegir una opcion.
        print_menu() 
        opcion = input("Elige una opcion: ")

    os.system('clear')

def modulo_compra():
    os.system('clear')

    def print_menu():
        print("-------------------------------------- COMPRA --------------------------------------\n")
        print("[1] Agregar producto al carrito\n")
        print("[2] Quitar producto del carrito\n")
        print("[3] Identificar cliente y cobrar\n")
        print("[4] Listar objetos en el carrito\n")
        print("[5] Volver\n")
        print("------------------------------------------------------------------------------------\n")

    print_menu()
    opcion = input("Elige una opcion: ")

    while opcion != '5':
        
        if opcion == '1':
            print("\n[*] Agregar producto al carrito: \n\n")
            nombre = input("Nombre: ")
            validacion = carrito.agregar_al_carro(nombre, catalogo)
            if validacion == "[ERROR] El producto no esta en el catalogo.":
                print("[ERROR] El producto no esta en el catalogo.")
            else:
                print("\n[+] Producto agregado con exito.\n")

        if opcion == '2':
            print("\n[*] Quitar producto del carrito: \n\n")
            nombre = input("Nombre: ")
            validacion = carrito.quitar_del_carro(nombre)
            if validacion == "[ERROR] El producto no esta en el carrito.":
                print("\n[ERROR] El producto no esta en el carrito.\n")
            else:
                print("\n[+] Producto removido con exito.\n")
            

        if opcion == '3':
            print("\n[*] Identificar cliente y cobrar: \n\n")
            dni = input("DNI: ")
            carrito.obtener_precio_final()
            error = administracion.registrar_venta(dni, carrito)
            if error == None:
                carrito.limpieza_post_compra()
                print("\n|  ==============================  |")
                print("|  [+] Compra realizada con exito. |")
                print("|  ==============================  |\n")
            else:
                print("\n" + error + "\n")

        if opcion == '4':
            carrito.listar_objetos_en_el_carrito()

        print_menu()
        opcion = input("Elige una opcion: ")

    os.system('clear')

def modulo_manejo_de_tarjetas_de_credito():
    os.system('clear')

    def print_menu():
        print("-------------------------- MANEJO DE TARJETAS DE CREDITO ---------------------------\n")
        print("[1] Dar de alta cliente\n")
        print("[2] Dar de alta una tarjeta\n")
        print("[3] Dar de alta beneficio para tarjeta\n")
        print("[4] Listar tarjetas de credito\n")
        print("[5] Listar tarjetas de credito con beneficios\n")
        print("[6] Volver\n")
        print("------------------------------------------------------------------------------------\n")
    print_menu()
    opcion = input("Elige una opcion: ")

    while opcion != '6':
        if opcion == '1':
            print("\n[*] Dar de alta cliente: \n")
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            sistema_tarjetas.dar_de_alta_cliente(dni, nombre, apellido)

        if opcion == '2':
            print("\n[*] Dar de alta una tarjeta: \n")
            numero = input("Numero de tarjeta: ")
            dni = input("DNI del titular: ")
            sistema_tarjetas.dar_de_alta_tarjeta(numero, dni)

        if opcion == '3':
            print("\n[*] Dar de alta beneficio para tarjeta: \n")
            numero = input("Numero de tarjeta: ")
            beneficio = input("Beneficio: ")
            sistema_tarjetas.dar_de_alta_beneficios_a_tarjeta(numero, beneficio)

        if opcion == '4':
            sistema_tarjetas.listar_tarjetas_de_credito()

        if opcion == '5':
            sistema_tarjetas.listar_tarjetas_de_credito_con_beneficios()

        print_menu()
        opcion = input("Elige una opcion: ")

    os.system('clear')

def modulo_administrativo():
    os.system('clear')

    def print_menu():
        print("---------------------------------- ADMINISTRACION ----------------------------------\n")
        print("[1] Visualizar el total vendido\n")
        print("[2] Visualizar el total comprado por cliente\n")
        print("[3] Visualizar el total vendido con cada tarjeta\n")
        print("[4] Visualizar el total de descuentos por promociones\n")
        print("[5] Volver\n")
        print("------------------------------------------------------------------------------------\n")
    print_menu()
    opcion = input("Elige una opcion: ")

    while opcion != '5':
        if opcion == '1':
            administracion.imprimir_ventas_totales()

        if opcion == '2':
            administracion.imprimir_ventas_por_cliente()

        if opcion == '3':
            administracion.imprimir_ventas_por_tarjeta()

        if opcion == '4':
            administracion.imprimir_total_descuentos()

        print_menu()
        opcion = input("Elige una opcion: ")

    os.system('clear')

def modulo_salir():
    print("\n[*] Saliste del sistema.")
    sys.exit()

def main():
    """
        Funcion principal del programa, que gestiona el menu principal.
    """
    os.system('clear') # Esto es utilizado para limpiar la consola. (Es lo que hace que cuando entremos a un menu, se borre lo que habia antes)

    def print_menu(): # Es una funcion sencilla, la llamaremos para imprimir el menu principal.
        print("---------------------------------- MENU PRINCIPAL ----------------------------------\n")
        print("[1] Productos y promociones\n")
        print("[2] Compra\n")
        print("[3] Manejo de tarjetas de credito\n")
        print("[4] Administrativo\n")
        print("[5] Salir\n")
        print("------------------------------------------------------------------------------------\n")
    print_menu()
    modulo_seleccionado = input("Elige el modulo a utilizar: ") # Solicitamos al usuario ingresar un modulo.

    while True: # Es un bucle infinito, por lo tanto, el programa solo se cerrara si elegimos el modulo 5 (modulo_salir).
        
        if modulo_seleccionado == '1':
            modulo_productos_y_promociones()
        if modulo_seleccionado == '2':
            modulo_compra()
        if modulo_seleccionado == '3':
            modulo_manejo_de_tarjetas_de_credito()
        if modulo_seleccionado == '4':
            modulo_administrativo()
        if modulo_seleccionado == '5':
            modulo_salir()

        print_menu() # Imprimimos el menu principal.
        modulo_seleccionado = input("Elige el modulo a utilizar: ")

main()