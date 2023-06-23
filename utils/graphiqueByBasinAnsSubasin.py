import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
from utils.separationOuragan import getSeparedHurricane
import numpy as np

def getAllGraphique(data : pd.DataFrame):

    all_ouragans = getSeparedHurricane(data)
    # Liste des bassins et sous-bassins
    bassins = data['BASIN'].unique().tolist()
    sous_bassins = data['SUBBASIN'].unique().tolist()

    # Compteurs pour le nombre d'ouragans par bassin et sous-bassin
    compteur_bassins = Counter()
    compteur_sous_bassins = {bassin: Counter() for bassin in bassins}
    # Parcourir les dataframes
    for dataframe in all_ouragans:
        # Compter les ouragans par bassin
        compteur_bassins.update(dataframe['BASIN'].dropna().tolist())

        # Compter les ouragans par sous-bassin de chaque bassin
        for bassin in bassins:
            sous_bassin_counts = dataframe[dataframe['BASIN'] == bassin]['SUBBASIN'].dropna().tolist()
            compteur_sous_bassins[bassin].update(sous_bassin_counts)

    # Créer le graphique à barres
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    fig.subplots_adjust(hspace=0.5)

    # Graphique pour le nombre d'ouragans par bassin
    ax1.bar(compteur_bassins.keys(), compteur_bassins.values())
    ax1.set_xlabel('Bassins')
    ax1.set_ylabel("Nombre d'ouragans")
    ax1.set_title("Nombre d'ouragans par bassin")

    # Graphique pour le nombre d'ouragans dans chaque sous-bassin par bassin
    x = range(len(sous_bassins))
    width = 0.1
    colors = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black', 'white', 'orange', 'purple', 'brown', 'pink']

    for i, bassin in enumerate(bassins):
        counts = [compteur_sous_bassins[bassin][sous_bassin] for sous_bassin in sous_bassins]
        ax2.bar([val + (i * width) for val in x], counts, width=width, color=colors[i], label=bassin)

    ax2.set_xlabel('Sous-bassins')
    ax2.set_ylabel("Nombre d'ouragans")
    ax2.set_title("Nombre d'ouragans par sous-bassin et par bassin")
    ax2.set_xticks([val + ((len(bassins) - 1) * width) / 2 for val in x])
    ax2.set_xticklabels(sous_bassins)
    ax2.legend(bassins)

    plt.show()


def getNumberHurricaneByYear(data: pd.DataFrame):
    all_hurricanes = getSeparedHurricane(data)
    years = data['year'].unique().tolist()
    min_year = min(years)
    max_year = max(years)

    # Compteur pour le nombre d'ouragans par année
    counter_total = Counter()
    counter_CP = Counter()

    # Parcourir les dataframes
    for dataframe in all_hurricanes:
        list_year = dataframe['year'].unique().tolist()
        list_basin = dataframe['BASIN'].unique().tolist()
        hurricanes_CP = dataframe[dataframe['SUBBASIN'] == 'CP']
        list_subbasin = hurricanes_CP['year'].unique().tolist()
        counter_total.update(list_year)
        counter_CP.update(list_subbasin)
        #
        # # Filtrer les ouragans du sous-bassin "CP" et compter par année
        # hurricanes_CP = dataframe[dataframe['SUBBASIN'] == 'CP']
        # counter_CP.update(hurricanes_CP['year'].dropna().tolist())

    print(f"""
    Ouragans dans le monde entre {min_year} et {max_year} :
    pour un total de {sum(counter_total.values())} ouragans.
    
    -Année avec le plus d'ouragans : {counter_total.most_common(1)[0][0]}
     Nombre d'ouragans : {counter_total.most_common(1)[0][1]}
    
    -Année avec le moins d'ouragans : {counter_total.most_common()[-1][0]}
     Nombre d'ouragans : {counter_total.most_common()[-1][1]}
    
    -Avec en moyenne {round(sum(counter_total.values()) / len(counter_total), 2)} ouragans par année.
    
    Ouragans dans le sous-bassin "CP" entre {min_year} et {max_year} :
    pour un total de {sum(counter_CP.values())} ouragans.
    
    -Année avec le plus d'ouragans : {counter_CP.most_common(1)[0][0]}
     Nombre d'ouragans : {counter_CP.most_common(1)[0][1]}
    
    -Année avec le moins d'ouragans : {counter_CP.most_common()[-1][0]}
     Nombre d'ouragans : {counter_CP.most_common()[-1][1]}
    
    -Avec en moyenne {round(sum(counter_CP.values()) / len(counter_CP), 2)} ouragans par année.
    
    
    """)

    # Trier les années dans l'ordre croissant
    years = sorted(set(years))

    if max_year - min_year > 50:
        # Créer des séquences d'années avec un intervalle de 50 ans
        sequences = list(range(min_year, max_year + 1, 50))
        if sequences[-1] != max_year:
            sequences.append(max_year)
    else:
        # Si la différence est inférieure ou égale à 50, utiliser seulement les années min et max
        sequences = [min_year, max_year]

    for i in range(len(sequences) - 1):
        sequence_start = sequences[i]
        sequence_end = sequences[i + 1]

        # Filtrer les années pour le graphique courant
        filtered_years = [year for year in years if sequence_start <= year <= sequence_end]

        # Préparer les données pour l'histogramme
        counts_total = [counter_total[year] for year in filtered_years]
        counts_CP = [counter_CP[year] for year in filtered_years]

        # Créer le graphique en histogramme
        fig, ax = plt.subplots(figsize=(12, 6))

        width = 0.35  # Largeur des barres
        x = np.arange(len(filtered_years))  # Positions des barres sur l'axe x

        ax.bar(x - width/2, counts_total, width, label='Total')
        ax.bar(x + width/2, counts_CP, width, label='CP')

        # Configurer l'axe des x
        ax.set_xticks(x)
        ax.set_xticklabels(filtered_years, rotation=45)
        ax.set_xlabel('Année')

        # Configurer l'axe des y
        ax.set_ylabel("Nombre d'ouragans")

        # Titre et légende du graphique
        ax.set_title(f"Nombre d'ouragans par année de {sequence_start} a {sequence_end} (Total et sous-bassin CP)")
        ax.legend()

        plt.tight_layout()
        plt.show()



if __name__ == '__main__':
    data = pd.read_csv("../data/Historical_Hurricane_Tracks.csv", low_memory=False)
    getNumberHurricaneByYear(data)
