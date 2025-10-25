from modulos import utilidades 
from modulos import matematicas
from modulos import cuento


def menuPrincipal():
    while True:
        print("\nProyecto 1 del Módulo 3")
        print("GRUPO A")

        utilidades.saludar()
        print(f"Hoy es: {utilidades.obtener_fecha_actual()}")

        print("\nMENÚ DE OPCIONES")
        print("1. Cuento")
        print("2. Función Matemáticas")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                cuento.imprimir_cuento()
            case "2":
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                resultado_suma = matematicas.sumar(a, b)
                print(f"La suma de {a} + {b} es: {resultado_suma}")

                n = int(input("Ingresa un número entero no negativo para calcular su factorial: "))
                try:
                    resultado_factorial = matematicas.factorial(n)
                    print(f"El factorial de {n} es: {resultado_factorial}")
                except ValueError as e:
                    print(f"Error: {e}")
            case "3":
                utilidades.despedida()
                utilidades.pausar_programa()
                break
            case _:
                print("Opción Invalida")
