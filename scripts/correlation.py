import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix

# https://stackoverflow.com/a/30215541

data = pd.read_csv('../data/jfreechart-stats.csv')
del data["class"]

axes = scatter_matrix(data, diagonal='kde')
corr = data.corr().to_numpy()
for i, j in zip(*plt.np.tril_indices_from(axes, k=1)):
    if j < i:
        axes[i, j].annotate(
            "%.3f" % corr[i, j], (0.8, 0.8), xycoords='axes fraction', ha='center', va='center')

plt.suptitle(
    "Matrice de corrélation entre différentes mesures,\n pour le projet jfreechart")
plt.show()

# Regression linéaire
data.columns = [colonne.strip() for colonne in data.columns]
# colonnes_a_tester = {['NCLOC', 'WMC'], ['DCP', 'WMC'], ['NOCom', 'WMC']}

for nom_colonne in list(data):
    if nom_colonne == 'WMC':
        continue
    x = data[nom_colonne]
    y = data['WMC']
    plt.plot(x, y, 'o')
    slope, intercept = np.polyfit(x, y, 1)
    plt.plot(x, slope * x + intercept)
    titre = "Régression linéaire des données : WMC et " + nom_colonne
    plt.suptitle(titre)
    plt.xlabel(nom_colonne)
    print(
        f"Y (WMC) = X ({nom_colonne}) * {round(slope, 2)} + {round(intercept, 2)}")
    plt.ylabel('WMC')
    plt.show()
