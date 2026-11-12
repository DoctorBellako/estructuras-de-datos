# Cola (Queue) - el primero en entrar es el primero en salir (FIFO)

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, dato):
        self.items.append(dato)

    def desencolar(self):
        if self.esta_vacia():
            print("La cola esta vacia")
            return None
        return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        print("Cola:", self.items)


# Ejemplo: fila de un banco
if __name__ == "__main__":
    fila = Cola()
    fila.encolar("Ana")
    fila.encolar("Luis")
    fila.encolar("Maria")
    fila.mostrar()
    print("Atiendo a:", fila.desencolar())
    fila.mostrar()
