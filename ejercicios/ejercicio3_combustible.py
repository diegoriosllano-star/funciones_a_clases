# EJERCICIO 3. CONSUMO DE COMBUSTIBLE
# Un conductor necesita conocer el rendimiento de combustible
# de su vehículo y el costo de un recorrido.
# El usuario proporciona la distancia recorrida en kilómetros
# y la cantidad de litros consumidos.
# El precio por litro es de $24.00.


# PROBLEMA
# Calcular el rendimiento de combustible de un vehículo
# y el costo total del combustible consumido.


# ENTRADAS
# distancia : float, kilómetros, valor mayor que 0.
# litros : float, litros consumidos, valor mayor que 0.


# SALIDAS
# distancia : float, kilómetros.
# litros : float, litros consumidos.
# rendimiento : float, kilómetros por litro.
# costo : float, pesos mexicanos.
# El rendimiento y el costo se muestran con dos decimales.


# REGLAS Y SUPUESTOS
# - La distancia debe ser mayor que 0.
# - Los litros consumidos deben ser mayores que 0.
# - El precio por litro de combustible es de $24.00.
# - El rendimiento se calcula como distancia / litros.
# - El costo se calcula como litros * 24.
# - El rendimiento se muestra con dos decimales.
# - El costo se muestra en pesos mexicanos con dos decimales.
# - La única biblioteca externa permitida es tabulate.


# CLASE
# Nombre: ConsumoCombustible
# Responsabilidad: almacenar los datos del recorrido,
# calcular el rendimiento y el costo del combustible,
# y mostrar los resultados.


# ATRIBUTOS
# distancia : float
#   Distancia recorrida en kilómetros. Valor inicial: 0.0.
#
# litros : float
#   Litros consumidos. Valor inicial: 0.0.
#
# rendimiento : float
#   Rendimiento en kilómetros por litro. Valor inicial: 0.0.
#
# costo : float
#   Costo total del combustible. Valor inicial: 0.0.


# CONTRATO DE CLASE
# class ConsumoCombustible:
#
#   __init__(self) -> None:
#       Inicializa distancia=0.0, litros=0.0,
#       rendimiento=0.0 y costo=0.0.
#
#   leerDatos(self) -> None:
#       Solicita la distancia y los litros consumidos
#       y los guarda en self.distancia y self.litros.
#
#   calcularRendimiento(self) -> None:
#       Calcula el rendimiento usando self.distancia
#       y self.litros, y guarda el resultado en self.rendimiento.
#
#   calcularCosto(self) -> None:
#       Calcula el costo usando self.litros
#       y guarda el resultado en self.costo.
#
#   mostrarResultados(self) -> None:
#       Muestra distancia, litros, precio por litro,
#       rendimiento y costo mediante tabulate.


# ALGORITMO
# 1. Desde menu/menu.py crear un objeto ConsumoCombustible.
# 2. Ejecutar leerDatos().
# 3. Ejecutar calcularRendimiento():
#       self.rendimiento = self.distancia / self.litros
#
# 4. Ejecutar calcularCosto():
#       self.costo = self.litros * 24
#
# 5. Ejecutar mostrarResultados().
# 6. Mostrar distancia, litros, precio por litro,
#    rendimiento y costo total.


# CASOS DE PRUEBA
# 120 km, 10 L -> rendimiento 12.00 km/L, costo $240.00
# 250 km, 20 L -> rendimiento 12.50 km/L, costo $480.00
# 180 km, 15 L -> rendimiento 12.00 km/L, costo $360.00
# 300 km, 25 L -> rendimiento 12.00 km/L, costo $600.00


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente la clase ConsumoCombustible.
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


class ConsumoCombustible:
    def __init__(self):
        self.distancia = 0.0
        self.litros = 0.0
        self.rendimiento = 0.0
        self.costo = 0.0

    def leerDatos(self):
        self.distancia = float(input("Ingrese la distancia recorrida en km: "))
        self.litros = float(input("Ingrese los litros consumidos: "))

    def calcularRendimiento(self):
        self.rendimiento = self.distancia / self.litros

    def calcularCosto(self):
        self.costo = self.litros * 24

    def mostrarResultados(self):
        filas = [
            ["Distancia recorrida", f"{self.distancia:.2f} km"],
            ["Litros consumidos", f"{self.litros:.2f} L"],
            ["Precio por litro", "$24.00"],
            ["Rendimiento", f"{self.rendimiento:.2f} km/L"],
            ["Costo total", f"${self.costo:.2f}"]
        ]

        print("Resultado del consumo de combustible:")
        print(tabulate(filas, headers=["Concepto", "Valor"]))