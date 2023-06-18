import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("./data/Hurricane_Name.csv")

bassin_ep = df[df['BASIN'] == 'EP']


################################## DIFFERENTS GRAPHIQUES #####################################################

# Compter le nombre d'ouragans par mois
nombre_ouragans_par_mois = bassin_ep['month'].value_counts().sort_index()

    # Assigner les noms des mois aux numéros de mois
noms_mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre',
             'Novembre', 'Décembre']
nombre_ouragans_par_mois.index = noms_mois

    # Ajuster la largeur et la hauteur de la figure
plt.figure(figsize=(10, 10))

    # Diagramme à barres
plt.bar(nombre_ouragans_par_mois.index, nombre_ouragans_par_mois.values)
plt.xlabel('Mois')
plt.ylabel('Nombre d\'ouragans')
plt.title('Nombre d\'ouragans par mois dans le bassin EP')
plt.xticks(rotation=45)  # Rotation des étiquettes des mois
plt.show()

########################################################################################################

# Évolution de la vitesse du vent dans le bassin EP
plt.plot(bassin_ep['year'], bassin_ep['USA_WIND'])
plt.xlabel('Année')
plt.ylabel('Vitesse du vent (USA)')
plt.title('Évolution de la vitesse du vent dans le bassin EP')
plt.show()

########################################################################################################

# Compter le nombre d'ouragans par sous-bassin
nb_sousbassins_ep = bassin_ep['SUBBASIN'].value_counts()

    # Camembert
plt.pie(nb_sousbassins_ep.values, labels=nb_sousbassins_ep.index, autopct='%1.1f%%')
plt.title('Répartition des sous-bassins dans le bassin EP')
plt.axis('equal')  # Pour avoir un cercle parfait
plt.show()