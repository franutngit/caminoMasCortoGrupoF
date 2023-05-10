"""Prueba Dijkstra - Sexto ajuste: Modularizacion"""

from grafo import Grafo
from datos import Datos as dat
from usuario import Usuario as user

"""Datos: Vertices y Aristas"""
v = dat.vertices()
a = dat.aristas(v)

'''Armado del grafo'''
graf = Grafo()
for e in v:
    graf.agregarVertice(e)
for e in a:
    graf.agregarArista(e[0], e[1], e[2])

'''Interaccion con el usuario'''

o = user.origen(v)
print(f'ORIGEN escogido: {o}\n')
d = user.destino(v)
print(f'DESTINO escogido: {d}')

'''Camino mas corto mediante Dijkstra'''
# Se aplica el algoritmo con el vertice inicial
graf.dijkstra(o)
# Se muestra el camino mas corto con los vertices inicial y final
print(graf.camino(o, d))
