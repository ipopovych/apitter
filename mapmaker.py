from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster
import folium
import os


def geoloc(location):
    geolocator = Nominatim()
    loc = geolocator.geocode(location, timeout=100)
    return (loc.latitude, loc.longitude) if loc else None


def createmap(data):
    """

    """
    m = folium.Map(data[0][1], zoom_start=12, tiles='OpenStreetMap')
    friends_cluster = MarkerCluster(name='Friends Tags').add_to(m)

    n_markers = len(data)
    for i in range(n_markers):
        if data[i][1]:
            popup = folium.Popup(data[i][0], parse_html=True)
            folium.Marker(data[i][1],
                          popup=popup,
                          icon=folium.Icon(color='black'),
                          ).add_to(friends_cluster)

    folium.plugins.Fullscreen().add_to(m)
    folium.LayerControl().add_to(m)
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'templates/friendsmap.html')
    m.save(file_path)
    print("Map created successfully. Saved as: {}".format(file_path))
    return file_path