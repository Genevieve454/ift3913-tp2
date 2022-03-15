import matplotlib.pyplot as plt
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

plt.suptitle("Matrice de corrélation entre différentes mesures,\n pour le projet jfreechart")
plt.show()
