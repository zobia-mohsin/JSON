from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import json

infile = open('US_fires_9_14.json', 'r')
#outfile = open('readable_eq_data.json', 'w')

# take raw file and convert that into a python dictionary
read_fires = json.load(infile)

# represent a list (the features)
brightness, lons, lats = [], [], []

# eq going through each earthquake which a each dictionary
for fire in read_fires:

    brightness_list = fire['brightness']
    if brightness_list > 450:

        lon = fire['longitude']
        lat = fire['latitude']

        lons.append(lon)
        lats.append(lat)
        brightness.append(brightness_list)
        # same thing, see first 5 elements of the list

data = [{
    'type': 'scattergeo',  # enhance size of dots on earth by mags
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [brightness_list/30 for brightness_list in brightness],
        'color': brightness,
        'colorscale':'viridis',
        'reversescale':True,
        'colorbar':{'title': 'Brightness'}
    }

}]

my_layout = Layout(title="US Fires - 9/14/2020 through 9/20/2020")

# combines figure data
fig = {'data': data, 'layout': my_layout}

# plot figure and give it this filename
offline.plot(fig, filename='US_fires_9_14.json.html')
# need magnitude to tell how big the earthquakes are
