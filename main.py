
import pandas as pd
import os

dataHurricanesName = pd.read_csv("data/Hurricane_Name.csv")
dataHurricanes = pd.read_csv("data/Historical_Hurricane_Tracks.csv")
# allHuricanesCaribean = dataHurricanes[dataHurricanes["SUBBASIN"] == "CP"]
# allHuricanesNameCaribean = dataHurricanesName[dataHurricanesName["SUBBASIN"] == "CP"]
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

# def getHuricanesInCaribean():
#     print("\n Donnée de tous les ouragans dans la mer des caraibes  : \n")
#     print("\n",allHuricanesCaribean.info())
#     print("\n",allHuricanesCaribean.describe())
#     print("\n",allHuricanesCaribean.nunique())
#     print("\n",allHuricanesCaribean.duplicated())
#     print("\n Donnée de tous les ouragans namés dans la mer des caraibes  : \n")
#     print("\n", allHuricanesNameCaribean.info())
#     print("\n", allHuricanesNameCaribean.describe())
#     print("\n", allHuricanesNameCaribean.nunique())
#     print("\n", allHuricanesNameCaribean.duplicated())
#     print(f"""
#     Nous avons {allHuricanesCaribean.shape[0]} ouragans dans la mer des caraibes`
#     dont {allHuricanesNameCaribean.shape[0]} nommés
#     """)
#     hurricanes = allHuricanesCaribean["NAME"].unique()
#     for hurricane in hurricanes:
#         dataHurricane = allHuricanesCaribean[allHuricanesCaribean["NAME"] == hurricane]
#         print("\n il y a : ", dataHurricane.shape[0], "données pour l'ouragan : ", hurricane)


def setCsvByHurricanes():
    unique_Hurricanes = dataHurricanesName["NAME"].unique()
    folder_name = 'Hurricanes'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    for hurricanes in unique_Hurricanes:
        filter_Hurricanes = dataHurricanesName[dataHurricanesName["NAME"] == hurricanes]
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

def getCaribbeanData():
    data = pd.read_csv("data/Hurricane_Name.csv")
    # Définir les limites de la région des Caraïbes
    lat_min, lat_max = 5, 25
    lon_min, lon_max = -100, -55

    caribbean_data = data[
        (data['LAT'] >= lat_min) &
        (data['LAT'] <= lat_max) &
        (data['LON'] >= lon_min) &
        (data['LON'] <= lon_max)]

    hurricanes_past_in_caribbean = []

    for _, row in caribbean_data.iterrows():
        name = row['NAME']
        year = row['year']
        hurricane_data_caribbean = caribbean_data[
            (caribbean_data['NAME'] == name) &
            (caribbean_data['year'] == year)]

        if name in [h['NAME'] for h in hurricanes_past_in_caribbean]:
            for h in hurricanes_past_in_caribbean:
                if h['NAME'] == name:
                    h['data'].append(hurricane_data_caribbean)
                    break
        else:
            hurricanes_past_in_caribbean.append(
                {'NAME': name, 'data': [hurricane_data_caribbean]})

    output_data = []
    for hurricane in hurricanes_past_in_caribbean:
        for data in hurricane['data']:
            output_data.append(data)

    output_df = pd.concat(output_data)
    output_df.to_csv('data/hurricanes_Past_In_Caribbean.csv', index=False)

if __name__ == '__main__':
        print(f"""
        Fait :
        1. Lire les fichier
        Ce qu'il reste a faire :
        2. Netoyer les données
            supprimer les ouragans si on ne connais aucun de leur basins
        3. Faire un graphique par Ouragan (trajectoire)
        
        
        À faire :
        4. Compare les trajectoire
        5. Analyser les trajectoire par année
        6. Analyser les puissance des ourgans par année
        7. Comparer les puissance des ourgans
        """)

#%%
