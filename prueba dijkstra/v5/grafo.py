"""Clase que define los vertices del grafo"""


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


"""Clase que define el grafo y calcula el camino mas corto"""


class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, v):
        # Se chequea que el vertice no se encuentra en el diccionario
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)

    # Crea las aristas del grafo:
    def agregarArista(self, a, b, p):
        if a in self.vertices and b in self.vertices:  # Se chequea si los vertices ya se encuentran en el diccionario
            self.vertices[a].agregarVecino(b, p)
            # En este caso, la arista va dirigida de 'a' hacia 'b'

    # 5 - Metodo que indica el recorrido de la ruta mas corta y la distancia total de la misma
    def camino(self, a, b):
        camino = []
        actual = b
        if self.vertices[b].distancia == float('inf'):
            return 'El DESTINO es inaccesible'
        else:
            print(f"\n La ruta mas rapida por Dijkstra desde '{a}' hasta '{b}' es:")
            # Recorre los vertices desde el final yendo por los predecesores, para definir el camino mas corto
            while actual is not None:
                camino.insert(0, actual)
                actual = self.vertices[actual].predecesor
            return f'{camino}; DISTANCIA RECORRIDA: {self.vertices[b].distancia} metros'

    # 4 - Funcion que retorna el vertice con menor distancia, de la lista de los no visitados
    def minimo(self, lista):  # lista: vertices no visitados
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia  # Distancia del primer elemento
            v = lista[0]  # El primer elemento es el primero de la lista
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
                if v != a:  # el nodo inicial debe tener una distancia 0
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
