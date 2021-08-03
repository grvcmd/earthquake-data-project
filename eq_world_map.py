import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data/readable_eq_data.json"
with open(filename) as f:
    all_earthquake_data = json.load(f)

# Create a list of all the earthquakes
all_earthquake_dicts = all_earthquake_data['features']

# Extract magnitude, longitude, and latitude of all eqs
magnitudes, longitudes, latitudes = [], [], []
for earthquake_dict in all_earthquake_dicts:
    magnitude = earthquake_dict['properties']['mag']
    longitude = earthquake_dict['geometry']['coordinates'][0]
    latitude = earthquake_dict['geometry']['coordinates'][1]
    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)

# Map the earthquakes
data = [Scattergeo(lon=longitudes, lat=latitudes)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
