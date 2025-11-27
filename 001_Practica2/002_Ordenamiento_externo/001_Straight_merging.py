

from typing import List, TypeVar

T = TypeVar('T')


def merge_two_sorted(a: List[T], b: List[T]) -> List[T]:
	"""Fusiona dos listas ordenadas y devuelve una nueva lista ordenada (establе)."""
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


def straight_merging(arr: List[T], run_size: int) -> List[T]:
	"""Simula straight merging y devuelve una nueva lista ordenada.

	Args:
		arr: lista de elementos comparables.
		run_size: tamaño (aprox.) de cada run que cabe en memoria.

	Proceso:
	  1. Dividir `arr` en chunks de tamaño `run_size` y ordenar cada chunk -> runs.
	  2. Repetir pasadas: fusionar runs adyacentes por pares hasta que quede 1 run.

	Esta función no modifica `arr`.
	"""
	if run_size <= 0:
		raise ValueError('run_size debe ser >= 1')
	n = len(arr)
	if n <= 1:
		return list(arr)

	# 1) Crear runs ordenados
	runs: List[List[T]] = []
	for i in range(0, n, run_size):
		chunk = list(arr[i:i + run_size])
		chunk.sort()
		runs.append(chunk)

	# 2) Fusionar por pasadas hasta tener un solo run
	pass_num = 0
	while len(runs) > 1:
		pass_num += 1
		new_runs: List[List[T]] = []
		# fusionar runs adyacentes por pares
		for i in range(0, len(runs), 2):
			if i + 1 < len(runs):
				merged = merge_two_sorted(runs[i], runs[i + 1])
				new_runs.append(merged)
			else:
				# si hay una run sobrante, pasa tal cual a la siguiente ronda
				new_runs.append(runs[i])
		runs = new_runs

	return runs[0] if runs else []


if __name__ == '__main__':
	# Pruebas educativas y demostración
	casos = [
		([], 3, []),
		([1], 2, [1]),
		([1, 2, 3, 4], 2, [1, 2, 3, 4]),
		([4, 3, 2, 1], 2, [1, 2, 3, 4]),
		([3, 1, 2, 1], 2, [1, 1, 2, 3]),
		([5, -1, 3, 0, 2], 2, [-1, 0, 2, 3, 5]),
		(list(range(10, 0, -1)), 3, list(range(1, 11))),
	]

	all_ok = True
	for entrada, run_size, esperado in casos:
		resultado = straight_merging(list(entrada), run_size)
		ok = resultado == esperado
		print(f'entrada: {entrada} run_size: {run_size} -> resultado: {resultado} | esperado: {esperado} | OK: {ok}')
		all_ok = all_ok and ok

	if all_ok:
		print('\nTodas las pruebas pasaron.')
	else:
		print('\nAlgunas pruebas fallaron.')

