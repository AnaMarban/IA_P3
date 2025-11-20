

from typing import List, TypeVar

T = TypeVar('T')


def merge_two_sorted(a: List[T], b: List[T]) -> List[T]:
	"""Fusiona dos listas ordenadas y devuelve una nueva lista ordenada (estable)."""
	i = j = 0
	out: List[T] = []
	while i < len(a) and j < len(b):
		if a[i] <= b[j]:
			out.append(a[i])
			i += 1
		else:
			out.append(b[j])
			j += 1
	if i < len(a):
		out.extend(a[i:])
	if j < len(b):
		out.extend(b[j:])
	return out


def find_natural_runs(arr: List[T]) -> List[List[T]]:
	"""Encuentra runs naturales (no-decrecientes) en `arr`.

	Devuelve una lista de listas, cada una es un run ya ordenado.
	"""
	runs: List[List[T]] = []
	n = len(arr)
	if n == 0:
		return runs

	start = 0
	for i in range(1, n):
		# si la secuencia se rompe (disminuye), cerramos el run anterior
		if arr[i] < arr[i - 1]:
			runs.append(list(arr[start:i]))
			start = i
	# añadir último run
	runs.append(list(arr[start:n]))
	return runs


def natural_merging(arr: List[T]) -> List[T]:
	"""Realiza Natural Merging sobre `arr` y devuelve una nueva lista ordenada.

	Proceso:
	  1. Detectar runs naturales en la entrada.
	  2. Repetir pasadas: fusionar runs adyacentes por pares hasta quedar uno.
	"""
	n = len(arr)
	if n <= 1:
		return list(arr)

	runs = find_natural_runs(arr)

	# Si ya está ordenada (único run), devolver copia
	if len(runs) <= 1:
		return list(runs[0]) if runs else []

	# Fusionar por pasadas hasta que haya un único run
	while len(runs) > 1:
		new_runs: List[List[T]] = []
		for i in range(0, len(runs), 2):
			if i + 1 < len(runs):
				merged = merge_two_sorted(runs[i], runs[i + 1])
				new_runs.append(merged)
			else:
				new_runs.append(runs[i])
		runs = new_runs

	return runs[0]


if __name__ == '__main__':
	# Pruebas rápidas
	casos = [
		([], []),
		([1], [1]),
		([1, 2, 3, 4], [1, 2, 3, 4]),
		([4, 3, 2, 1], [1, 2, 3, 4]),
		([3, 1, 2, 1], [1, 1, 2, 3]),
		([5, -1, 3, 0, 2], [-1, 0, 2, 3, 5]),
		([-5, -2, -3, -1, 0], [-5, -3, -2, -1, 0]),
	]

	all_ok = True
	for entrada, esperado in casos:
		resultado = natural_merging(list(entrada))
		ok = resultado == esperado
		print(f'entrada: {entrada} -> resultado: {resultado} | esperado: {esperado} | OK: {ok}')
		all_ok = all_ok and ok

	if all_ok:
		print('\nTodas las pruebas pasaron.')
	else:
		print('\nAlgunas pruebas fallaron.')

