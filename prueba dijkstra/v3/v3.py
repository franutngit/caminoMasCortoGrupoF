"""Prueba Dijkstra - Tercer ajuste"""

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
            # Para un GRAFO DIRIGIDO se ajustara esta linea, de 'a' hacia 'b'
            self.vertices[a].agregarVecino(b, p)
            # 'b' es vecino de 'a', pero no al reves, ya que esta dirigido de 'a' a 'b'

    # 6 - Metodo que devuelve la informacion que contiene cada vertice (distancia y predecesor):
    def imprimirGrafica(self):
        for v in self.vertices:
            print("La distancia más corta al vertice " + str(v) + " es " + str(
                self.vertices[v].distancia) + "; vértice predecesor: " +
                  str(self.vertices[v].predecesor))

    # 5 - Metodo que indica el recorrido de la ruta mas corta y la distancia total de la misma
    def camino(self, b):  # Recibe como parametro el vertice final
        camino = []
        actual = b
        if self.vertices[b].distancia == float('inf'):
            return 'El vertice final es inaccesible'
        else:
            print("\n\nLa ruta mas rapida por Dijkstra y la distancia correspondiente es:")
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
    # Creacion del grafo de segundo ajuste (GRAFO DIRIGIDO)
    g = Grafica()
    # Se agregan los vertices al grafo
    # Vertices de inicio y fin
    I = 'Inicio'
    F = 'Fin'

    # Vertices intermedios
    v1 = '1'
    v2 = '2'
    v3 = '3'
    v4 = '4'
    v5 = '5'
    v6 = '6'
    v7 = '7'
    v8 = '8'
    v9 = '9'
    v10 = '10'
    v11 = '11'
    v12 = '12'
    v13 = '13'
    v14 = '14'
    v15 = '15'

    # Lista de vertices intermedios
    vert = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15]

    # Se agregan los vertices al grafo
    g.agregarVertice(I)
    for v in vert:
        g.agregarVertice(v)
    g.agregarVertice(F)

    # Se indican las aristas del grafo y sus respectivas distancias
    # Al agregarse las aristas, se va indicando el sentido de cada vertice
    g.agregarArista(I, v1, 100)
    g.agregarArista(v1, v2, 250)
    g.agregarArista(v1, v4, 90)
    g.agregarArista(v2, v3, 75)
    g.agregarArista(v3, v7, 125)
    g.agregarArista(v4, v1, 90)
    g.agregarArista(v4, v6, 250)
    g.agregarArista(v5, v4, 250)
    g.agregarArista(v5, v2, 125)
    g.agregarArista(v6, v5, 0)
    g.agregarArista(v6, v7, 75)
    g.agregarArista(v7, v5, 75)
    g.agregarArista(v7, v11, 100)
    g.agregarArista(v8, v4, 90)
    g.agregarArista(v8, F, 50)
    g.agregarArista(v9, v10, 120)
    g.agregarArista(v10, v6, 90)
    g.agregarArista(v10, v11, 90)
    g.agregarArista(v11, v15, 100)
    g.agregarArista(v12, v8, 90)
    g.agregarArista(v13, v9, 90)
    g.agregarArista(v13, v12, 100)
    g.agregarArista(v14, v10, 90)
    g.agregarArista(v14, v13, 120)
    g.agregarArista(v15, v14, 100)
    g.agregarArista(F, v9, 50)

    '''Camino mas corto mediante el algoritmo'''
    g.dijkstra(I)  # Aqui se indica el vertice inicial
    print(g.camino(F))  # Aqui se indica el vertice final

    # A continuacion se indicara, para cada vertice, la distancia mas corta respecto al vertice inicial, y el vertice
    # desde donde viene para minimizar la distancia
    print("\nValores finales de la grafica:")
    g.imprimirGrafica()
