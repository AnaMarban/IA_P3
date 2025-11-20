
from typing import List


def _counting_sort_by_digit(arr: List[int], exp: int) -> List[int]:
	"""Counting sort estable por el dígito correspondiente a `exp` (10^i).

	Args:
		arr: lista de enteros no negativos.
		exp: 1, 10, 100, ... indicando el dígito a usar.

	Returns:
		Nueva lista ordenada de forma estable por ese dígito.
	"""
	n = len(arr)
	out = [0] * n
	count = [0] * 10

	# Contar ocurrencias del dígito
	for num in arr:
		index = (num // exp) % 10
		count[index] += 1

	# Convertir a posiciones acumuladas
	for i in range(1, 10):
		count[i] += count[i - 1]

	# Construir salida (recorrer en reversa para estabilidad)
	for i in range(n - 1, -1, -1):
		num = arr[i]
		index = (num // exp) % 10
		count[index] -= 1
		out[count[index]] = num

	return out


def _radix_sort_non_negative(arr: List[int]) -> List[int]:
	"""Radix sort (LSD) para una lista de enteros no negativos. Devuelve nueva lista."""
	if not arr:
		return []
	# Encontrar el máximo para saber cuántos dígitos
	max_val = max(arr)
	exp = 1
	salida = list(arr)
	while max_val // exp > 0:
		salida = _counting_sort_by_digit(salida, exp)
		exp *= 10
	return salida


def radix_sort(arr: List[int]) -> List[int]:
	"""Ordena la lista de enteros `arr` (puede contener negativos) y devuelve
	una nueva lista ordenada.

	Estrategia:
	  - separar `negativos` y `positivos`
	  - aplicar radix sort a los absolutos de `negativos` y a `positivos`
	  - reconstruir: los negativos deben quedar en orden ascendente (por eso
		invertimos el orden de los absolutos ordenados y los hacemos negativos)
	"""
	if not arr:
		return []

	positivos = [x for x in arr if x >= 0]
	negativos = [-x for x in arr if x < 0]  # trabajamos con valores absolutos

	sorted_pos = _radix_sort_non_negative(positivos)
	sorted_neg_abs = _radix_sort_non_negative(negativos)

	# Reconstruir negativos: los absolutos ordenados asc; para negativos los queremos
	# en orden ascendente (p. ej. -5, -3, -1) — obtenemos eso invirtiendo los absolutos
	# ordenados y negándolos.
	sorted_neg = [ -x for x in reversed(sorted_neg_abs) ]

	return sorted_neg + sorted_pos


if __name__ == '__main__':
	casos = [
		([], []),
		([1], [1]),
		([1, 2, 3, 4], [1, 2, 3, 4]),
		([4, 3, 2, 1], [1, 2, 3, 4]),
		([3, 1, 2, 1], [1, 1, 2, 3]),
		([5, -1, 3, 0, 2], [-1, 0, 2, 3, 5]),
		([-5, -10, -3, -1], [-10, -5, -3, -1]),
		([170,45,75,90,802,24,2,66], [2,24,45,66,75,90,170,802]),
	]

	all_ok = True
	for entrada, esperado in casos:
		resultado = radix_sort(list(entrada))
		ok = resultado == esperado
		print(f'entrada: {entrada} -> resultado: {resultado} | esperado: {esperado} | OK: {ok}')
		all_ok = all_ok and ok

	if all_ok:
		print('\nTodas las pruebas pasaron.')
	else:
		print('\nAlgunas pruebas fallaron.')

