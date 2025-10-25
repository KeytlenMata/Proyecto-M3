# def suma():# matematicas.py

def sumar(a, b):
    """
    Suma dos números y devuelve el resultado.
    
    Parámetros:
    a (int o float): Primer número
    b (int o float): Segundo número
    
    Retorna:
    int o float: La suma de a y b
    """
    return a + b

#def factorial():
def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.
    
    Parámetros:
    n (int): Número entero no negativo
    
    Retorna:
    int: Factorial de n
    
    Lanza ValueError si n es negativo.
    """
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


