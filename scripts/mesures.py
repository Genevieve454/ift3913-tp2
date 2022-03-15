import pandas as pd
import matplotlib.pyplot as plt
import csv

"""
Scripts pour obtenir les statistiques boite moustache du fichier jfreechart-stats.csv
"""

# Utilisés pour le calcul de limite inférieure
MINS = [
    0,  # NCLOC
    0,  # DCP
    1,  # NOCom
    1  # WMC
]

medianes = []
quartiles_superieurs = []
quartiles_inferieurs = []
longueurs = []
limites_inferieures = []
limites_superieures = []

data = pd.read_csv('../data/jfreechart-stats.csv')
del data["class"]
# Nettoyer le nom des colonnes
data.columns = [colonne.strip() for colonne in data.columns]

for i, nom_colonne in enumerate(list(data)):
    medianes.append(data[nom_colonne].median())

    valeurs_min_mediane = data[nom_colonne]\
        .where(data[nom_colonne] < medianes[i])
    valeurs_max_mediane = data[nom_colonne]\
        .where(data[nom_colonne] >= medianes[i])

    quartiles_inferieurs.append(valeurs_min_mediane.median())
    quartiles_superieurs.append(valeurs_max_mediane.median())

    longueurs.append(quartiles_superieurs[i] - quartiles_inferieurs[i])

    limites_inferieures.append(max(
        MINS[i],
        quartiles_inferieurs[i] - 1.5 * longueurs[i]
    ))
    limites_superieures.append(quartiles_superieurs[i] + 1.5 * longueurs[i])

with open('../data/statistiques.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Statistiques"] + list(data))
    writer.writerow(["Médiane"] + medianes)
    writer.writerow(["Quartile supérieur"] + quartiles_superieurs)
    writer.writerow(["Quartile inférieur"] + quartiles_inferieurs)
    writer.writerow(["Longueur"] + longueurs)
    writer.writerow(["Limite supérieure"] + limites_superieures)
    writer.writerow(["Limite inférieure"] + limites_inferieures)

for nom_colonne in list(data):
    data.boxplot(showfliers=False, grid=False, column=[nom_colonne]).plot()
    plt.title(
        f"Diagramme de boîte pour la mesure {nom_colonne},\n pour le projet jfreechart")
    plt.show()
