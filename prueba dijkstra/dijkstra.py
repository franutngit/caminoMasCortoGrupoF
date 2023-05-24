"""El codigo pretende ejecutar el algoritmo de Dijkstra en un grafo NO DIRIGIDO; en la ejecución se le han de indicar
la cantidad de vertices, las aristas con sus respectivos pesos y el algoritmo devolvera el camino mas corto,
indicando los vertices que recorre; ademas indica el camino mas corto para cada vertice del grafo en relacion al punto
de inicio indicado y, para cada vertice, por donde ha de recorrer el camino para que sea el de menor distancia.
El algoritmo sólo mostrará un camino mas corto. Si hay otro camino mas corto con la misma distancia, no se mostrara."""

'''Clase que define los vertices del grafo, sus relaciones con los otros vertices y su comportamiento en el algoritmo'''


class Vertice:
    def __init__(self, i):
        self.id = i  # variable que identifica al vertice
        self.vecinos = []  # lista que indica los vertices contiguos al vertice
        self.visitado = False  # indica si el vertice ya ha sido recorrido por el algoritmo
        self.predecesor = None  # indica el vertice vecino donde la distancia es menor en el camino mas corto
        self.distancia = float('inf')  # distancia inicial estandar de 'infinito'

    def agregarVecino(self, v, p):
        if not v in self.vecinos:  # el condicional es para evitar la repeticion de vertices
            self.vecinos.append([v, p])  # al agregar un vertice vecino, se dice cual (v) y la distancia al mismo (p)
        # Tener en cuenta que, como estan en una lista, vecino[0] es el indice del vecino (v), y que vecino[1] es la
        # distancia o peso con el mismo (p); vecino[0] y vecino[1] se utilizaran varias veces en el codigo


'''Clase que relaciona los vertices del grafo mediante aristas, que contiene el algoritmo de dijkstra 
y que indica el camino mas corto'''


class Grafica:
    def __init__(self):
        self.vertices = {}  # Diccionario que contiene los vertices (objetos) en el grafo

    # Metodo para agregar vertices al diccionario 'vertices'
    def agregarVertice(self, v):
        if v not in self.vertices:  # Se chequea que el vertice no se encuentra en el diccionario
            self.vertices[v] = Vertice(
                v)  # Se agrega el vertice al diccionario (objeto); el parametro coincide con el indice del objeto

    # Metodo que crea las aristas del grafo, que son las uniones entre los vertices
    def agregarArista(self, a, b,
                      p):  # Al crear la arista, deben indicarse los dos vertices que la conforman y la distancia (p) que los une
        if a in self.vertices and b in self.vertices:  # Se chequea si los vertices ya se encuentran en el diccionario (condicion necesaria para crear una arista)
            # Se agregan los vecinos a ambos vertices, ya que es un grafo NO DIRIGIDO:
            self.vertices[a].agregarVecino(b, p)
            self.vertices[b].agregarVecino(a, p)

    # 6 - Metodo que devuelve la informacion que contiene cada vertice:
    # Se recorre a cada uno y deberá decir la menor distancia al vertice inicial y el vértice predecesor en el camino mas corto
    def imprimirGrafica(self):
        for v in self.vertices:
            print("La distancia del vertice " + str(v) + " es " + str(self.vertices[v].distancia) + " llegando desde " +
                  str(self.vertices[v].predecesor))

    # 5 - Metodo que indica el recorrido de la ruta mas corta y la distancia total de la misma
    def camino(self, b):  # Recibe como parametro el nodo final para indicar el camino mas corto
        camino = []  # Lista que contendrá los índices de los vértices de la ruta mas corta
        actual = b  # El nodo actual, en este caso, sera el nodo final, para recorrerlo en sentido inverso
        while actual is not None:  # Cuando sea None significa que ha recorrido el camino mas corto, desde el final al principio
            camino.insert(0,
                          actual)  # Se utiliza insert en lugar de append, para que se coloque el vertice al inicio de la lista
            actual = self.vertices[actual].predecesor  # Se va actualizando el nodo, hacia el predecesor del vertice actual
        return [camino, self.vertices[b].distancia]  # Se retorna el camino de vertices y la distancia total

    # Metodo complementario al del Algoritmo de Dijkstra:
    # 4 - Para definir el nuevo vertice actual es necesario saber el vertice de menor distancia recorrida:
    def minimo(self, lista):  # Recibe como parametro la lista de vertices no visitados
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia  # Distancia del primer elemento
            v = lista[0]  # El primer elemento es el primero de la lista
            # Se recorre la lista completa de nodos no visitados
            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia  # Se actualiza la distancia si es menor
                    v = e  # Se indica cuál es el nodo de menor distancia
            return v  # Se retorna el vertice con menor distancia

    # Metodo que contiene el ALGORITMO DE DIJKSTRA
    def dijkstra(self, a):
        if a in self.vertices:  # Debe verificarse que el nodo de partida se encuentra en el conjunto de vertices
            self.vertices[a].distancia = 0  # 1 - Se establece la distancia del nodo inicial como 0
            actual = a  # 1 - Se establece que el vertice 'a' es ahora el vertice actual, es decir, el que se compara con los demas vertices
            # 1 - Se crea una lista de vertices no visitados (los cuales se iran descartando hasta terminar el algoritmo)
            noVisitados = []

            # 1 - Se llena la lista de vertices como 'no visitados' aun:
            for v in self.vertices:
                if v != a:  # el nodo inicial debe tener una distancia 0, por lo que no debe ingresar
                    self.vertices[v].distancia = float(
                        'inf')  # se les asigna por defecto una distancia de infinito al inicio
                self.vertices[
                    v].predecesor = None  # se indica al inicio que no se proviene de ningun vertice, ya que no se ha realizado ningun camino todavia
                noVisitados.append(v)  # se añade el vertice a la lista

            # 2 - Este bucle se repite mientras hayan vertices no visitados:
            while len(noVisitados) > 0:
                # 2 - Se recorrera cada vecino del vertice actual, para ajustar las distancias y crear el camino:
                for vecino in self.vertices[actual].vecinos:
                    if not self.vertices[vecino[0]].visitado:  # Solo se consideran los vertices vecinos no visitados
                        # 2 - Se revisa si es necesario realizar la correccion de la distancia, para ver si hay una mas corta:
                        # Para ello se compara que la suma de la distancia recorrida mas la distancia al vertice vecino sea
                        # menor a la distancia que ya existe en ese vertice vecino
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            # Si se cumple la condicion anterior, se corrige la distancia que ya tiene el vertice
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            # ... y se indica que el camino mas corto proviene del vertice actual
                            self.vertices[vecino[0]].predecesor = actual

                # 3 - Se define el vertice actual como visitado y se lo quita de la lista de no visitados
                self.vertices[actual].visitado = True
                noVisitados.remove(actual)

                # 4 - Se define el nuevo vertice actual, el cual debe tener la menor distancia recorrida
                actual = self.minimo(noVisitados)

        else:  # Este 'else' solo se activa si el nodo de partida no existe en el conjunto de vertices
            return False


'''Clase que agrupa el codigo que ejecuta el algoritmo'''


class main:
    # Creacion del grafo
    g = Grafica()
    # Se agregan los vertices al grafo
    g.agregarVertice(1)
    g.agregarVertice(2)
    g.agregarVertice(3)
    g.agregarVertice(4)
    g.agregarVertice(5)
    g.agregarVertice(6)
    # Se indican las aristas del grafo (vertices que estan unidos) y sus respectivas distancias
    g.agregarArista(1, 6, 14)
    g.agregarArista(1, 2, 7)
    g.agregarArista(1, 3, 9)
    g.agregarArista(2, 3, 10)
    g.agregarArista(2, 4, 15)
    g.agregarArista(3, 4, 11)
    g.agregarArista(3, 6, 2)
    g.agregarArista(4, 5, 6)
    g.agregarArista(5, 6, 9)

    # Aplicacion del algoritmo de dijkstra al grafo
    print("\n\nLa ruta mas rapida por Dijkstra junto con su costo es:")
    g.dijkstra(1)  # Aqui se indica el vertice inicial
    print(g.camino(5))  # Aqui se indica el vertice final
    # El algoritmo devolvera el camino mas corto (una lista de los vertices por los que pasa) y la distancia recorrida

    # A continuacion se indicara, para cada vertice, la distancia mas corta respecto al vertice inicial, y el vertice
    # desde donde viene para minimizar la distancia
    print("\nLos valores finales de la grafica son los siguientes:")
    g.imprimirGrafica()

# NOTAS:
# Se pueden revisar los siguientes videos, si es necesario:
# Teoria del Algoritmo de Dijkstra: https://www.youtube.com/watch?v=P9vbiZZUYkI
# Algoritmo de Dijkstra en python I - Creacion de grafos: https://www.youtube.com/watch?v=hoE38ao9m7c
# Algoritmo de Dijkstra en python II - Implementacion del algoritmo de Dijkstra: https://www.youtube.com/watch?v=wYyrMnfPmMw
