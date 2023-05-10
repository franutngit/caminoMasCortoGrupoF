"""Clase para los datos del grafo: vertices y aristas"""


class Datos:
    @staticmethod
    def vertices():
        # VERTICES del grafo enlistados
        # Conjunto de todos los vertices del grafo:
        # Aqui cada vertice ha sido nombrado como las esquinas de un mapa, con excepcion de los vertices de inicio y fin
        # Se usan estos vertices para crear las aristas (tener en cuenta las posiciones en la lista, por los indices)
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
        return v

    @staticmethod
    def aristas(v):
        # ARISTAS del grafo enlistadas
        # 'a' es el conjunto de todas las aristas del grafo
        # Cada elemento de 'a' es una arista que contiene tres elementos:
        # el primero es el vertice inicial de la arista, el segundo es el final, el ultimo la distancia entreambos
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
             [v[8], v[16], 50],
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
             [v[16], v[9], 50]]
        return a