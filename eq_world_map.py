import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data/eq_data_30_day_m1.json"
with open(filename) as f:
    all_earthquake_data = json.load(f)

# Create a list of all the earthquakes
all_earthquake_dicts = all_earthquake_data['features']

# Extract magnitude, longitude, and latitude of all eqs
magnitudes, longitudes, latitudes, hover_texts = [], [], [], []
for earthquake_dict in all_earthquake_dicts:
    magnitude = earthquake_dict['properties']['mag']
    longitude = earthquake_dict['geometry']['coordinates'][0]
    latitude = earthquake_dict['geometry']['coordinates'][1]
    title = earthquake_dict['properties']['title']
    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)
    hover_texts.append(title)

# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'text': hover_texts,
    'marker': {
        'size': [5*magnitude for magnitude in magnitudes],
        'color': magnitudes,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': "Magnitude"},
    }
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
