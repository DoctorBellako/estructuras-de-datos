# Programa principal - menu para probar las estructuras

from lineales.pila import Pila
from lineales.cola import Cola
from lineales.lista_enlazada import ListaEnlazada
from no_lineales.arbol_binario import ArbolBinario
from no_lineales.grafo import Grafo

print("=== Estructuras de datos ===")
print("1. Pila")
print("2. Cola")
print("3. Lista enlazada")
print("4. Arbol binario")
print("5. Grafo")

opcion = input("Elige una opcion (1-5): ")

if opcion == "1":
    p = Pila()
    p.apilar(1)
    p.apilar(2)
    p.apilar(3)
    p.mostrar()
    print("Saco:", p.desapilar())
elif opcion == "2":
    c = Cola()
    c.encolar("A")
    c.encolar("B")
    c.mostrar()
    print("Saco:", c.desencolar())
elif opcion == "3":
    l = ListaEnlazada()
    l.agregar_final(5)
    l.agregar_final(10)
    l.agregar_inicio(1)
    l.mostrar()
elif opcion == "4":
    a = ArbolBinario()
    for n in [8, 3, 10, 1, 6]:
        a.insertar(n)
    a.inorden(a.raiz)
    print()
elif opcion == "5":
    g = Grafo()
    g.agregar_arista(1, 2)
    g.agregar_arista(1, 3)
    g.agregar_arista(2, 4)
    g.bfs(1)
else:
    print("Opcion no valida")
