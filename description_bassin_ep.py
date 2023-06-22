import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("./data/Hurricane_Name.csv")
#
# bassin_ep = df[df['BASIN'] == 'EP']
# nb_tempêtes_par_bassin = df['BASIN'].value_counts()
#
# print('\n')
#
# print(">> GÉNÉRALITÉ")
# # Nombre de tempêtes par bassin
# nombre_tempetes_par_bassin = df['BASIN'].value_counts()
# print("Nombre de tempêtes par bassin :")
# for bassin, i in nombre_tempetes_par_bassin.items():
#     print(f"{bassin}: {i}")
#
# print('\n')
#
# print(">> FOCUS SUR LE BASSIN EP")
# # Liste des sous-bassins dans EP
# sous_bassins = bassin_ep['SUBBASIN'].unique().tolist()
# print("Liste des sous-bassins :")
# for i in sous_bassins:
#     print(i)
#
# print('\n')
#
# # Nombre d'ouragans par année
# ouragans_par_annee = bassin_ep['year'].value_counts()
#
#     # Année avec le plus d'ouragans
# annee_plus_ouragans = ouragans_par_annee.idxmax()
#
#     # Année avec le moins d'ouragans
# annee_moins_ouragans = ouragans_par_annee.idxmin()
#
# print("L'année avec le plus d'ouragans dans le bassin EP :", annee_plus_ouragans)
# print("L'année avec le moins d'ouragans dans le bassin EP :", annee_moins_ouragans)
#
# print('\n')

df = pd.read_csv("data/Historical_Hurricane_Tracks.csv",low_memory=False)

bassin = df['BASIN'].unique()
print("Liste des bassins :", bassin)

subbassin = df['SUBBASIN'].unique()
print("Liste des sous-bassins :", subbassin)

years_ouragan = df['year'].unique()
ouragans_par_annee = {}
bassin_ouragan = {}
subbassin_ouragan = {}

for year in years_ouragan:
    ouragans = df[df['year'] == year]
    names = ouragans['NAME'].unique()
    ouragans_par_annee[year] = 0
    for name in names:
        ouragans_par_annee[year] += 1
        df_ouragan = ouragans[(ouragans['NAME'] == name) & (ouragans['year'] == year)]
        bassin_value = df_ouragan['BASIN'].values[0]
        subbassin_value = df_ouragan['SUBBASIN'].values[0]
        if pd.notna(subbassin_value):
            subbassin_ouragan[subbassin_value] = subbassin_ouragan.get(subbassin_value, 0) + 1
        else:
            subbassin_ouragan['NA'] = subbassin_ouragan.get('NA', 0) + 1
        if pd.notna(bassin_value):
            bassin_ouragan[bassin_value] = bassin_ouragan.get(bassin_value, 0) + 1
        else:
            bassin_ouragan['NA'] = bassin_ouragan.get('NA', 0) + 1

total_sum = sum(ouragans_par_annee.values())
print("Nombre total d'ouragans :", total_sum)

# Année avec le plus d'ouragans
annee_plus_ouragans = max(ouragans_par_annee, key=ouragans_par_annee.get)
print("L'année avec le plus d'ouragans :", annee_plus_ouragans, "avec", ouragans_par_annee[annee_plus_ouragans], "ouragans")

# Année avec le moins d'ouragans
annee_moins_ouragans = min(ouragans_par_annee, key=ouragans_par_annee.get)
print("L'année avec le moins d'ouragans :", annee_moins_ouragans, "avec", ouragans_par_annee[annee_moins_ouragans], "ouragans")

# Nombre d'ouragans par bassin
print("Nombre d'ouragans par bassin :", bassin_ouragan)

# Nombre d'ouragans par sous-bassin
print("Nombre d'ouragans par sous-bassin :", subbassin_ouragan)
