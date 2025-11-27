
from typing import List, TypeVar

T = TypeVar('T')


def insertion_sort(arr: List[T]) -> List[T]:
	"""Ordena la lista `arr` usando el método de inserción y devuelve la misma lista.

	La función modifica `arr` en sitio (in-place).

	Args:
		arr: Lista de elementos comparables (por ejemplo, int, float, str).

	Returns:
		La lista ordenada (la misma instancia `arr`, ordenada).

	Ejemplo:
		>>> insertion_sort([3,1,2])
		[1, 2, 3]
	"""
	# Recorremos desde el segundo elemento hasta el final
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		# Mover los elementos mayores que key una posición a la derecha
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
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
		copia = list(entrada)  # trabajar sobre una copia para no mutar los casos
		resultado = insertion_sort(copia)
		ok = resultado == esperado
		print(f'entrada: {entrada} -> resultado: {resultado} | esperado: {esperado} | OK: {ok}')
		all_ok = all_ok and ok

	if all_ok:
		print('\nTodas las pruebas pasaron.')
	else:
		print('\nAlgunas pruebas fallaron.')

