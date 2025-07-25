import math

def factorial(n, detailed=False):
    """
    Calcula el factorial de un número entero no negativo.
    Lanza ValueError si el número es negativo, no entero o excede un límite superior.
    Si detailed es True, devuelve una cadena con el desarrollo (ej. "5x4x3x2x1").3
    """
    if not isinstance(n, int):
        raise ValueError("Error: El factorial solo está definido para números enteros.")
    if n < 0:
        raise ValueError("Error: El factorial no está definido para números negativos.")
    if n > 170: # Límite para evitar desbordamiento con math.factorial o números irrazonablemente grandes
        raise ValueError("Error: El número es demasiado grande para calcular el factorial.")
    if n == 0:
        if detailed:
            return "1"
        return 1
    
    if detailed:
        # Genera la cadena de la multiplicación: "nx(n-1)x...x1"
        return " x ".join(map(str, range(n, 0, -1)))
    
    return math.factorial(n)

def combinatoria(n, k):
    """
    Calcula la combinatoria "n choose k" (C(n, k)).
    Lanza ValueError si n o k no son enteros no negativos, o si k > n.
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise ValueError("Error: n y k deben ser números enteros para la combinatoria.")
    if n < 0 or k < 0:
        raise ValueError("Error: n y k deben ser números no negativos para la combinatoria.")
    if k > n:
        return 0 # Por definición, C(n, k) = 0 si k > n
    
    try:
        # No llamamos a factorial con detailed=True aquí para el cálculo interno,
        # solo para la visualización en la GUI.
        num_val = factorial(n)
        den_val_k = factorial(k)
        den_val_nk = factorial(n - k)
        return num_val // (den_val_k * den_val_nk)
    except ValueError as e:
        raise ValueError(f"Error al calcular combinatoria: {e}")


def _validate_nk(n, k, operation_name):
    """Función auxiliar para validar n y k para operaciones combinatorias."""
    if not isinstance(n, int) or not isinstance(k, int):
        raise ValueError(f"Error: n y k deben ser números enteros para la {operation_name}.")
    if n < 0 or k < 0:
        raise ValueError(f"Error: n y k deben ser números no negativos para la {operation_name}.")

def permutacion(n, k):
    _validate_nk(n, k, "permutación") # Reutiliza la validación
    if k > n:
        raise ValueError("Error: Para permutación P(n, k), k no puede ser mayor que n.")
    try:
        return math.perm(n, k)
    except ValueError as e:
        
        raise ValueError(f"Error al calcular permutación: {e}") 
if __name__ == "__main__":
    print("Este archivo contiene la lógica matemática de la calculadora.")
    print("Para usar la interfaz gráfica, por favor, ejecuta 'python calculator_gui.py'.")