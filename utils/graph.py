import pandas as pd
import matplotlib.pyplot as plt



def getGraphPressionVersusSpeed(data: pd.DataFrame):

    # Extraire les colonnes de pression et de vitesse du DataFrame
    pression = data['USA_PRES']
    vitesse = data['USA_WIND']

    # Tracer le graphique
    plt.plot(vitesse, pression, 'o')
    plt.xlabel('Vitesse')
    plt.ylabel('Pression')
    plt.title('Pression en fonction de la vitesse')
    plt.grid(True)

    # Afficher le graphique
    plt.show()


def getHistPressionVersusSpeed(data: pd.DataFrame):

    # Extraire les colonnes de pression et de vitesse du DataFrame
    pression = data['USA_PRES']
    vitesse = data['USA_WIND']

    # Tracer l'histogramme
    plt.hist2d(vitesse, pression, bins=(20, 20),
               cmap='Blues')  # Vous pouvez ajuster le nombre de bins selon vos préférences
    plt.colorbar()
    plt.xlabel('Vitesse')
    plt.ylabel('Pression')
    plt.title('Histogramme de pression en fonction de la vitesse')

    # Afficher l'histogramme
    plt.show()

def getBarPlotPressionVersusSpeed(data: pd.DataFrame):

    # Extraire les colonnes de pression et de vitesse du DataFrame
    pression = data['USA_PRES']
    vitesse = data['USA_WIND']

    # Tracer le diagramme en barres
    plt.bar(vitesse, pression)
    plt.xlabel('Vitesse')
    plt.ylabel('Pression')
    plt.title('Diagramme en barres de pression en fonction de la vitesse')

    # Afficher le diagramme en barres
    plt.show()

def getPressByYear(list_data):

    moyennes_pres = []
    annees = []

    # Boucle sur la liste des DataFrames
    for df in list_data:
        moyenne_pres = df['USA_PRES'].mean()
        annee = df['year'].iloc[0]  # Supposant que 'Annee' est une colonne dans vos DataFrames
        moyennes_pres.append(moyenne_pres)
        annees.append(annee)

    # Tracer le graphique de USA_WIND par année
    plt.bar(annees, moyennes_pres)
    plt.xlabel('Année')
    plt.ylabel('USA_PRES (moyenne)')
    plt.title('Diagramme en barres de USA_PRES par année')
    plt.grid(True)
    plt.show()

def getWindByYear(list_data):
    moyennes_wind = []
    annees = []

    # Boucle sur la liste des DataFrames
    for df in list_data:
        moyenne_wind = df['USA_WIND'].mean()
        annee = df['year'].iloc[0]  # Supposant que 'Annee' est une colonne dans vos DataFrames
        if annee in annees:
            moyennes_wind[annees.index(annee)] = (moyennes_wind[annees.index(annee)] + moyenne_wind) / 2
        if annee not in annees:
            moyennes_wind.append(moyenne_wind)
            annees.append(annee)

    # Tracer le graphique de USA_WIND par année
    plt.bar(annees, moyennes_wind)
    plt.xlabel('Année')
    plt.ylabel('USA_WIND (moyenne)')
    plt.title('Diagramme en barres de USA_WIND par année')
    plt.grid(True)
    plt.show()