import pandas as pd

# Charger les données depuis le fichier CSV
data = pd.read_csv("../data/hurricanes_Past_In_Caribbean.csv", low_memory=False)

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

# Afficher les données de chaque ouragan
for i, ouragan_data in enumerate(ouragans):
    print(f"\n Ouragans {ouragan_data['NAME'].values[0]} "
          f"de {ouragan_data['Hurricane_Date'].min()} "
          f"a {ouragan_data['Hurricane_Date'].max()} ")

# # Sauvegarder les données de chaque ouragan dans des fichiers CSV
# for i, ouragan_data in enumerate(ouragans):
#     ouragan_data.to_csv(f"hurricane_{i+1}.csv", index=False)
