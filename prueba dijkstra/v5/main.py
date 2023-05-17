"""Prueba Dijkstra - Sexto ajuste: Modularizacion"""

from grafo import Grafo
from datos import Datos as dato
from usuario import Usuario as usuarios

"""Datos: Vertices y Aristas"""
vertices = dato.vertices()
aristas = dato.aristas(vertices)

'''Armado del grafo'''
grafo = Grafo()
for idVertice in vertices:
    grafo.agregarVertice(idVertice)
for arista in aristas:
    grafo.agregarArista(arista[0], arista[1], arista[2])

'''Interaccion con el usuario'''
# Se consulta al usuario cual debe ser el vertice de origen
origen = usuarios.origen(vertices)
print(f'ORIGEN escogido: {origen}\n')
# Se consulta al usuario cual debe ser el vertice de destino
destino = usuarios.destino(vertices)
print(f'DESTINO escogido: {destino}')

'''Camino mas corto mediante Dijkstra'''
# Se aplica el algoritmo desde el vertice de origen
grafo.dijkstra(origen)
# Se muestra el camino mas corto desde los vertices origen y destino
print(grafo.camino(origen, destino))
