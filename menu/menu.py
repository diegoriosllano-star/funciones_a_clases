from ejercicios.ejercicio1_taxi import ViajeTaxi
from ejercicios.ejercicio2_cine import CompraBoletos

def mostrarMenu():
    print()
    print("FUNCIONES A CLASES - POO")
    print("1. Viaje en taxi")
    print("2. Venta de boletos de cine")
    print("3. Consumo de combustible")
    print("0. Salir")


def menus():
    opcion = ""

    while opcion != "0":
        mostrarMenu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            viaje = ViajeTaxi()
            viaje.leerKilometros()
            viaje.calcularImporte()
            viaje.mostrarImporte()
        elif opcion == "2":
             compra = CompraBoletos()
             compra.leerCantidad()
             compra.calcularCompra()
             compra.mostrarCompra()
        elif opcion == "3":
            print("Ejercicio 3 pendiente.")
        elif opcion != "0":
            print("Opción no válida.")