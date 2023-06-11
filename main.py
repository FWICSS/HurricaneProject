
import pandas as pd
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataByCountry = pd.read_csv("data_1686321075.csv")
    dataLatinAmericaAndCaraibes = pd.read_csv("data_1686320929.csv")
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



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
