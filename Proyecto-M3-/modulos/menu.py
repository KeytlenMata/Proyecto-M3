from modulos import utilidades 
from modulos import matematicas
from modulos import cuento


def menuPrincipal():
    while True:
        print("\nProyecto 1 del Módulo 3")
        print("GRUPO A")

        utilidades.saludar()
        print(f"Hoy es: {utilidades.obtener_fecha_actual()}" )

        print("\nMENÚ DE OPCIONES")
        print("1. Cuento")
        print("2. Función Matemáticas")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                cuento.imprimir_cuento()
            case "2":
                matematicas.suma()
                matematicas.factorial()
            case "3":
                utilidades.despedida()
                utilidades.pausar_programa()
                break
            case _:
                print("Opción Invalida")
