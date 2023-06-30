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
