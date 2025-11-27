
# Primero defino una estructura de "Union-Find" (o Disjoint Set).
# Esto me sirve para saber si dos nodos ya están conectados en el árbol.
# Si los uno otra vez, formaría un ciclo y eso es justo lo que Kruskal evita.

class UnionFind:
    def __init__(self, nodos):
        # parent[nodo] me dice quién es el "papá" de ese nodo en el conjunto.
        # Al inicio, cada nodo es su propio papá.
        self.parent = {n: n for n in nodos}
        # rank lo uso para hacer las uniones de manera más eficiente.
        self.rank = {n: 0 for n in nodos}

    def find(self, nodo):
        # Esta función regresa el "representante" del conjunto del nodo.
        # Si el nodo no es su propio papá, sigo subiendo hasta encontrar la raíz.
        # De paso, aplico "path compression" para que quede más plano.
        if self.parent[nodo] != nodo:
            self.parent[nodo] = self.find(self.parent[nodo])
        return self.parent[nodo]

    def union(self, a, b):
        # Uno los conjuntos de a y b si no están ya unidos.
        raiz_a = self.find(a)
        raiz_b = self.find(b)

        if raiz_a == raiz_b:
            # Si ya tienen la misma raíz, unirlos crearía un ciclo.
            return False

        # Si no, los conecto. Uso rank para que el árbol no se haga muy profundo.
        if self.rank[raiz_a] < self.rank[raiz_b]:
            self.parent[raiz_a] = raiz_b
        elif self.rank[raiz_a] > self.rank[raiz_b]:
            self.parent[raiz_b] = raiz_a
        else:
            self.parent[raiz_b] = raiz_a
            self.rank[raiz_a] += 1

        return True


def kruskal_paso_a_paso(nodos, aristas, modo="minimo"):
    """
    nodos: lista de nodos, por ejemplo ["A", "B", "C", "D"]
    aristas: lista de tuplas (peso, origen, destino)
    modo: "minimo" para árbol de costo mínimo, "maximo" para árbol de costo máximo
    """

    # Aquí voy a guardar las aristas que sí entran al Árbol de Kruskal.
    arbol = []
    costo_total = 0

    # Inicializo la estructura de conjuntos disjuntos.
    uf = UnionFind(nodos)

    # Ordeno las aristas según el modo.
    # Si es mínimo -> de menor a mayor.
    # Si es máximo -> de mayor a menor.
    if modo == "minimo":
        aristas_ordenadas = sorted(aristas, key=lambda x: x[0])
        print("=== ALGORITMO DE KRUSKAL (Árbol de COSTO MÍNIMO) ===")
    else:
        aristas_ordenadas = sorted(aristas, key=lambda x: x[0], reverse=True)
        print("=== ALGORITMO DE KRUSKAL (Árbol de COSTO MÁXIMO) ===")

    print("Nodos:", nodos)
    print("Aristas (peso, origen, destino):")
    for w, u, v in aristas:
        print(f"  ({w}, {u}, {v})")

    print("-----------------------------------------")

    paso = 1

    # Recorro todas las aristas ya ordenadas.
    for peso, origen, destino in aristas_ordenadas:
        print(f"\nPaso {paso}: revisando arista {origen} --({peso})--> {destino}")

        # Reviso si esta arista conecta dos componentes distintos.
        # Si sí, la puedo agregar. Si no, formaría un ciclo y la descarto.
        if uf.union(origen, destino):
            print("  -> Esta arista NO forma ciclo. La agrego al árbol.")
            arbol.append((origen, destino, peso))
            costo_total += peso

            print("  Aristas en el árbol hasta ahora:")
            for (u, v, w) in arbol:
                print(f"    {u} --({w})--> {v}")
            print(f"  Costo acumulado: {costo_total}")
        else:
            print("  -> Esta arista formaría un ciclo. Se descarta.")

        # Si ya tengo (nodos - 1) aristas, el árbol está completo.
        if len(arbol) == len(nodos) - 1:
            print("\nYa se tienen suficientes aristas para formar el árbol.")
            break

        paso += 1

    print("\n=== RESULTADO FINAL ===")
    if len(arbol) != len(nodos) - 1:
        print("No se pudo formar un árbol que conecte todos los nodos (el grafo no es conexo).")
        return

    if modo == "minimo":
        print("Árbol de EXPANSIÓN MÍNIMA (Kruskal):")
    else:
        print("Árbol de EXPANSIÓN MÁXIMA (Kruskal):")

    for (u, v, w) in arbol:
        print(f"  {u} --({w})--> {v}")
    print(f"Costo total del árbol: {costo_total}")

    # Parte gráfica simple en texto.
    print("\nRepresentación gráfica simple:")
    for (u, v, w) in arbol:
        print(f"[{u}] ---{w}--- [{v}]")


# Ejemplo de grafo para probar el algoritmo.
nodos_ejemplo = ["A", "B", "C", "D", "E"]

# Cada arista es (peso, origen, destino).
aristas_ejemplo = [
    (2, "A", "B"),
    (3, "A", "C"),
    (1, "B", "C"),
    (4, "B", "D"),
    (5, "C", "D"),
    (6, "C", "E"),
    (2, "D", "E")
]

if __name__ == "__main__":
    print("Nodos disponibles:", nodos_ejemplo)
    print("Aristas disponibles (peso, origen, destino):")
    for w, u, v in aristas_ejemplo:
        print(f"  ({w}, {u}, {v})")

    print("\n¿Quieres Árbol de costo mínimo o máximo?")
    print("1) Mínimo")
    print("2) Máximo")
    opcion = input("Elige 1 o 2: ").strip()

    if opcion == "1":
        modo = "minimo"
    elif opcion == "2":
        modo = "maximo"
    else:
        print("Opción no válida, uso mínimo por defecto.")
        modo = "minimo"

    kruskal_paso_a_paso(nodos_ejemplo, aristas_ejemplo, modo=modo)
