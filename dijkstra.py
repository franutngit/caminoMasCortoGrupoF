# clase para definir un vertice
class Vertice:
    """Clase que define los vertices de las graficas"""

    # constructor
    def __init__(self, i):
        self.id = i
        self.vecinos = []
        self.visitado = False
        self.padre = None
        self.distancia = float('inf')

    def agregarVecino(self, v, p):
        if not v in self.vecinos:
            self.vecinos.append([v, p])


class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)

    def agregarArista(self, a, b, p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b, p)
            self.vertices[b].agregarVecino(a, p)

    def imprimirGrafica(self):
        for v in self.vertices:
            print("La distancia del vertice " + str(v) + " es " + str(self.vertices[v].distancia) + " llegando desde " +
                  str(self.vertices[v].padre))

    def camino(self, b):
        camino = []
        actual = b
        while actual is not None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[b].distancia]

    def minimo(self, lista):
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]
            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia
                    v = e

            return v

    def dijkstra(self, a):
        if a in self.vertices:
            self.vertices[a].distancia = 0
            actual = a
            noVisitados = []

            for v in self.vertices:
                if v != a:
                    self.vertices[v].distancia = float('inf')
                self.vertices[v].padre = None
                noVisitados.append(v)

            while len(noVisitados) > 0:
                for vecino in self.vertices[actual].vecinos:
                    if not self.vertices[vecino[0]].visitado:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual

                self.vertices[actual].visitado = True
                noVisitados.remove(actual)

                actual = self.minimo(noVisitados)

        else:
            return False


class main:
    g = Grafica()
    g.agregarVertice(1)
    g.agregarVertice(2)
    g.agregarVertice(3)
    g.agregarVertice(4)
    g.agregarVertice(5)
    g.agregarVertice(6)
    g.agregarArista(1, 6, 14)
    g.agregarArista(1, 2, 7)
    g.agregarArista(1, 3, 9)
    g.agregarArista(2, 3, 10)
    g.agregarArista(2, 4, 15)
    g.agregarArista(3, 4, 11)
    g.agregarArista(3, 6, 2)
    g.agregarArista(4, 5, 6)
    g.agregarArista(5, 6, 9)

    print("\n\nLa ruta mas rapida por Dijkstra junto con su costo es:")
    g.dijkstra(1)
    print(g.camino(6))
    print("\nLos valores finales de la grafica son los siguientes:")
    g.imprimirGrafica()
