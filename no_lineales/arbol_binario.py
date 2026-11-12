# Arbol binario de busqueda
# Los menores van a la izquierda y los mayores a la derecha

class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self._insertar(self.raiz, dato)

    def _insertar(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(dato)
            else:
                self._insertar(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(dato)
            else:
                self._insertar(nodo.derecha, dato)

    def buscar(self, dato):
        return self._buscar(self.raiz, dato)

    def _buscar(self, nodo, dato):
        if nodo is None:
            return False
        if nodo.dato == dato:
            return True
        if dato < nodo.dato:
            return self._buscar(nodo.izquierda, dato)
        return self._buscar(nodo.derecha, dato)

    # Recorrido inorden (sale ordenado de menor a mayor)
    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierda)
            print(nodo.dato, end=" ")
            self.inorden(nodo.derecha)


# Ejemplo
if __name__ == "__main__":
    arbol = ArbolBinario()
    for numero in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(numero)

    print("Inorden:", end=" ")
    arbol.inorden(arbol.raiz)
    print()
    print("Esta el 60?", arbol.buscar(60))
    print("Esta el 99?", arbol.buscar(99))
