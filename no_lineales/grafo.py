# Grafo no dirigido usando lista de adyacencia (un diccionario)

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = []

    def agregar_arista(self, a, b):
        self.agregar_vertice(a)
        self.agregar_vertice(b)
        self.vertices[a].append(b)
        self.vertices[b].append(a)

    def mostrar(self):
        for v in self.vertices:
            print(v, "->", self.vertices[v])

    # Recorrido en anchura (BFS)
    def bfs(self, inicio):
        visitados = [inicio]
        cola = [inicio]
        while len(cola) > 0:
            actual = cola.pop(0)
            print(actual, end=" ")
            for vecino in self.vertices[actual]:
                if vecino not in visitados:
                    visitados.append(vecino)
                    cola.append(vecino)
        print()


# Ejemplo: ciudades conectadas
if __name__ == "__main__":
    g = Grafo()
    g.agregar_arista("Medellin", "Bogota")
    g.agregar_arista("Medellin", "Cali")
    g.agregar_arista("Bogota", "Cartagena")
    g.agregar_arista("Cali", "Cartagena")
    g.mostrar()
    print("Recorrido desde Medellin:")
    g.bfs("Medellin")
