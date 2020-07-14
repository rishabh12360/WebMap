
import folium
import pandas, io

data = pandas.read_csv ("Volcanoes.txt")
data_json = io.open ("world.json", 'r', encoding='utf-8-sig').read ()
lat = list (data.LAT)
lon = list (data.LON)
elev = list (data.ELEV)


def colour_producer(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev < 3000:
        return "orange"
    else:
        return "red"


Map = folium.Map (location=[38.58, -99.09], zoom_start=6, )
fgv = folium.FeatureGroup (name="Volcanoes")

for lat, lon, elev in zip (lat, lon, elev):
    fgv.add_child (folium.CircleMarker (location=[lat, lon], popup=str (elev) + "m", radius
    =6, fill_color=colour_producer (elev),
                                       color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup (name="Population")

fgp.add_child (folium.GeoJson (data=data_json, style_function=lambda x: {'fillColor': 'blue' if x['properties']
['POP2005'] < 10000000 else 'green' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
Map.add_child (fgv)
Map.add_child(fgp)
Map.add_child(folium.LayerControl())
Map.save ("Map1.html")
