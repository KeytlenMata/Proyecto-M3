from datetime import datetime


def saludar():
    print("Hola! Buenos dias!")


def despedida():
    print("Nos vemos mañana!")


saludar()
despedida()

# ==========================
# Funciones añadidas por Edgarcia09
# ==========================


def obtener_fecha_actual():
    fecha_actual = datetime.now()
    return fecha_actual.strftime("%d/%m/%Y")


def pausar_programa():
    input("Presiona Enter para continuar...")
