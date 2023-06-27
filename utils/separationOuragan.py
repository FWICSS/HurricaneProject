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
    # Convertir la colonne "Hurricane_Date" en type datetime
    data["Hurricane_Date"] = pd.to_datetime(data["Hurricane_Date"])

    # Calculer la différence entre les dates consécutives
    data["Date_Diff"] = data["Hurricane_Date"].diff()

    # Définir une durée minimale d'interruption pour considérer un nouvel ouragan (2 jours dans cet exemple)
    min_interruption = pd.Timedelta(days=2)

    # Identifier les positions où l'interruption dépasse la durée minimale
    interruption_indices = data[data["Date_Diff"] > min_interruption].index

    # Diviser les données en plusieurs ouragans
    ouragans = []
    start_index = 0
    for end_index in interruption_indices:
        ouragan_data = data.iloc[start_index:end_index]
        ouragans.append(ouragan_data)
        start_index = end_index
    # Ajouter le dernier ouragan
    ouragan_data = data.iloc[start_index:]
    ouragans.append(ouragan_data)
    return ouragans

if __name__ == '__main__':
    data = pd.read_csv("../data/Hurricane_Name.csv")
    print(getNumberOfHurricane(data))

