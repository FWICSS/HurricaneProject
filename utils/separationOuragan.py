import pandas as pd


def getNumberOfHurricane(data: pd.DataFrame):
    ouragans = getSeparedHurricane(data)
    return len(ouragans)
    # # Afficher les données de chaque ouragan
    # for i, ouragan_data in enumerate(ouragans):
    #     print(f"\n Ouragans {ouragan_data['NAME'].values[0]} "
    #           f"de {ouragan_data['Hurricane_Date'].min()} "
    #           f"a {ouragan_data['Hurricane_Date'].max()} ")

def getSeparedHurricane(data: pd.DataFrame):
    grouped = data.groupby('SID')
    list_of_dataframes = []
    for group_name, group_data in grouped:
        # Crée un nouveau DataFrame pour chaque groupe
        grouped_df = pd.DataFrame(group_data)

        # Ajoute le DataFrame à la liste
        list_of_dataframes.append(grouped_df)

    return list_of_dataframes

def getSeparedHurricaneByName(data: pd.DataFrame):
    grouped = data.groupby(['NAME','year'])
    list_of_dataframes = []
    for group_name, group_data in grouped:
        # Crée un nouveau DataFrame pour chaque groupe
        grouped_df = pd.DataFrame(group_data)

        # Ajoute le DataFrame à la liste
        list_of_dataframes.append(grouped_df)

    return list_of_dataframes

def getOcurrenceDataframe(dataframes):
    # Dictionnaire pour stocker le nombre d'occurrences de lignes de chaque DataFrame
    occurrences = {}

    # Parcours de la liste de DataFrames
    for df in dataframes:
        num_rows = df.shape[0]  # Récupère le nombre de lignes du DataFrame
        if num_rows in occurrences:
            occurrences[num_rows] += 1  # Incrémente le compteur d'occurrences pour ce nombre de lignes
        else:
            occurrences[num_rows] = 1  # Initialise le compteur d'occurrences pour ce nombre de lignes

    # Trouve le maximum d'occurrences de lignes
    max_occurrences = max(occurrences.values())
    key_max_occurrences = max(occurrences, key=occurrences.get)
    print(key_max_occurrences)
    # Trouve les clés correspondant à la valeur maximale
    keys_with_max_occurrences = [key for key, val in occurrences.items() if val == max_occurrences]

    # Liste des DataFrames ayant le maximum d'occurrences de lignes

    dataframes_with_max_occurrences = []
    for df in dataframes:
        if df.shape[0] == key_max_occurrences:
            dataframes_with_max_occurrences.append(df)

    # print(dataframes_with_max_occurrences)
    #
    # Affichage des résultats
    print(f"Maximum d'occurrences de lignes : {max_occurrences}")
    print(f"Clés correspondant à la valeur maximale : {keys_with_max_occurrences}")
    print(f"{occurrences[keys_with_max_occurrences[0]]}")
    print("DataFrames ayant le maximum d'occurrences de lignes :")

    for df in dataframes_with_max_occurrences:
        print(df["NAME"].unique())



if __name__ == '__main__':
    data = pd.read_csv("../data/hurricanes_Past_In_Caribbean.csv")
    data_caribean = getSeparedHurricaneByName(data)
    getOcurrenceDataframe(data_caribean)


