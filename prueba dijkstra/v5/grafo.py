"""Clase que define los vertices del grafo"""


class Vertice:
    def __init__(self, id):
        self.id = id
        self.vecinos = []
        self.visitado = False
        self.predecesor = None
        self.distancia = float('inf')

    def agregarVecino(self, idVert, dist):
        # el condicional es para evitar la repeticion de vertices
        if not idVert in self.vecinos:
            self.vecinos.append([idVert, dist])


"""Clase que define el grafo y calcula el camino mas corto"""


class Grafo:
    def __init__(self):
        self.dicVertices = {}

    def agregarVertice(self, idVert):
        # Se chequea que el vertice no se encuentre en el diccionario
        if idVert not in self.dicVertices:
            self.dicVertices[idVert] = Vertice(idVert)

    # Crea las aristas del grafo:
    def agregarArista(self, idVertA, idVertB, dist):
        if idVertA in self.dicVertices and idVertB in self.dicVertices:  # Se chequea si los vertices ya se encuentran en el diccionario
            self.dicVertices[idVertA].agregarVecino(idVertB, dist)
            # En este caso, la arista va dirigida de 'A' hacia 'B'

    # 5 - Metodo que indica el recorrido de la ruta mas corta y la distancia total de la misma
    def camino(self, idVertOrigen, idVertDestino):
        camino = []
        actual = idVertDestino
        if self.dicVertices[idVertDestino].distancia == float('inf'):
            return 'El DESTINO es inaccesible'
        else:
            print(f"\n La ruta mas rapida por Dijkstra desde '{idVertOrigen}' hasta '{idVertDestino}' es:")
            # Recorre los vertices desde el final yendo por los predecesores, para definir el camino mas corto
            while actual is not None:
                camino.insert(0, actual)
                actual = self.dicVertices[actual].predecesor
            return f'{camino}; DISTANCIA RECORRIDA: {self.dicVertices[idVertDestino].distancia} metros'

    # 4 - Funcion que retorna el vertice con menor distancia, de la lista de los no visitados
    def minimo(self, listVertNoV):  # lista: vertices no visitados
        if len(listVertNoV) > 0:
            distMenorVert = self.dicVertices[listVertNoV[0]].distancia  # Distancia del primer elemento
            idVertMenorDist = listVertNoV[0]  # El primer elemento es el primero de la lista
            for idVert in listVertNoV:
                if distMenorVert > self.dicVertices[idVert].distancia:
                    distMenorVert = self.dicVertices[idVert].distancia  # Se actualiza la distancia si es menor
                    idVertMenorDist = idVert  # Se indica cuál es el nodo de menor distancia
            return idVertMenorDist

    # Metodo que contiene el ALGORITMO DE DIJKSTRA
    def dijkstra(self, idVertOrigen):
        if idVertOrigen in self.dicVertices:  # Debe verificarse que el nodo de partida se encuentra en el conjunto de vertices
            self.dicVertices[idVertOrigen].distancia = 0  # 1 - Se establece la distancia del nodo inicial como 0
            actual = idVertOrigen  # 1 - Se establece que el vertice inicial como el actual
            # 1 - Se crea una lista de vertices no visitados y se los llena
            vertNoVisitados = []
            for idVert in self.dicVertices:
                if idVert != idVertOrigen:  # el nodo inicial debe tener una distancia 0
                    self.dicVertices[idVert].distancia = float('inf')  # Valor infinito por defecto
                self.dicVertices[idVert].predecesor = None  # se indica al inicio no tiene predecesor
                vertNoVisitados.append(idVert)  # se añade el vertice a la lista

            # 2 - Este bucle se repite mientras hayan vertices no visitados:
            while len(vertNoVisitados) > 0:
                # 2 - Se recorrera cada vecino del vertice actual, para ajustar las distancias y crear el camino:
                for vertVecino in self.dicVertices[actual].vecinos:
                    if not self.dicVertices[vertVecino[0]].visitado:  # Solo se consideran los vertices vecinos no visitados
                        # 2 - Se revisa si es necesario realizar la correccion de la distancia, para ver si hay una mas corta:
                        if self.dicVertices[actual].distancia + vertVecino[1] < self.dicVertices[vertVecino[0]].distancia:
                            # Si se cumple la condicion anterior, se corrige la distancia y se indica el predecesor
                            self.dicVertices[vertVecino[0]].distancia = self.dicVertices[actual].distancia + vertVecino[1]
                            self.dicVertices[vertVecino[0]].predecesor = actual
                # 3 - Se define el vertice actual como visitado y se lo quita de la lista de no visitados
                self.dicVertices[actual].visitado = True
                vertNoVisitados.remove(actual)
                # 4 - Se define el nuevo vertice actual, el cual debe tener la menor distancia recorrida
                actual = self.minimo(vertNoVisitados)
        else:
            return False
