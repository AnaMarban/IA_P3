
from typing import List, TypeVar

T = TypeVar('T')


def merge_two_sorted(a: List[T], b: List[T]) -> List[T]:
    """Fusiona dos listas ordenadas y devuelve una nueva lista ordenada."""
    i = j = 0
    result: List[T] = []
    
    # Comparar elementos de ambas listas y tomar el menor
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    
    # Agregar elementos restantes
    result.extend(a[i:])
    result.extend(b[j:])
    
    return result


def create_runs(arr: List[T], run_size: int) -> List[List[T]]:
    """Crea runs ordenados de tamaño fijo."""
    runs: List[List[T]] = []
    
    # Dividir la lista en chunks del tamaño especificado
    for i in range(0, len(arr), run_size):
        chunk = list(arr[i:i + run_size])
        chunk.sort()  # Ordenar cada chunk
        runs.append(chunk)
    
    return runs


def fibonacci_distribution(num_runs: int) -> tuple:
    """Calcula distribución de Fibonacci para los runs."""
    # Generar números de Fibonacci
    fib = [1, 1]
    while sum(fib) < num_runs:
        fib.append(fib[-1] + fib[-2])
    
    # Retornar distribución para dos archivos
    if len(fib) >= 2:
        return fib[-2], fib[-1]
    return 1, 1


def distribute_runs(runs: List[List[T]]) -> tuple:
    """Distribuye runs en dos listas usando secuencia de Fibonacci."""
    if not runs:
        return [], []
    
    # Calcular distribución de Fibonacci
    fib_a, fib_b = fibonacci_distribution(len(runs))
    
    # Distribuir runs
    tape_a = runs[:fib_a] if fib_a <= len(runs) else runs[:]
    tape_b = runs[fib_a:fib_a + fib_b] if fib_a < len(runs) else []
    
    return tape_a, tape_b


def polyphase_merge(tape_a: List[List[T]], tape_b: List[List[T]]) -> List[T]:
    """Realiza el merge polyphase de las dos cintas."""
    # Mientras ambas cintas tengan runs
    while tape_a and tape_b:
        # Tomar un run de cada cinta y hacer merge
        run_a = tape_a.pop(0)
        run_b = tape_b.pop(0)
        merged_run = merge_two_sorted(run_a, run_b)
        
        # El run fusionado va a la cinta que tenga menos runs
        if len(tape_a) <= len(tape_b):
            tape_a.append(merged_run)
        else:
            tape_b.append(merged_run)
    
    # Concatenar runs restantes
    result = []
    remaining_runs = tape_a if tape_a else tape_b
    
    for run in remaining_runs:
        result.extend(run)
    
    return result


def polyphase_sort(arr: List[T], run_size: int = 3) -> List[T]:
    """Algoritmo Polyphase Sort simplificado.
    
    Args:
        arr: Lista de elementos a ordenar
        run_size: Tamaño de cada run inicial
        
    Returns:
        Lista ordenada
    """
    if len(arr) <= 1:
        return list(arr)
    
    # Si es pequeño, usar ordenamiento directo
    if len(arr) <= run_size:
        return sorted(arr)
    
    # Paso 1: Crear runs iniciales ordenados
    runs = create_runs(arr, run_size)
    
    # Si solo hay un run, retornarlo
    if len(runs) == 1:
        return runs[0]
    
    # Paso 2: Distribuir runs usando Fibonacci
    tape_a, tape_b = distribute_runs(runs)
    
    # Paso 3: Hacer merge polyphase
    result = polyphase_merge(tape_a, tape_b)
    
    return result


# Ejemplos de uso
if __name__ == "__main__":
    # Ejemplo 1: Lista de números
    print("=== Polyphase Sort - Ejemplo 1 ===")
    numeros = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print(f"Lista original: {numeros}")
    resultado = polyphase_sort(numeros, run_size=3)
    print(f"Lista ordenada: {resultado}")
    print(f"¿Correcto? {resultado == sorted(numeros)}")
    
    # Ejemplo 2: Lista de strings
    print("\n=== Polyphase Sort - Ejemplo 2 ===")
    palabras = ["python", "algoritmo", "ordenamiento", "externo", "fibonacci", "merge"]
    print(f"Lista original: {palabras}")
    resultado2 = polyphase_sort(palabras, run_size=2)
    print(f"Lista ordenada: {resultado2}")
    print(f"¿Correcto? {resultado2 == sorted(palabras)}")
    
    # Ejemplo 3: Demostración paso a paso
    print("\n=== Polyphase Sort - Paso a paso ===")
    datos = [8, 3, 1, 7, 2, 6, 4, 5]
    print(f"1. Datos originales: {datos}")
    
    # Crear runs
    runs = create_runs(datos, 2)
    print(f"2. Runs creados: {runs}")
    
    # Distribución Fibonacci
    fib_a, fib_b = fibonacci_distribution(len(runs))
    print(f"3. Distribución Fibonacci: {fib_a}, {fib_b}")
    
    # Distribuir runs
    tape_a, tape_b = distribute_runs(runs)
    print(f"4. Cinta A: {tape_a}")
    print(f"   Cinta B: {tape_b}")
    
    # Resultado final
    resultado3 = polyphase_sort(datos, run_size=2)
    print(f"5. Resultado final: {resultado3}")
