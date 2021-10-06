import json

infile = open('eq_data_30_day_m1.json','r')
outfile = open('readable_eq_data.json','w')

eq_data = json.load(infile)             #take raw file and convert that into a python dictionary

json.dump(eq_data, outfile, indent = 4)  #indent 4 levels deep
list_of_eqs = eq_data['features'] #trying to get certain lines in the readable file, line etc, use type and print
#represent a list (the features)
#there is a 158 earthquakes, each earthquake is a dictionary with
mags= []
lons = []
lats = []

#eq going through each earthquake which a each dictionary
for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

#same thing, see first 5 elements of the list
print(mags[0:5])
print(lons[:5])
print(lats[:5])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title = "Global Earthquake 1 Day")

#combines figure data
fig = {'data': data, 'layout':my_layout}

#plot figure and give it this filename
offline.plot(fig,filename='globaleathquake1day.html')
#need magnitude to tell how big the earthquakes are
