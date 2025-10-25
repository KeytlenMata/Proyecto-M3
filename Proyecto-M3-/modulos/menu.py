from modulos import utilidades 
from modulos import matematicas
from modulos import cuento


def menuPrincipal():
    while True:
        # === ENCABEZADO ===
        print("\n" + "="*50)
        print("Proyecto 1 del Módulo 3".center(50))
        print("GRUPO A".center(50))
        print("="*50)

        utilidades.saludar()
        print(f"Hoy es: {utilidades.obtener_fecha_actual()}")

        # === MENÚ DE OPCIONES ===
        print("\n" + "-"*50)
        print("MENÚ DE OPCIONES".center(50))
        print("-"*50)
        print("1. Cuento")
        print("2. Función Matemáticas")
        print("3. Salir")
        print("-"*50)
        
        opcion = input("\nSelecciona una opción: ").strip()

        match opcion:
            case "1":
                print("\n" + ">"*20 + " CUENTO " + "<"*20)
                cuento.imprimir_cuento()
                utilidades.pausar_programa()
            case "2":
                print("\n" + ">"*15 + " OPERACIONES MATEMÁTICAS " + "<"*15)
                try:
                    a = float(input("Ingresa el primer número: "))
                    b = float(input("Ingresa el segundo número: "))
                    resultado_suma = matematicas.sumar(a, b)
                    print(f"\nLa suma de {a} + {b} es: {resultado_suma}")
                except ValueError:
                    print("Error: Por favor ingresa números válidos.")
                    utilidades.pausar_programa()
                    continue

                try:
                    n = int(input("\nIngresa un número entero no negativo para calcular su factorial: "))
                    resultado_factorial = matematicas.factorial(n)
                    print(f"El factorial de {n} es: {resultado_factorial}")
                except ValueError as e:
                    print(f"Error: {e}")
                
                utilidades.pausar_programa()
            case "3":
                print("\n" + "="*50)
                utilidades.despedida()
                utilidades.pausar_programa()
                break
            case _:
                print("\nOpción inválida. Por favor, selecciona 1, 2 o 3.")
                utilidades.pausar_programa()
