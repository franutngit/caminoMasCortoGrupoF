import folium
import osmnx as ox
import networkx as nx
import requests

# Función para obtener las coordenadas geográficas a partir de una dirección
def geocode_address(address):
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': address,
        'format': 'json',
        'limit': 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            return float(data[0]['lat']), float(data[0]['lon'])
    return None

# Direcciones de ejemplo
start_address = 'Av. España 123, Mendoza, Mendoza, Argentina'
end_address = 'Avenida General San Martín 456, Mendoza, Mendoza, Argentina'

# Obtener las coordenadas geográficas de las direcciones
start_coord = geocode_address(start_address)
end_coord = geocode_address(end_address)

if start_coord is not None and end_coord is not None:
    # Obtener el grafo de la red de calles en un área cercana al punto de inicio para conducción en auto
    graph = ox.graph_from_point(start_coord, dist=3000, network_type='drive', simplify=True)

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
else:
    print("No se pudieron obtener las coordenadas para las direcciones especificadas.")
