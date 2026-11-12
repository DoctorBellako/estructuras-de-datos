# Lista enlazada simple - cada nodo apunta al siguiente

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_final(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def agregar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.dato == dato:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return
            anterior = actual
            actual = actual.siguiente
        print("No encontre el dato", dato)

    def mostrar(self):
        actual = self.cabeza
        texto = ""
        while actual is not None:
            texto = texto + str(actual.dato) + " -> "
            actual = actual.siguiente
        print(texto + "None")


# Ejemplo
if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.agregar_final(1)
    lista.agregar_final(2)
    lista.agregar_final(3)
    lista.agregar_inicio(0)
    lista.mostrar()
    lista.eliminar(2)
    lista.mostrar()
