import folium
import networkx as nx
from geopy.distance import geodesic

def shortest_path(start, end, waypoints):
    # Crear el grafo
    G = nx.Graph()

    # Agregar los puntos de inicio y fin al grafo
    G.add_node('Start', pos=start)
    G.add_node('End', pos=end)

    # Agregar los puntos intermedios al grafo
    for i, waypoint in enumerate(waypoints):
        G.add_node(f'Waypoint{i}', pos=waypoint)

    # Calcular las distancias entre los puntos
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            node1, node2 = nodes[i], nodes[j]
            dist = geodesic(G.nodes[node1]['pos'], G.nodes[node2]['pos']).meters
            G.add_edge(node1, node2, weight=dist)

    # Encontrar el camino más corto utilizando el algoritmo Dijkstra
    path = nx.dijkstra_path(G, 'Start', 'End', weight='weight')

    return path

# Coordenadas de ejemplo
start_coord = (-32.897330, -68.853555)  # Nueva York
end_coord = (-32.904422, -68.842819)  # Los Ángeles
waypoints_coords = []  # Chicago y Filadelfia

# Encontrar el camino más corto
path_coords = shortest_path(start_coord, end_coord, waypoints_coords)

# Crear el mapa
map = folium.Map(location=start_coord, zoom_start=4)

# Agregar marcadores al mapa
for i, coord in enumerate(path_coords):
    if coord == 'Start':
        folium.Marker(start_coord, popup='Start').add_to(map)
    elif coord == 'End':
        folium.Marker(end_coord, popup='End').add_to(map)
    else:
        folium.Marker(coord, popup=f'Waypoint {i}').add_to(map)

# Agregar la línea que representa el camino más corto al mapa
polyline_coords = []
for coord in path_coords:
    if coord == 'Start':
        polyline_coords.append(start_coord)
    elif coord == 'End':
        polyline_coords.append(end_coord)
    else:
        polyline_coords.append(coord)

folium.PolyLine(polyline_coords, color='blue', weight=2.5, opacity=1).add_to(map)

# Mostrar el mapa
map
map.save("map.html")
