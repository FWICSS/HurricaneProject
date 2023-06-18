import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd

data = pd.read_csv("../Hurricanes/IRMA.csv")

years = data["year"].unique()

# Création de la figure et de l'axe
fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())
trajectories = []

for year in years:
    print(year)
    data_sid = data[data["year"] == year]
    print(data_sid)
    ax.plot(data_sid["LON"], data_sid["LAT"], marker='o', transform=ccrs.PlateCarree())

# # Traçage de la courbe de la trajectoire
# ax.plot(data["LON"], data["LAT"], marker='o', color='red', transform=ccrs.PlateCarree())

# Ajout des fonctionnalités cartographiques
ax.coastlines()
ax.gridlines()
ax.set_extent([-100, -60, 10, 40], crs=ccrs.PlateCarree())

# Affichage du graphique
plt.show()
fig.savefig("IRMA.png")

