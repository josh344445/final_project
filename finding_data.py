import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import gmaps
with open("graffiti_requests.csv") as f:
    reader = csv.reader(f)
    headers = next(reader, None)
    column = {}
    for h in headers:
        column[h] = []

    for row in reader:
        for h, v in zip(headers, row):
            if h in ('lat', 'long'):
                column[h].append(float(v.strip()))
            else:
                column[h].append(v)
    locations = np.column_stack((column['lat'], column['long']))
    fig = gmaps.figure()
    fig.add_layer(gmaps.heatmap_layer(locations, point_radius=20))
    fig
