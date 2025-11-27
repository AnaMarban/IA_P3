import heapq

def dijkstra_paso_a_paso(grafo, origen, destino):
    # distancias guarda el costo mínimo conocido hasta cada nodo
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0

    # anterior guarda el "camino": de dónde venimos a cada nodo
    anterior = {nodo: None for nodo in grafo}

    # cola de prioridad: (distancia_actual, nodo_actual)
    cola = [(0, origen)]

    print("=== INICIO DEL ALGORITMO DE DIJKSTRA ===")
    print(f"Nodo origen: {origen}, nodo destino: {destino}")
    print("----------------------------------------")

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        print(f"\n> Visitando nodo: {nodo_actual} con distancia actual: {distancia_actual}")

        # Si ya llegamos al destino, podemos terminar
        if nodo_actual == destino:
            print("\nSe ha alcanzado el nodo destino. Terminando búsqueda...")
            break

        # Si esta distancia ya no es la mejor, la ignoramos
        if distancia_actual > distancias[nodo_actual]:
            print("  Esta entrada está desactualizada, se ignora.")
            continue

        # Revisar vecinos
        for vecino, peso in grafo[nodo_actual]:
            print(f"  Revisando vecino: {vecino} con peso: {peso}")
            nueva_distancia = distancia_actual + peso
            print(f"    Nueva distancia posible a {vecino}: {nueva_distancia}")

            # Si encontramos un camino más corto al vecino, lo actualizamos
            if nueva_distancia < distancias[vecino]:
                print(f"    -> Mejora encontrada! Antes: {distancias[vecino]}, Ahora: {nueva_distancia}")
                distancias[vecino] = nueva_distancia
                anterior[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_distancia, vecino))
            else:
                print(f"    -> No mejora (la mejor distancia actual a {vecino} es {distancias[vecino]})")

    # Reconstruir el camino
    camino = []
    nodo = destino
    if distancias[destino] == float('inf'):
        print("\nNo existe un camino desde", origen, "hasta", destino)
        return

    while nodo is not None:
        camino.append(nodo)
        nodo = anterior[nodo]
    camino.reverse()

    print("\n=== RESULTADO FINAL ===")
    print("Camino más corto:", " -> ".join(camino))
    print("Costo total:", distancias[destino])


# Ejemplo 
grafo_ejemplo = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("C", 1), ("D", 5)],
    "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
    "D": [("B", 5), ("C", 8), ("E", 2)],
    "E": [("C", 10), ("D", 2)]
}

if __name__ == "__main__":
    print("Nodos disponibles en el grafo:", list(grafo_ejemplo.keys()))
    origen = input("Ingresa el nodo origen: ").strip()
    destino = input("Ingresa el nodo destino: ").strip()

    if origen not in grafo_ejemplo or destino not in grafo_ejemplo:
        print("Alguno de los nodos no existe en el grafo.")
    else:
        dijkstra_paso_a_paso(grafo_ejemplo, origen, destino)
