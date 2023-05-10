"""Clase para los datos del grafo: vertices y aristas"""


class Datos:
    @staticmethod
    def vertices():
        # VERTICES del grafo enlistados
        # Conjunto de todos los vertices del grafo:
        # Aqui cada vertice ha sido nombrado como las esquinas de un mapa, con excepcion de los vertices de inicio y fin
        # Se usan estos vertices para crear las aristas (tener en cuenta las posiciones en la lista, por los indices)
        listaVertices = ['UTN',  # 0
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
        return listaVertices

    @staticmethod
    def aristas(vertices):
        # ARISTAS del grafo enlistadas
        # 'a' es el conjunto de todas las aristas del grafo
        # Cada elemento de 'a' es una arista que contiene tres elementos:
        # el primero es el vertice inicial de la arista, el segundo es el final, el ultimo la distancia entreambos
        listaAristas = [[vertices[0], vertices[1], 100],
                        [vertices[1], vertices[2], 250],
                        [vertices[1], vertices[4], 90],
                        [vertices[2], vertices[3], 75],
                        [vertices[3], vertices[7], 125],
                        [vertices[4], vertices[1], 90],
                        [vertices[4], vertices[6], 250],
                        [vertices[5], vertices[4], 250],
                        [vertices[5], vertices[2], 125],
                        [vertices[6], vertices[5], 0],
                        [vertices[6], vertices[7], 75],
                        [vertices[7], vertices[5], 75],
                        [vertices[7], vertices[11], 100],
                        [vertices[8], vertices[4], 90],
                        [vertices[8], vertices[16], 50],
                        [vertices[9], vertices[10], 120],
                        [vertices[10], vertices[6], 90],
                        [vertices[10], vertices[11], 90],
                        [vertices[11], vertices[15], 100],
                        [vertices[12], vertices[8], 90],
                        [vertices[13], vertices[9], 90],
                        [vertices[13], vertices[12], 100],
                        [vertices[14], vertices[10], 90],
                        [vertices[14], vertices[13], 120],
                        [vertices[15], vertices[14], 100],
                        [vertices[16], vertices[9], 50]]
        return listaAristas
