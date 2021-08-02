import json

# Explore the structure of the data
filename = "data/eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

magnitudes, longitudes, latitudes = [], [], []
for eq_dict in all_eq_dicts:
    magnitude = eq_dict['properties']['mag']
    longitude = eq_dict['geometry']['coordinates'][0]
    latitude = eq_dict['geometry']['coordinates'][1]
    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)

print(magnitudes[:10])
print(longitudes[:5])
print(latitudes[:5])
