import heapq   # Uso heapq porque me sirve como cola de priorida
               # Básicamente saca la arista más barata sin tener que ordenarlas a mano

def prim_paso_a_paso(grafo, inicio):

    # Aquí se guardan los nodos ya forman parte del árbol
    visitados = set()

    # Lista donde se van guardando las aristas que realmente entran al Árbol Parcial Mínimo
    aristas_mst = []

    # Para llevar la suma de los costos 
    costo_total = 0

    # Cola de prioridad donde meto las aristas posibles. Cada entrada será:
    # (peso, desde, hacia)
    cola = []

    print("=== ALGORITMO DE PRIM (Árbol Parcial Mínimo) ===")
    print(f"Nodo inicial: {inicio}")
    print("-----------------------------------------------")

    # Agrego mi nodo inicial al conjunto de visitados
    visitados.add(inicio)

    # Todas las aristas que salen del nodo inicial las pongo en la cola
    # Así empiezo a tener opciones para expandir el árbol
    for vecino, peso in grafo[inicio]:
        heapq.heappush(cola, (peso, inicio, vecino))

    paso = 1

    # Mientras todavía existan aristas por revisar Y no haya agregado todos los nodos:
    while cola and len(visitados) < len(grafo):

        # Saca siempre la arista más barata (ventaja del heap)
        peso, origen, destino = heapq.heappop(cola)

        print(f"\nPaso {paso}:")
        print(f"  Revisando arista {origen} --({peso})--> {destino}")

        # Si ya agregué ese nodo al árbol, significa que esta arista ya no sirve
        if destino in visitados:
            print("  -> Esta arista se descarta porque el nodo ya está en el árbol.")
            paso += 1
            continue

        # Si el nodo destino NO estaba en el árbol, entonces esta arista SÍ va al MST.
        print("  -> Esta arista se agrega al Árbol Parcial Mínimo.")
        visitados.add(destino)
        aristas_mst.append((origen, destino, peso))
        costo_total += peso

        # Imprimo lo que llevo hasta ahora solo para visualizar mejor
        print("  Nodos agregados:", visitados)
        print("  Aristas seleccionadas:")
        for (u, v, w) in aristas_mst:
            print(f"    {u} --({w})--> {v}")
        print("  Costo acumulado:", costo_total)

        # Ahora que agregué un nodo nuevo, meto sus aristas a la cola para considerarlas
        for vecino, p in grafo[destino]:
            if vecino not in visitados:
                print(f"    Agrego opción de arista {destino} --({p})--> {vecino}")
                heapq.heappush(cola, (p, destino, vecino))

        paso += 1

    print("\n=== RESULTADO FINAL ===")
    if len(visitados) < len(grafo):
        print("El grafo no estaba completamente conectado, así que no se puede formar un MST completo")
        return

    print("Árbol Parcial Mínimo final:")
    for (u, v, w) in aristas_mst:
        print(f"  {u} --({w})--> {v}")
    print(f"Costo total: {costo_total}")

    print("\nRepresentación gráfica simple:")
    for (u, v, w) in aristas_mst:
        print(f"[{u}] ---{w}--- [{v}]")


# Ejemplo para probar rápido en consola
grafo_ejemplo = {
    "A": [("B", 2), ("C", 3)],
    "B": [("A", 2), ("C", 1), ("D", 4)],
    "C": [("A", 3), ("B", 1), ("D", 5), ("E", 6)],
    "D": [("B", 4), ("C", 5), ("E", 2)],
    "E": [("C", 6), ("D", 2)]
}

if __name__ == "__main__":
    print("Nodos disponibles:", list(grafo_ejemplo.keys()))
    inicio = input("Nodo inicial para Prim: ").strip()

    if inicio not in grafo_ejemplo:
        print("Ese nodo no existe :(")
    else:
        prim_paso_a_paso(grafo_ejemplo, inicio)
