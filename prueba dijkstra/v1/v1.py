"""Prueba Dijkstra v1 - Primera aproximacion"""

'''Clase que define los vertices del grafo'''


class Vertice:
    def __init__(self, i):
        self.id = i
        self.vecinos = []
        self.visitado = False
        self.predecesor = None
        self.distancia = float('inf')

    def agregarVecino(self, v, p):
        # el condicional es para evitar la repeticion de vertices
        if not v in self.vecinos:
            self.vecinos.append([v, p])


'''Clase que define el grafo y calcula el camino mas corto'''


class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, v):
        # Se chequea que el vertice no se encuentra en el diccionario
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)

    # Metodo que crea las aristas del grafo, que son las uniones entre los vertices
    def agregarArista(self, a, b, p):
        if a in self.vertices and b in self.vertices:  # Se chequea si los vertices ya se encuentran en el diccionario
            # Se agregan los vecinos a ambos vertices, ya que es un grafo NO DIRIGIDO:
            self.vertices[a].agregarVecino(b, p)
            self.vertices[b].agregarVecino(a, p)

    # 6 - Metodo que devuelve la informacion que contiene cada vertice (distancia y predecesor):
    def imprimirGrafica(self):
        for v in self.vertices:
            print("La distancia del vertice " + str(v) + " es " + str(self.vertices[v].distancia) + " llegando desde " +
                  str(self.vertices[v].predecesor))

    # 5 - Metodo que indica el recorrido de la ruta mas corta y la distancia total de la misma
    def camino(self, b):  # Recibe como parametro el vertice final
        camino = []
        actual = b
        # Recorre los vertices desde el final yendo por los predecesores, para definir el camino mas corto
        while actual is not None:
            camino.insert(0, actual)
            actual = self.vertices[actual].predecesor
        return [camino, self.vertices[b].distancia]

    # 4 - Funcion que retorna el vertice con menor distancia, de la lista de los no visitados
    def minimo(self, lista):  # lista: vertices no visitados
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia  # Distancia del primer elemento
            v = lista[0]  # El primer elemento es el primero de la lista
            # Se recorre la lista completa de nodos no visitados
            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia  # Se actualiza la distancia si es menor
                    v = e  # Se indica cuál es el nodo de menor distancia
            return v

    # Metodo que contiene el ALGORITMO DE DIJKSTRA
    def dijkstra(self, a):
        if a in self.vertices:  # Debe verificarse que el nodo de partida se encuentra en el conjunto de vertices
            self.vertices[a].distancia = 0  # 1 - Se establece la distancia del nodo inicial como 0
            actual = a  # 1 - Se establece que el vertice inicial como el actual
            # 1 - Se crea una lista de vertices no visitados y se los llena
            noVisitados = []
            for v in self.vertices:
                if v != a:  # el nodo inicial debe tener una distancia 0, por lo que no debe ingresar
                    self.vertices[v].distancia = float('inf')  # Valor infinito por defecto
                self.vertices[v].predecesor = None  # se indica al inicio no tiene predecesor
                noVisitados.append(v)  # se añade el vertice a la lista

            # 2 - Este bucle se repite mientras hayan vertices no visitados:
            while len(noVisitados) > 0:
                # 2 - Se recorrera cada vecino del vertice actual, para ajustar las distancias y crear el camino:
                for vecino in self.vertices[actual].vecinos:
                    if not self.vertices[vecino[0]].visitado:  # Solo se consideran los vertices vecinos no visitados
                        # 2 - Se revisa si es necesario realizar la correccion de la distancia, para ver si hay una mas corta:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            # Si se cumple la condicion anterior, se corrige la distancia y se indica el predecesor
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].predecesor = actual
                # 3 - Se define el vertice actual como visitado y se lo quita de la lista de no visitados
                self.vertices[actual].visitado = True
                noVisitados.remove(actual)
                # 4 - Se define el nuevo vertice actual, el cual debe tener la menor distancia recorrida
                actual = self.minimo(noVisitados)
        else:
            return False


'''Clase que agrupa el codigo que ejecuta el algoritmo'''


class main:
    # Creacion del grafo de primera aproximacion (GRAFO NO DIRIGIDO)
    g = Grafica()
    # Se agregan los vertices al grafo
    A, B, C, D, E, F, G, H, I, X = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'X'
    g.agregarVertice(A)
    g.agregarVertice(B)
    g.agregarVertice(C)
    g.agregarVertice(D)
    g.agregarVertice(E)
    g.agregarVertice(F)
    g.agregarVertice(G)
    g.agregarVertice(H)
    g.agregarVertice(I)
    g.agregarVertice(X)
    # Se indican las aristas del grafo y sus respectivas distancias
    g.agregarArista(A, B, 50)
    g.agregarArista(A, D, 125)
    g.agregarArista(B, C, 190)
    g.agregarArista(B, E, 50)
    g.agregarArista(C, F, 40)
    g.agregarArista(C, G, 220)
    g.agregarArista(D, E, 130)
    g.agregarArista(D, H, 300)
    g.agregarArista(E, F, 190)
    g.agregarArista(E, H, 200)
    g.agregarArista(F, G, 180)
    g.agregarArista(F, I, 220)
    g.agregarArista(G, X, 240)
    g.agregarArista(H, I, 200)
    g.agregarArista(I, X, 60)

    # Camino mas corto mediante el algoritmo
    print("\n\nLa ruta mas rapida por Dijkstra junto con su costo es:")
    g.dijkstra(A)  # Aqui se indica el vertice inicial A
    print(g.camino(X))  # Aqui se indica el vertice final X

    # A continuacion se indicara, para cada vertice, la distancia mas corta respecto al vertice inicial, y el vertice
    # desde donde viene para minimizar la distancia
    print("\nLos valores finales de la grafica son los siguientes:")
    g.imprimirGrafica()
