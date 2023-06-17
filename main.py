
import pandas as pd
import os

name_huricane  = '';
data = '';
# Press the green button in the gutter to run the script.
def getNamesHuricanes():
    df = pd.read_csv("data/Historical_Hurricane_Tracks.csv")
    unique_hurricanes = df["NAME"].unique()
    for name_hurricane in unique_hurricanes:
        print(name_hurricane)

    df = df[df["NAME"] != "NOT_NAMED"]
    print(df)
    df.to_csv("Hurricane_Name.csv")

def setCsvByHurricanes():
    dataHurricanes = pd.read_csv("data/Hurricane_Name.csv")
    unique_Hurricanes = dataHurricanes["NAME"].unique()
    folder_name = 'Hurricanes'

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    for hurricanes in unique_Hurricanes:
        filter_Hurricanes = dataHurricanes[dataHurricanes["NAME"] == hurricanes]
        hurricane = hurricanes.replace(":", "-")
        filename = f'{folder_name}/{hurricane}.csv'
        filter_Hurricanes.to_csv(filename, index=False)

def listOFBassin():
    dataHurricanes = pd.read_csv("data/Hurricane_Name.csv")
    unique_Bassin = dataHurricanes["BASIN"].unique()
    print(f"\n list des basins : {unique_Bassin}")

def setCsvByCountry():
    dataByCountry = pd.read_csv("data/data_1686321075.csv")
    #dataLatinAmericaAndCaraibes = pd.read_csv("data_1686320929.csv")
    unique_countries = dataByCountry['Country__ESTANDAR'].unique()
    # Créer le dossier 'Country' s'il n'existe pas déjà
    folder_name = 'Country'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    for country in unique_countries:
        # Filtrer les lignes où la colonne 'Country__ESTANDAR' est égale à la valeur actuelle
        filtered_df = dataByCountry[dataByCountry['Country__ESTANDAR'] == country]

        # Enregistrer les données filtrées dans un fichier CSV avec le nom de la valeur
        filename = f'{folder_name}/{country}.csv'
        filtered_df.to_csv(filename, index=False)

if __name__ == '__main__':
        print(f"""
        1. Lire les fichier
        2. Netoyer les données
            supprimer les ouragans si on ne connais aucun de leur basins
        3. Faire un graphique par Ouragan (trajectoire)
        4. Compare les trajectoire
        5. Analyser les trajectoire par année
        """)
        setCsvByHurricanes()
#%%
