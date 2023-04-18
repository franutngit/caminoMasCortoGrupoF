import osmnx as ox
import networkx as nx
from geopy.geocoders import Photon
import folium
import socket
socket.getaddrinfo('localhost', 8080)

geolocator = Photon(user_agent="my_application_name", timeout=10, domain='https://api.openstreetmap.org', scheme='http')

city = 'New York City, New York, USA'
G = ox.graph_from_place(city, network_type='drive')

# Agregar atributos de velocidad y distancia a los bordes
G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)

geolocator = Photon(user_agent="geoapiExercises", timeout=10, domain='https://photon.komoot.io', scheme='https')
origin_location = geolocator.geocode("Times Square, New York")
destination_location = geolocator.geocode("Empire State Building, New York")

origin = (origin_location.latitude, origin_location.longitude)
destination = (destination_location.latitude, destination_location.longitude)

# Verificar si los nodos de origen y destino están dentro de la ciudad
city_bbox = ox.utils_geo.bbox_from_point(ox.geocode(city))
orig_node, orig_dist = ox.distance.nearest_nodes(G, origin[0], origin[1], return_dist=True)
dest_node, dest_dist = ox.distance.nearest_nodes(G, destination[0], destination[1], return_dist=True)
if orig_dist > 100:
    print('El origen está lejos de la red vial')
if dest_dist > 100:
    print('El destino está lejos de la red vial')

# Calcular el camino más corto utilizando el tiempo de viaje estimado
route = nx.shortest_path(G, orig_node, dest_node, weight='travel_time')

# Crear un mapa centrado en Nueva York
map_center = [40.7589, -73.9851]
m = folium.Map(location=map_center, zoom_start=13)

# Agregar marcadores para el origen y el destino
folium.Marker(location=origin, icon=folium.Icon(color='blue')).add_to(m)
folium.Marker(location=destination, icon=folium.Icon(color='green')).add_to(m)

# Agregar una capa de ruta
route_coords = []
for node in route:
    route_coords.append(tuple(reversed(ox.get_node(G, node)['x_y'])))
folium.PolyLine(locations=route_coords, color='red', weight=5).add_to(m)

# Mostrar el mapa
m
