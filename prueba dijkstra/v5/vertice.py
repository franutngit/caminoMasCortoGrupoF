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