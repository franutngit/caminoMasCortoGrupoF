"""Prueba Dijkstra - Cuarto ajuste: Interactividad con usuario"""

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


class Grafo:
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
            print(
                f'La distancia más corta al vertice {v} es {self.vertices[v].distancia}m; vértice predecesor: {self.vertices[v].predecesor}')

    # 5 - Metodo que indica el recorrido de la ruta mas corta y la distancia total de la misma
    def camino(self, a, b):  # Recibe como parametro el vertice final
        camino = []
        actual = b
        if self.vertices[b].distancia == float('inf'):
            return 'El vertice final es inaccesible'
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


def origen(v):
    while True:
        print("Indique el punto de ORIGEN:")
        for i in range(len(v)):
            print(i + 1, v[i])
        n = int(input('Opcion: '))
        if 1 <= n <= len(v):
            return v[n - 1]
        else:
            print("Opcion invalida")


def destino(v):
    while True:
        print("Indique el punto de DESTINO:")
        for i in range(len(v)):
            print(i + 1, v[i])
        n = int(input('Opcion: '))
        if 1 <= n <= len(v):
            return v[n - 1]
        else:
            print("Opcion invalida")


class main:
    """Datos: Vertices y Aristas"""
    # VERTICES del grafo enlistados
    v = ['UTN',  # 0
         'Rodriguez y Sobremonte',  # 1
         'Rodriguez y A Villanueva',  # 2
         'Rodriguez y R Ortega',  # 3
         'Rotonda UTN',  # 4
         'Belgrano y A Villanueva',  # 5
         'Belgrano y Colon',  # 6
         'Belgrano y R Ortega/San Lorenzo',  # 7
         'Pedro Molina y Peru',  # 8
         'Peru y Infanta M de San Martin',  # 9
         'Colon y Peru',  # 10
         'San Lorenzo y Peru',  # 11
         'Pedro Molina y 25 de Mayo',  # 12
         '25 de Mayo y Infanta M de San Martin',  # 13
         'Colon y 25 de Mayo',  # 14
         '25 de Mayo y San Lorenzo',  # 15
         'Peru entre P Molina y Infanta M de SM']  # 16
    # ARISTAS del grafo enlistados
    a = [[v[0], v[1], 100],
         [v[1], v[2], 250],
         [v[1], v[4], 90],
         [v[2], v[3], 75],
         [v[3], v[7], 125],
         [v[4], v[1], 90],
         [v[4], v[6], 250],
         [v[5], v[4], 250],
         [v[5], v[2], 125],
         [v[6], v[5], 0],
         [v[6], v[7], 75],
         [v[7], v[5], 75],
         [v[7], v[11], 100],
         [v[8], v[4], 90],
         [v[8], v[-1], 50],
         [v[9], v[10], 120],
         [v[10], v[6], 90],
         [v[10], v[11], 90],
         [v[11], v[15], 100],
         [v[12], v[8], 90],
         [v[13], v[9], 90],
         [v[13], v[12], 100],
         [v[14], v[10], 90],
         [v[14], v[13], 120],
         [v[15], v[14], 100],
         [v[-1], v[9], 50]]

    '''Armado del grafo'''
    g = Grafo()
    for e in v:
        g.agregarVertice(e)
    for e in a:
        g.agregarArista(e[0], e[1], e[2])

    '''Interaccion con el usuario'''
    o = origen(v)
    print(f'ORIGEN escogido: {o}\n')
    d = destino(v)
    print(f'DESTINO escogido: {d}')

    '''Camino mas corto mediante Dijkstra'''
    g.dijkstra(o)  # Aqui se indica el vertice inicial v[0]
    print(g.camino(o, d))  # Aqui se indica el vertice final v[-1], es decir, el ultimo de la lista

    # Valores por vertice:
    # print("\nValores finales de la grafica:")
    # g.imprimirGrafica()
