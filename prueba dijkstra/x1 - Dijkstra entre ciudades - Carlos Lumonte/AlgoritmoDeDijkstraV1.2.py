""" Codigo de Algoritmo de Dijkstra version 1.0 - MDI."""
import heapq


# Definimos la función que implementa el algoritmo de Dijkstra
def dijkstraV1_2(graphs, start, end):
    # Creamos un diccionario para almacenar las distancias más cortas entre los nodos
    distances = {node: float('inf') for node in graphs}
    # La distancia desde el nodo de inicio a sí mismo es cero
    distances[start] = 0
    # Creamos un diccionario para almacenar el camino más eficiente hasta cada nodo
    path = {}
    # Creamos una cola de prioridad usando el módulo heapq
    pq = [(0, start)]
    while pq:
        # Extraemos el nodo con la menor distancia desde la cola de prioridad
        current_distance, current_node = heapq.heappop(pq)
        # Si hemos visitado este nodo anteriormente, pasamos al siguiente
        if current_distance > distances[current_node]:
            continue
        # Si hemos llegado al nodo de destino, terminamos la búsqueda
        if current_node == end:
            break
        # Para cada nodo adyacente al nodo actual
        for neighbor, weight in graphs[current_node].items():
            # Calculamos la distancia provisional al nodo adyacente
            distance = current_distance + weight
            # Si la distancia provisional es menor que la distancia almacenada anteriormente, actualizamos
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Actualizamos el camino más eficiente hasta el nodo adyacente
                path[neighbor] = current_node
                # Agregamos el nodo a la cola de prioridad
                heapq.heappush(pq, (distance, neighbor))
    # Construimos el camino más eficiente desde el nodo de inicio hasta el nodo de destino
    shortest_path = []
    current = end
    while current != start:
        shortest_path.append(current)
        current = path[current]
    shortest_path.append(start)
    shortest_path.reverse()
    # Devolvemos el camino más eficiente y la distancia recorrida
    return shortest_path, distances[end]


# Creamos el grafo como un diccionario de diccionarios
graph = {
    'Capital': {'Godoy Cruz': 3, 'Guaymallen': 8, 'Las Heras': 6, 'Lujan de Cuyo': 19},
    'General Alvear': {'San Rafael': 144, 'Malargue': 211, 'Santa Rosa': 196},
    'Godoy Cruz': {'Capital': 3, 'Guaymallen': 8, 'Las Heras': 6},
    'Guaymallen': {'Capital': 8, 'Godoy Cruz': 3, 'Las Heras': 6, 'Maipu': 14},
    'Junin': {'Rivadavia': 13, 'San Martin': 40, 'Santa Rosa': 69},
    'La Paz': {'Lavalle': 109, 'Rivadavia': 161, 'San Martin': 161, 'Santa Rosa': 51},
    'Las Heras': {'Capital': 6, 'Godoy Cruz': 8, 'Guaymallen': 14, 'Lujan de Cuyo': 19, 'Maipu': 19, 'San Carlos': 65},
    'Lavalle': {'La Paz': 109, 'Maipu': 137, 'San Martin': 53, 'Santa Rosa': 103},
    'Lujan de Cuyo': {'Capital': 19, 'Las Heras': 6, 'Maipu': 14, 'San Carlos': 65},
    'Maipu': {'Guaymallen': 14, 'Las Heras': 6, 'Lavalle': 109, 'Lujan de Cuyo': 19, 'San Martin': 40},
    'Malargue': {'San Rafael': 266, 'General Alvear': 211},
    'Rivadavia': {'Junin': 13, 'La Paz': 161, 'San Martin': 40, 'Santa Rosa': 69},
    'San Carlos': {'Lujan de Cuyo': 69, 'Las Heras': 65, 'Tunuyan': 45, 'Tupungato': 35},
    'San Martin': {'Junin': 40, 'La Paz': 30, 'Lavalle': 60, 'Maipu': 45, 'Rivadavia': 15, 'Santa Rosa': 55},
    'San Rafael': {'Malargue': 266, 'Tunuyan': 151, 'Tupungato': 185, 'General Alvear': 144},
    'Santa Rosa': {'Junin': 69, 'La Paz': 51, 'Lavalle': 33, 'Rivadavia': 63, 'San Martin': 45, 'General Alvear': 196},
    'Tunuyan': {'San Carlos': 65, 'Tupungato': 30, 'San Rafael': 151},
    'Tupungato': {'San Carlos': 65, 'Tunuyan': 30, 'San Rafael': 185}
}

# argumentos que tomaran los parametros
inicio = 'Capital'
fin = 'Las Heras'
mi_lista = list(dijkstraV1_2(graph, inicio, fin))

# valores que retorna la funcion
caminoMasCorto = mi_lista[0]
distancia = mi_lista[1]

# mostrar datos devueltos
msj = ""
for l in caminoMasCorto:
    msj += l
    if (l != fin):
        msj += "', luego '"
print(
    f"El camino mas corto es '{msj}' con un total de {distancia} kilometros.")
