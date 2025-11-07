
from typing import List, TypeVar

T = TypeVar('T')


def _merge(left: List[T], right: List[T]) -> List[T]:
	"""Mezcla dos listas ordenadas `left` y `right` y devuelve la lista resultante."""
	i = j = 0
	out: List[T] = []
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			out.append(left[i])
			i += 1
		else:
			out.append(right[j])
			j += 1
	# Añadir los restos
	if i < len(left):
		out.extend(left[i:])
	if j < len(right):
		out.extend(right[j:])
	return out


def merge_sort(arr: List[T]) -> List[T]:
	"""Ordena `arr` usando Merge Sort y devuelve una nueva lista ordenada.

	Esta función no modifica la lista de entrada.
	"""
	n = len(arr)
	if n <= 1:
		return list(arr)
	mid = n // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return _merge(left, right)


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
		resultado = merge_sort(list(entrada))
		ok = resultado == esperado
		print(f'entrada: {entrada} -> resultado: {resultado} | esperado: {esperado} | OK: {ok}')
		all_ok = all_ok and ok

	if all_ok:
		print('\nTodas las pruebas pasaron.')
	else:
		print('\nAlgunas pruebas fallaron.')

