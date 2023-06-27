from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
from netCDF4 import Dataset

fig = plt.figure(figsize=(12, 12))

# Open, store lat-lon-air_temp variables and close the .nc file
T = Dataset("subset (4).nc", "r", format='NETCDF4_CLASSIC')

L1 = T.variables['lon'][:]
L2 = T.variables['lat'][:]
Heat = T.variables['sst'][:]

T.close()

# Store collected dataset in Meshgrid fashion for plotting
lon, lat = np.meshgrid(L1, L2)


def update(frame):
    plt.clf()
    m = Basemap(projection='ortho', resolution='l', lat_0=0, lon_0=frame)
    xi, yi = m(lon, lat)
    m.contourf(xi, yi, Heat[0], 20, cmap='rainbow')
    m.drawcoastlines()
    m.drawcountries()
    m.drawparallels(np.arange(-80., 81., 20.))
    m.drawmeridians(np.arange(-180., 181., 20.))


ani = FuncAnimation(fig, update, frames=range(-180, 181, 1), repeat=False)

ani.save('Earth Rotation Test 2.mp4', FFMpegWriter(fps=30))
