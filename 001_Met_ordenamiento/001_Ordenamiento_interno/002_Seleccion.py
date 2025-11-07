
from typing import List, TypeVar

T = TypeVar('T')


def selection_sort(arr: List[T]) -> List[T]:
	"""Ordena la lista `arr` usando el método de selección y devuelve la misma lista.

	La función modifica `arr` en sitio (in-place).

	Args:
		arr: Lista de elementos comparables (por ejemplo, int, float, str).

	Returns:
		La lista ordenada (la misma instancia `arr`, ordenada).
	"""
	n = len(arr)
	for i in range(n - 1):
		# Encontrar el índice del mínimo elemento en arr[i:]
		min_idx = i
		for j in range(i + 1, n):
			if arr[j] < arr[min_idx]:
				min_idx = j
		# Intercambiar si min_idx cambió
		if min_idx != i:
			arr[i], arr[min_idx] = arr[min_idx], arr[i]
	return arr


if __name__ == '__main__':
	# Pruebas básicas y demostración rápida
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
		resultado = selection_sort(copia)
		ok = resultado == esperado
		print(f'entrada: {entrada} -> resultado: {resultado} | esperado: {esperado} | OK: {ok}')
		all_ok = all_ok and ok

	if all_ok:
		print('\nTodas las pruebas pasaron.')
	else:
		print('\nAlgunas pruebas fallaron.')

