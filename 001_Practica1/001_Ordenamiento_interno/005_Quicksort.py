"""Implementación de QuickSort (ordenamiento rápido) in-place.

Se usa partición tipo Lomuto con pivote aleatorio para reducir la probabilidad
de degeneración en entradas casi ordenadas. La función `quick_sort` modifica
la lista en sitio y devuelve la misma lista para conveniencia.

Complejidad promedio: O(n log n). Peor caso: O(n^2) si se eligen pivotes muy
mal (aunque el pivote aleatorio reduce esa probabilidad).
"""

from typing import List, TypeVar
import random

T = TypeVar('T')


def _partition(arr: List[T], lo: int, hi: int) -> int:
	"""Partición Lomuto: usa arr[hi] como pivote; devuelve índice final del pivote."""
	pivot = arr[hi]
	i = lo - 1
	for j in range(lo, hi):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
	return i + 1


def _quick_sort(arr: List[T], lo: int, hi: int) -> None:
	if lo < hi:
		# Elegir pivote aleatorio y colocarlo en hi
		pivot_idx = random.randint(lo, hi)
		arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]
		p = _partition(arr, lo, hi)
		_quick_sort(arr, lo, p - 1)
		_quick_sort(arr, p + 1, hi)


def quick_sort(arr: List[T]) -> List[T]:
	"""Ordena `arr` in-place usando QuickSort y devuelve la misma lista.

	Args:
		arr: Lista de elementos comparables.

	Returns:
		La misma lista `arr`, ordenada.
	"""
	# Para comportamiento determinista en pruebas ocasionales, no fijamos la semilla.
	if len(arr) <= 1:
		return arr
	_quick_sort(arr, 0, len(arr) - 1)
	return arr


if __name__ == '__main__':
	# Pruebas básicas
	casos = [
		([], []),
		([1], [1]),
		([1, 2, 3, 4], [1, 2, 3, 4]),
		([4, 3, 2, 1], [1, 2, 3, 4]),
		([3, 1, 2, 1], [1, 1, 2, 3]),
		([5, -1, 3, 0, 2], [-1, 0, 2, 3, 5]),
	]

	all_ok = True
	for entrada, esperado in casos:
		copia = list(entrada)
		resultado = quick_sort(copia)
		ok = resultado == esperado
		print(f'entrada: {entrada} -> resultado: {resultado} | esperado: {esperado} | OK: {ok}')
		all_ok = all_ok and ok

	if all_ok:
		print('\nTodas las pruebas pasaron.')
	else:
		print('\nAlgunas pruebas fallaron.')

