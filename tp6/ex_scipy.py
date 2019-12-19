import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate
from scipy import stats
from scipy import optimize
from scipy import interpolate
from scipy import misc



#EXEMPLE 1 :  CREATION DE GRAPH ET APPROXIMATION
def eggholder(x):
    return (-(x[1] + 47) * np.sin(np.sqrt(abs(x[0]/2 + (x[1]  + 47))))
            -x[0] * np.sin(np.sqrt(abs(x[0] - (x[1]  + 47)))))

def graphExample1():
    bounds = [(-512, 512), (-512, 512)]

    x = np.arange(-512, 513)
    y = np.arange(-512, 513)
    xgrid, ygrid = np.meshgrid(x, y)
    xy = np.stack([xgrid, ygrid])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(45, -45)
    ax.plot_surface(xgrid, ygrid, eggholder(xy), cmap='terrain')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('eggholder(x, y)')
    plt.show()

    #Optimisation de La courbe
    results = dict()
    results['shgo'] = optimize.shgo(eggholder, bounds)
    results['shgo']



#EXEMPLE 2 :  CREATION DE GRAPH ET APPROXIMATION
def func(x, a, b, c):
    return a * np.exp(-b * x) + c


def optimizeExample():
    # Define the data to be fit with some noise:
    xdata = np.linspace(0, 4, 50)
    y = func(xdata, 2.5, 1.3, 0.5)
    np.random.seed(1729)
    y_noise = 0.2 * np.random.normal(size=xdata.size)
    ydata = y + y_noise
    plt.plot(xdata, ydata, 'b-', label='data')

    # Fit for the parameters a, b, c of the function func:
    popt, pcov = optimize.curve_fit(func, xdata, ydata)
    popt
    plt.plot(xdata, func(xdata, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

    # Constrain the optimization to the region of 0 <= a <= 3, 0 <= b <= 1 and 0 <= c <= 0.5:
    popt, pcov = optimize.curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
    popt
    plt.plot(xdata, func(xdata, *popt), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


#EXEMPLE 3 :  CREATION DE GRAPH ET APPROXIMATION
def interpolateExample():
    x = np.arange(0, 10)
    y = np.exp(-x/3.0)
    f = interpolate.interp1d(x, y)

    xnew = np.arange(0, 9, 0.1)
    ynew = f(xnew)   # use interpolation function returned by `interp1d`
    plt.plot(x, y, 'o', xnew, ynew, '-')
    plt.show()


# Traitement d'image avec la bibliotheque scipy. misc : http://www.tangentex.com/TraitementImages.htm (Impossible d'executer ce code car 'imread' n'est plus pris en charge dans les nouvelle version de Scipy)
def traitementImage():
    #ouverture du fichier image
    ImageFile = 'website.jpg'
    try:
        print ("Lecture de l'image effectuée")
        #img = misc.imread(ImageFile)

    except IOError:
        print ('Erreur sur ouverture du fichier ' + ImageFile)
        #sys.exit(1)

    #affichage des caractéristiques de l'image
    #print(img.shape)

    # affichage de l'image
    
    #plt.imshow(img)
    plt.axis('off')
    plt.show()

    # On pourrait ensuite utiliser la libraire scipy.misc.imresize pour redimensionner l'image


# Execution Fonctions
graphExample1()
optimizeExample()
interpolateExample()



