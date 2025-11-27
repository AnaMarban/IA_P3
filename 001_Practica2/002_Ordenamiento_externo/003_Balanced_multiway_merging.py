

from typing import List, TypeVar
import heapq

T = TypeVar('T')


def _create_runs(arr: List[T], run_size: int) -> List[List[T]]:
	runs: List[List[T]] = []
	for i in range(0, len(arr), run_size):
		chunk = list(arr[i:i + run_size])
		chunk.sort()
		runs.append(chunk)
	return runs


def balanced_multiway_merging(arr: List[T], run_size: int, num_ways: int) -> List[T]:
	"""Simula Balanced Multiway Merging y devuelve una nueva lista ordenada.

	Args:
		arr: lista de elementos comparables.
		run_size: tamaño aproximado de cada run (lo que cabe en memoria).
		num_ways: cuántas runs fusionar en cada operación de mezcla (>=2).

	Proceso:
	  1. Crear runs ordenados de tamaño `run_size`.
	  2. Repetir pasadas: fusionar en grupos de `num_ways` usando una mezcla k-way
		 (aquí usamos `heapq.merge`) hasta que quede un único run.
	"""
	if run_size <= 0:
		raise ValueError('run_size debe ser >= 1')
	if num_ways < 2:
		raise ValueError('num_ways debe ser >= 2')

	n = len(arr)
	if n <= 1:
		return list(arr)

	runs = _create_runs(arr, run_size)

	# Si ya está en un único run
	if len(runs) <= 1:
		return list(runs[0]) if runs else []

	pass_num = 0
	while len(runs) > 1:
		pass_num += 1
		new_runs: List[List[T]] = []
		# fusionar grupos de num_ways runs
		for i in range(0, len(runs), num_ways):
			group = runs[i:i + num_ways]
			if len(group) == 1:
				new_runs.append(group[0])
			else:
				# heapq.merge devuelve un iterador que hace un merge k-way estable
				merged = list(heapq.merge(*group))
				new_runs.append(merged)
		runs = new_runs

	return runs[0]


if __name__ == '__main__':
	# Pruebas rápidas
	casos = [
		([], 3, 3, []),
		([1], 2, 3, [1]),
		([1, 2, 3, 4], 2, 2, [1, 2, 3, 4]),
		([4, 3, 2, 1], 2, 3, [1, 2, 3, 4]),
		([3, 1, 2, 1], 2, 3, [1, 1, 2, 3]),
		([5, -1, 3, 0, 2], 2, 3, [-1, 0, 2, 3, 5]),
		(list(range(10, 0, -1)), 3, 3, list(range(1, 11))),
	]

	all_ok = True
	for entrada, run_size, num_ways, esperado in casos:
		resultado = balanced_multiway_merging(list(entrada), run_size, num_ways)
		ok = resultado == esperado
		print(f'entrada: {entrada} run_size: {run_size} num_ways: {num_ways} -> resultado: {resultado} | esperado: {esperado} | OK: {ok}')
		all_ok = all_ok and ok

	if all_ok:
		print('\nTodas las pruebas pasaron.')
	else:
		print('\nAlgunas pruebas fallaron.')

