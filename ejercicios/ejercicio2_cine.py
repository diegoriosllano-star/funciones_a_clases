# EJERCICIO 2. VENTA DE BOLETOS DE CINE
# Cada boleto cuesta $75.00.
# Cuando se compran 4 boletos o más, se aplica
# un descuento del 10% sobre el subtotal.


# PROBLEMA
# Calcular el importe de una compra de boletos de cine.


# ENTRADAS
# cantidad : int, boletos, valor mayor que 0.


# SALIDAS
# cantidad : int, cantidad de boletos.
# subtotal : float, pesos mexicanos.
# descuento : float, pesos mexicanos.
# total : float, pesos mexicanos.
# Los importes se muestran con dos decimales.


# REGLAS Y SUPUESTOS
# - Cada boleto cuesta $75.00.
# - La cantidad de boletos debe ser mayor que 0.
# - Si se compran menos de 4 boletos, no hay descuento.
# - Si se compran 4 boletos o más, se aplica 10% de descuento.
# - El descuento se aplica sobre el subtotal.
# - Los importes se muestran con dos decimales.
# - La única biblioteca externa permitida es tabulate.


# CLASE
# Nombre: CompraBoletos
# Responsabilidad: almacenar la cantidad de boletos,
# calcular subtotal, descuento y total, y mostrar la compra.


# ATRIBUTOS
# cantidad : int
#   Cantidad de boletos. Valor inicial: 0.
#
# subtotal : float
#   Subtotal de la compra. Valor inicial: 0.0.
#
# descuento : float
#   Descuento aplicado. Valor inicial: 0.0.
#
# total : float
#   Total final de la compra. Valor inicial: 0.0.


# CONTRATO DE CLASE
# class CompraBoletos:
#
#   __init__(self) -> None:
#       Inicializa cantidad=0, subtotal=0.0,
#       descuento=0.0 y total=0.0.
#
#   leerCantidad(self) -> None:
#       Solicita la cantidad de boletos y la guarda
#       en self.cantidad.
#
#   calcularCompra(self) -> None:
#       Calcula subtotal, descuento y total usando
#       self.cantidad y guarda los resultados
#       en los atributos correspondientes.
#
#   mostrarCompra(self) -> None:
#       Muestra cantidad, precio unitario, subtotal,
#       descuento y total mediante tabulate.


# ALGORITMO
# 1. Desde menu/menu.py crear un objeto CompraBoletos.
# 2. Ejecutar leerCantidad().
# 3. Ejecutar calcularCompra():
#       self.subtotal = self.cantidad * 75
#
#       Si self.cantidad >= 4:
#           self.descuento = self.subtotal * 0.10
#       En caso contrario:
#           self.descuento = 0
#
#       self.total = self.subtotal - self.descuento
#
# 4. Ejecutar mostrarCompra().
# 5. Mostrar cantidad, precio unitario, subtotal,
#    descuento y total.


# CASOS DE PRUEBA
# 1 boleto  -> subtotal $75.00, descuento $0.00, total $75.00
# 3 boletos -> subtotal $225.00, descuento $0.00, total $225.00
# 4 boletos -> subtotal $300.00, descuento $30.00, total $270.00
# 6 boletos -> subtotal $450.00, descuento $45.00, total $405.00


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente la clase CompraBoletos.
# - Usa los atributos y métodos del contrato.
# - Inicializa todos los atributos en __init__.
# - Utiliza self para acceder a los atributos.
# - No agregues funciones auxiliares ni otras clases.
# - No agregues validaciones, mensajes ni cálculos
#   que no estén especificados.
# - No crees ni uses objetos en este archivo.
# - El objeto se crea y ejecuta desde menu/menu.py.
# - La única biblioteca externa permitida es tabulate.


# Implementa la clase según esta especificación.

from tabulate import tabulate


class CompraBoletos:
    def __init__(self):
        self.cantidad = 0
        self.subtotal = 0.0
        self.descuento = 0.0
        self.total = 0.0

    def leerCantidad(self):
        self.cantidad = int(input("Ingrese la cantidad de boletos: "))

    def calcularCompra(self):
        self.subtotal = self.cantidad * 75

        if self.cantidad >= 4:
            self.descuento = self.subtotal * 0.10
        else:
            self.descuento = 0

        self.total = self.subtotal - self.descuento

    def mostrarCompra(self):
        filas = [
            ["Cantidad de boletos", self.cantidad],
            ["Precio unitario", "$75.00"],
            ["Subtotal", f"${self.subtotal:.2f}"],
            ["Descuento", f"${self.descuento:.2f}"],
            ["Total a pagar", f"${self.total:.2f}"]
        ]

        print("Resultado de la compra de boletos:")
        print(tabulate(filas, headers=["Concepto", "Valor"]))