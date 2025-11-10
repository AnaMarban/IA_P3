

from typing import List, TypeVar
import heapq

T = TypeVar('T')


def merge_two_sorted(a: List[T], b: List[T]) -> List[T]:
    """Fusiona dos listas ordenadas."""
    i = j = 0
    result: List[T] = []
    
    # Comparar elementos y tomar el menor
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


def create_runs_replacement_selection(arr: List[T], memory_size: int) -> List[List[T]]:
    """Crea runs usando selección por reemplazo."""
    if not arr:
        return []
    
    runs: List[List[T]] = []
    i = 0
    
    while i < len(arr):
        # Llenar heap con elementos de memoria
        heap = []
        for _ in range(min(memory_size, len(arr) - i)):
            heapq.heappush(heap, arr[i])
            i += 1
        
        # Crear run actual
        current_run = []
        last_output = None
        
        # Procesar heap
        while heap:
            smallest = heapq.heappop(heap)
            
            # Si es mayor al último output, agregarlo al run
            if last_output is None or smallest >= last_output:
                current_run.append(smallest)
                last_output = smallest
            else:
                # Terminar run actual y empezar nuevo
                if current_run:
                    runs.append(current_run)
                current_run = [smallest]
                last_output = smallest
            
            # Agregar siguiente elemento si hay
            if i < len(arr):
                heapq.heappush(heap, arr[i])
                i += 1
        
        # Agregar último run
        if current_run:
            runs.append(current_run)
    
    return runs


def distribution_initial_runs(arr: List[T], memory_size: int = 3) -> List[T]:
    """Algoritmo de distribución de runs iniciales.
    
    Args:
        arr: Lista a ordenar
        memory_size: Tamaño de memoria disponible
        
    Returns:
        Lista ordenada
    """
    if len(arr) <= 1:
        return list(arr)
    
    # Crear runs con selección por reemplazo
    runs = create_runs_replacement_selection(arr, memory_size)
    
    # Fusionar runs hasta obtener resultado final
    while len(runs) > 1:
        new_runs = []
        # Fusionar pares de runs
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                merged = merge_two_sorted(runs[i], runs[i + 1])
                new_runs.append(merged)
            else:
                new_runs.append(runs[i])
        runs = new_runs
    
    return runs[0] if runs else []


# Ejemplos de uso
if __name__ == "__main__":
    # Ejemplo 1: Lista básica
    print("=== Distribution of Initial Runs ===")
    numeros = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"Lista original: {numeros}")
    resultado = distribution_initial_runs(numeros, memory_size=3)
    print(f"Lista ordenada: {resultado}")
    print(f"¿Correcto? {resultado == sorted(numeros)}")
    
    # Ejemplo 2: Mostrar ventaja con datos parcialmente ordenados
    print("\n=== Ejemplo con datos parcialmente ordenados ===")
    datos = [1, 3, 5, 2, 4, 6, 8, 7, 9]
    print(f"Datos: {datos}")
    runs = create_runs_replacement_selection(datos, memory_size=3)
    print(f"Runs creados: {runs}")
    print(f"Longitudes: {[len(run) for run in runs]}")
    
    resultado2 = distribution_initial_runs(datos, memory_size=3)
    print(f"Resultado final: {resultado2}")
