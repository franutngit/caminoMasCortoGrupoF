import folium
import osmnx as ox
import networkx as nx
import requests
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading

# Función para obtener las coordenadas geográficas a partir de una dirección
def geocode_address(country, province, department, address):
    location = f"{address}, {department}, {province}, {country}"
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': location,
        'format': 'json',
        'limit': 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            return float(data[0]['lat']), float(data[0]['lon'])
    return None

def calculate_distance(start_coord, end_coord):
    return ox.distance.great_circle_vec(start_coord[0], start_coord[1], end_coord[0], end_coord[1])

def get_directions():
    def process_directions():
        start_country = start_country_entry.get()
        start_province = start_province_entry.get()
        start_department = start_department_entry.get()
        start_address = start_address_entry.get()

        end_country = end_country_entry.get()
        end_province = end_province_entry.get()
        end_department = end_department_entry.get()
        end_address = end_address_entry.get()

        # Deshabilitar el botón de obtener direcciones
        get_directions_button.configure(state='disabled')

        # Obtener las coordenadas geográficas de las direcciones de origen y destino
        start_coord = geocode_address(start_country, start_province, start_department, start_address)
        end_coord = geocode_address(end_country, end_province, end_department, end_address)

        if start_coord is not None and end_coord is not None:
            # Calcular la distancia entre el punto de inicio y el punto de destino
            distance = calculate_distance(start_coord, end_coord)

            # Obtener el grafo de la red de calles en un área cercana al punto de inicio para conducción en auto
            graph = ox.graph_from_point(start_coord, dist=distance, network_type='drive', simplify=True)

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
            map.save("Camino mas corto.html")
            webbrowser.open_new_tab('Camino mas corto.html')

            # Cerrar la ventana principal y finalizar el programa para que se termine de ejecutar el bucle
            window.quit()
           
        else:
            messagebox.showerror("Error", "No se pudieron obtener las coordenadas para las direcciones especificadas.")

            # Restaurar el estado inicial
            get_directions_button.configure(state='normal')

    # Crear un hilo para ejecutar el procesamiento de direcciones
    directions_thread = threading.Thread(target=process_directions)
    directions_thread.start()

# Crear la ventana principal
window = tk.Tk()
window.title("Ruta más corta")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Personalizar estilo de fuente
font_style = ("Arial", 14)

# Marco para las direcciones de origen
frame_start = ttk.Frame(window, padding=20)
frame_start.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

start_label = ttk.Label(frame_start, text="Dirección de origen:", font=font_style)
start_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

start_country_label = ttk.Label(frame_start, text="País:", font=font_style)
start_country_label.grid(row=1, column=0, padx=10, pady=5)
start_country_entry = ttk.Entry(frame_start, font=font_style)
start_country_entry.grid(row=1, column=1, padx=10, pady=5)

start_province_label = ttk.Label(frame_start, text="Provincia:", font=font_style)
start_province_label.grid(row=2, column=0, padx=10, pady=5)
start_province_entry = ttk.Entry(frame_start, font=font_style)
start_province_entry.grid(row=2, column=1, padx=10, pady=5)

start_department_label = ttk.Label(frame_start, text="Departamento:", font=font_style)
start_department_label.grid(row=3, column=0, padx=10, pady=5)
start_department_entry = ttk.Entry(frame_start, font=font_style)
start_department_entry.grid(row=3, column=1, padx=10, pady=5)

start_address_label = ttk.Label(frame_start, text="Dirección:", font=font_style)
start_address_label.grid(row=4, column=0, padx=10, pady=5)
start_address_entry = ttk.Entry(frame_start, font=font_style)
start_address_entry.grid(row=4, column=1, padx=10, pady=5)

# Marco para las direcciones de destino
frame_end = ttk.Frame(window, padding=20)
frame_end.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

end_label = ttk.Label(frame_end, text="Dirección de destino:", font=font_style)
end_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

end_country_label = ttk.Label(frame_end, text="País:", font=font_style)
end_country_label.grid(row=1, column=0, padx=10, pady=5)
end_country_entry = ttk.Entry(frame_end, font=font_style)
end_country_entry.grid(row=1, column=1, padx=10, pady=5)

end_province_label = ttk.Label(frame_end, text="Provincia:", font=font_style)
end_province_label.grid(row=2, column=0, padx=10, pady=5)
end_province_entry = ttk.Entry(frame_end, font=font_style)
end_province_entry.grid(row=2, column=1, padx=10, pady=5)

end_department_label = ttk.Label(frame_end, text="Departamento:", font=font_style)
end_department_label.grid(row=3, column=0, padx=10, pady=5)
end_department_entry = ttk.Entry(frame_end, font=font_style)
end_department_entry.grid(row=3, column=1, padx=10, pady=5)

end_address_label = ttk.Label(frame_end, text="Dirección:", font=font_style)
end_address_label.grid(row=4, column=0, padx=10, pady=5)
end_address_entry = ttk.Entry(frame_end, font=font_style)
end_address_entry.grid(row=4, column=1, padx=10, pady=5)

# Botón para obtener direcciones
get_directions_button = ttk.Button(window, text="Obtener direcciones", command=get_directions, style="Accent.TButton")
get_directions_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Etiqueta para el tiempo estimado
time_label = ttk.Label(window, text="Tiempo estimado: 15 segundos", font=font_style)
time_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Centrar la ventana principal
center_window(window)

# Iniciar el bucle de la aplicación
window.mainloop() 
