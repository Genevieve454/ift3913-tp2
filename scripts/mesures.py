import pandas as pd
import matplotlib.pyplot as plt
import statistics
import csv

"""
Scripts pour obtenir les statistiques boite moustache du fichier jfreechart-stats.csv
"""

m = []
u = []
l = []
d = []
s = []
i = []

data = pd.read_csv('../data/jfreechart-stats.csv')
colonnes = list(data)
colonnes.remove('class')
nb_rangees = data.shape[0]

for k in colonnes:
    mediane = data[k].median()
    m.append(mediane)

    valeurs_min_mediane = []
    valeurs_max_mediane = []

    for j in range(nb_rangees):
        donnee = data.loc[j, k]

        if donnee < mediane:
            valeurs_min_mediane.append(donnee)
        else:
            valeurs_max_mediane.append(donnee)

    u.append(statistics.median(valeurs_max_mediane))
    l.append(statistics.median(valeurs_min_mediane))

for index in range(len(colonnes)):
    d.append(u[index]-l[index])
    s.append((u[index] + 1.5*d[index]))

    limite_inferieure = l[index] - 1.5*d[index]
    if limite_inferieure < 0:
        limite_inferieure = 0
    i.append(limite_inferieure)


with open('../data/statistiques.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Statistiques", "NCLOC", "DCP", "NOCom", "WMC"])
    writer.writerow(["Médiane", m[0], m[1], m[2], m[3]])
    writer.writerow(["Quartile supérieur", u[0], u[1], u[2], u[3]])
    writer.writerow(["Quartile inférieur", l[0], l[1], l[2], l[3]])
    writer.writerow(["Longueur", d[0], d[1], d[2], d[3]])
    writer.writerow(["Limite supérieure", s[0], s[1], s[2], s[3]])
    writer.writerow(["Limite inférieure", i[0], i[1], i[2], i[3]])

boxplot_NCLOC = data.boxplot(showfliers=False, grid=False, column=[' NCLOC'])
boxplot_NCLOC.plot()

plt.show()

boxplot_DCP = data.boxplot(showfliers=False, grid=False, column=[' DCP'])
boxplot_DCP.plot()

plt.show()

boxplot_NOCom = data.boxplot(showfliers=False, grid=False, column=[' NOCom'])
boxplot_NOCom.plot()

plt.show()

boxplot_WMC = data.boxplot(showfliers=False, grid=False, column=['WMC'])
boxplot_WMC.plot()

plt.show()
