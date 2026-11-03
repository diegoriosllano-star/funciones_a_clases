# EJERCICIO 1. VIAJE EN TAXI
# Un taxi cobra $35 de banderazo y $9 por kilómetro recorrido.
# Los viajes de más de 20 km tienen 10% de descuento.
# Se necesita mostrar el importe del viaje.


# PROBLEMA
# Calcular el importe de un viaje en taxi según los kilómetros recorridos.


# ENTRADAS
# kilometros : float, kilómetros recorridos, valor mayor o igual a 0.


# SALIDAS
# kilometros : float, kilómetros recorridos.
# importe : float, pesos mexicanos, mostrado con dos decimales.


# REGLAS Y SUPUESTOS
# - El banderazo cuesta $35.00.
# - Cada kilómetro recorrido cuesta $9.00.
# - Si el viaje es de más de 20 km, se aplica 10% de descuento.
# - Con exactamente 20 km no se aplica descuento.
# - El importe se muestra con dos decimales.
# - La única biblioteca externa permitida es tabulate.


# CLASE
# Nombre: ViajeTaxi
# Responsabilidad: almacenar los kilómetros recorridos,
# calcular el importe del viaje y mostrar el resultado.


# ATRIBUTOS
# kilometros : float
#   Kilómetros recorridos. Valor inicial: 0.0.
#
# importe : float
#   Importe calculado del viaje. Valor inicial: 0.0.


# CONTRATO DE CLASE
# class ViajeTaxi:
#
#   __init__(self) -> None:
#       Inicializa kilometros=0.0 e importe=0.0.
#
#   leerKilometros(self) -> None:
#       Solicita los kilómetros recorridos y los guarda
#       en self.kilometros.
#
#   calcularImporte(self) -> None:
#       Calcula el importe usando self.kilometros
#       y guarda el resultado en self.importe.
#
#   mostrarImporte(self) -> None:
#       Muestra self.kilometros y self.importe
#       mediante tabulate con dos decimales.


# ALGORITMO
# 1. Desde menu/menu.py crear un objeto ViajeTaxi.
# 2. Ejecutar leerKilometros().
# 3. Ejecutar calcularImporte():
#       self.importe = 35 + (self.kilometros * 9)
#
#       Si self.kilometros > 20:
#           descuento = self.importe * 0.10
#           self.importe = self.importe - descuento
#
# 4. Ejecutar mostrarImporte().
# 5. Mostrar los kilómetros y el importe final.


# CASOS DE PRUEBA
# 5 km  -> $80.00
# 20 km -> $215.00
# 21 km -> $201.60
# 30 km -> $274.50


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente la clase ViajeTaxi.
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


class ViajeTaxi:
    def __init__(self):
        self.kilometros = 0.0
        self.importe = 0.0

    def leerKilometros(self):
        self.kilometros = float(input("Ingrese los kilómetros recorridos: "))

    def calcularImporte(self):
        self.importe = 35 + (self.kilometros * 9)

        if self.kilometros > 20:
            descuento = self.importe * 0.10
            self.importe = self.importe - descuento

    def mostrarImporte(self):
        filas = [
            ["Kilómetros recorridos", f"{self.kilometros:.2f} km"],
            ["Importe del viaje", f"${self.importe:.2f}"]
        ]

        print("Resultado del viaje en taxi:")
        print(tabulate(filas, headers=["Concepto", "Valor"]))