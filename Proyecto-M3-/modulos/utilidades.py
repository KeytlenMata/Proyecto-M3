from datetime import datetime

def saludar():
    print("Hola! Buenos dias!")

def obtener_fecha_actual():
    fecha_actual = datetime.now()
    return fecha_actual.strftime("%d/%m/%Y")

def pausar_programa():
    input("Presiona Enter para continuar...")

def despedida():
    print("Nos vemos mañana!")
