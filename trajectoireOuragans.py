import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd
import os

data = pd.read_csv("data/hurricanes_Past_In_Caribbean.csv", low_memory=False)
plt.rcParams['agg.path.chunksize'] = 2000
plt.rcParams['path.simplify_threshold'] = 0.5
data = data[data["NAME"] != "NOT_NAMED"]
name_ouragans = data["NAME"].unique()
# Boucle sur chaque ouragan
for name_ouragan in name_ouragans:

    # Filtrer les données pour l'ouragan courant
    data_ouragans = data[data["NAME"] == name_ouragan]
    year_ouragans = data_ouragans["year"].unique()

    for year_ouragan in year_ouragans:
        data_ouragan = data_ouragans[data_ouragans["year"] == year_ouragan]
        # Obtenir les valeurs minimales et maximales de latitude et de longitude
        min_lat = data_ouragan["LAT"].min()
        max_lat = data_ouragan["LAT"].max()
        min_lon = data_ouragan["LON"].min()
        max_lon = data_ouragan["LON"].max()
        # Calculer une marge pour étendre légèrement l'étendue de la carte
        margin = 1.0

        extent = [min_lon - margin, max_lon + margin, min_lat - margin, max_lat + margin]

        # Créer une nouvelle figure pour l'ouragan courant
        fig = plt.figure(figsize=(10, 6))
        ax = plt.axes(projection=ccrs.PlateCarree())

        # Tracer la courbe de trajectoire pour l'ouragan courant
        ax.plot(data_ouragan["LON"], data_ouragan["LAT"], marker='o', transform=ccrs.PlateCarree())

        # Ajouter des fonctionnalités cartographiques
        ax.coastlines()
        ax.gridlines()
        ax.set_extent(extent, crs=ccrs.PlateCarree())

        # Titre du graphique
        plt.title(f"Trajectoire de l'ouragan {name_ouragan} {year_ouragan}")

        # Afficher le graphique
        plt.show()

        # Enregistrer le graphique dans un fichier PNG
        folder_name = f"Trajectoire/{year_ouragan}"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        name = name_ouragan.replace(":", "-")
        filename = f'{folder_name}/{name}_{year_ouragan}.png'
        fig.savefig(filename)

