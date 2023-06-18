import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Hurricane_Name.csv")

bassin_ep = df[df['BASIN'] == 'EP']
nb_tempêtes_par_bassin = df['BASIN'].value_counts()

print('\n')

print(">> GÉNÉRALITÉ")
# Nombre de tempêtes par bassin
nombre_tempetes_par_bassin = df['BASIN'].value_counts()
print("Nombre de tempêtes par bassin :")
for bassin, i in nombre_tempetes_par_bassin.items():
    print(f"{bassin}: {i}")

print('\n')

print(">> FOCUS SUR LE BASSIN EP")
# Liste des sous-bassins dans EP
sous_bassins = bassin_ep['SUBBASIN'].unique().tolist()
print("Liste des sous-bassins :")
for i in sous_bassins:
    print(i)

print('\n')

# Nombre d'ouragans par année
ouragans_par_annee = bassin_ep['year'].value_counts()

    # Année avec le plus d'ouragans
annee_plus_ouragans = ouragans_par_annee.idxmax()

    # Année avec le moins d'ouragans
annee_moins_ouragans = ouragans_par_annee.idxmin()

print("L'année avec le plus d'ouragans dans le bassin EP :", annee_plus_ouragans)
print("L'année avec le moins d'ouragans dans le bassin EP :", annee_moins_ouragans)

print('\n')