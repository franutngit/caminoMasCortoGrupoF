"""Prueba Dijkstra - Sexto ajuste: Modularizacion"""

from grafo import Grafo
from datos import Datos as dat
from usuario import Usuario

"""Datos: Vertices y Aristas"""
v = dat.vertices()
a = dat.aristas(v)

'''Armado del grafo'''
g = Grafo()
for e in v:
    g.agregarVertice(e)
for e in a:
    g.agregarArista(e[0], e[1], e[2])

'''Interaccion con el usuario'''

o = Usuario().origen(v)
print(f'ORIGEN escogido: {o}\n')
d = Usuario().destino(v)
print(f'DESTINO escogido: {d}')

'''Camino mas corto mediante Dijkstra'''
# Se aplica el algoritmo con el vertice inicial
g.dijkstra(o)
# Se muestra el camino mas corto con los vertices inicial y final
print(g.camino(o, d))
