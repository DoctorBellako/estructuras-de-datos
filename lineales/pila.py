# Pila (Stack) - el ultimo en entrar es el primero en salir (LIFO)

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, dato):
        self.items.append(dato)

    def desapilar(self):
        if self.esta_vacia():
            print("La pila esta vacia")
            return None
        return self.items.pop()

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.items[-1]

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        print("Pila:", self.items)


# Ejemplo
if __name__ == "__main__":
    pila = Pila()
    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)
    pila.mostrar()
    print("Saco:", pila.desapilar())
    print("Tope:", pila.ver_tope())
