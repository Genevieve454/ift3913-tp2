import pandas as pd
import csv


data = pd.read_csv('../data/jfreechart-stats.csv')
del data['class']
del data[' NCLOC']
del data['WMC']

print(data.corr(method='pearson'))

dix_modifications_et_plus = data[data[' NOCom'] >= 10]
moins_de_dix_modifications = data[data[' NOCom'] < 10]

nouvelles_donnees = {'DCP_dix_modifications_et_plus': dix_modifications_et_plus[' DCP'],
                     'DCP_moins_de_dix_modifications': moins_de_dix_modifications[' DCP']}

data = pd.DataFrame(nouvelles_donnees)
medianes = []
minimums = []
maximums = []

for i in list(data):
    medianes.append(data[i].median())
    minimums.append(data[i].min())
    maximums.append(data[i].max())


with open('../data/etude_de_cas.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Statistiques"] + list(data))
    writer.writerow(["Médiane"] + medianes)
    writer.writerow(["Maximums"] + maximums)
    writer.writerow(["Minimums"] + minimums)
