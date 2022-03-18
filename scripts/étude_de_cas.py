import pandas as pd
from statistics import geometric_mean
import csv

data = pd.read_csv('../data/jfreechart-stats.csv')
# Nettoyer le nom des colonnes
data.columns = [colonne.strip() for colonne in data.columns]
del data['class']
del data['NCLOC']
del data['WMC']

print(data.corr(method='pearson'))

collections_donnees = {}
collections_donnees['NOCom >= 10'] = data[data['NOCom'] >= 10]
collections_donnees['NOCom < 10'] = data[data['NOCom'] < 10]

nom_colonnes = []
moyennes_geometriques = []
minimums = []
maximums = []

for nom_colonne, donnees in collections_donnees.items():
    nom_colonnes.append(nom_colonne)
    moyennes_geometriques.append(round(geometric_mean(donnees['DCP']), 2))
    minimums.append(donnees['DCP'].min())
    maximums.append(donnees['DCP'].max())

with open('../data/etude_de_cas.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Statistiques"] + nom_colonnes)
    writer.writerow(["Moyennes Geometriques"] + moyennes_geometriques)
    writer.writerow(["Maximums"] + maximums)
    writer.writerow(["Minimums"] + minimums)
