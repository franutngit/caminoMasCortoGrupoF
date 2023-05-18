import folium
import osmnx as ox
import networkx as nx

# Coordenadas de ejemplo
start_coord = (-32.897330, -68.853555)  # Utn
end_coord = (-32.904422, -68.842819)  # Casino de Mendoza

# Obtener el grafo de la red de calles en un área cercana al punto de inicio para conducción en auto
graph = ox.graph_from_point(start_coord, dist=3000, network_type='drive')

# Convertir el grafo a un grafo no dirigido para encontrar la ruta más corta
graph = graph.to_undirected()

# Agregar los nodos de inicio y fin al grafo
start_node = ox.distance.nearest_nodes(graph, start_coord[1], start_coord[0])
end_node = ox.distance.nearest_nodes(graph, end_coord[1], end_coord[0])
graph.add_nodes_from([(start_node, {'pos': start_coord}), (end_node, {'pos': end_coord})])

# Encontrar el camino más corto utilizando el algoritmo Dijkstra
path = nx.shortest_path(graph, start_node, end_node, weight='length')

# Obtener las coordenadas de los nodos en el camino más corto
path_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in path]

# Crear el mapa
map = folium.Map(location=start_coord, zoom_start=14)

# Agregar marcadores al mapa
folium.Marker(start_coord, popup='Start').add_to(map)
folium.Marker(end_coord, popup='End').add_to(map)

# Agregar la línea que representa el camino más corto al mapa
folium.PolyLine(path_coords, color='blue', weight=2.5, opacity=1).add_to(map)

# Mostrar el mapa
map.save("map.html")
