import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.cm as cm
import numpy as np

# Génération d'une liste aléatoire d'entiers entre 1 et 100
liste1 = random.sample(range(1,100), 20)
liste2 = random.sample(range(1,100), 20)
liste3 = random.sample(range(1,100), 20)
liste4 = random.sample(range(1,100), 20)


print("liste 1 : " + str(liste1))
print("liste 2 : " + str(liste2))
print("liste 3 : " + str(liste3))
print("liste 4 : " + str(liste4))

# Génération du graph correspondant à "liste1"
plt.subplot(221)
plt.plot(liste1, "b-", marker="*", label="Liste 1")
plt.ylabel('nbres aleatoires')
plt.xlabel('échantillon de 20 valeurs')
plt.legend()

# Création Histogramme
plt.subplot(222)
x = [random.randint(0,150) for i in range(1000)]
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='b', alpha=0.5)

plt.xlabel('Mise')
plt.ylabel(u'Probabilité')
plt.axis([0, 150, 0, 0.02])
plt.grid(True)

# Génération d'un graph qui mutualise les resultats des différentes courbes
plt.subplot(223)
plt.plot(liste1, "b-", marker="*", label="Liste 1")
plt.plot(liste2, "r--", marker="+", label="Liste 2")
plt.plot(liste3, "g:", marker=".", label="Liste 3")
plt.plot(liste4, "c-", marker="", label="Liste 4")

# Défintion du nom des axes
plt.ylabel('nbres aleatoires')
plt.xlabel('échantillon de 20 valeurs')

# Place des points dangers et points fléchés sur le graphe
plt.text(6, 90, r'Danger')
plt.text(12, 55, r'Stable')
plt.annotate('Limite', xy=(17, 90), xytext=(19, 95),arrowprops={'facecolor':'black', 'shrink':0.05} )
# Afficher Légende
plt.legend() 

plt.subplot(224)
# Création Camenbert
name = ['-18', '18-25', '25-50', '50+']
data = random.sample(range(1,10), 4)
#data = [5000, 26000, 21400, 12000]

explode=(0, 0.15, 0, 0)
plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
plt.axis('equal')
plt.show()

# Création d'une surface

X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.cos(R)

fig = plt.figure()
ax = fig.gca(projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap="viridis",
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

# Affichage graphique
#plt.show()