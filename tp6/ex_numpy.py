import numpy as np


# Création d'un tableau de dimension (3,5) composé des 15 premiers nombres
A = np.arange(15).reshape(3, 5)
print ("Création d'une matrice A de dimension : "+ str(A.shape))
print (str(A) + '\n')


# Création d'un tableau de dimension (3,4,2) composé de nombre aléatoire
B = np.random.rand(3,4,2)
print ("Création d'une matrice B de dimension : "+ str(B.shape))
print (str(B))
print ('\n'+'ndim :'+str(B.ndim))
print ('shape :'+str(B.shape))
print ('size :'+str(B.size))
print ('dtype :'+str(B.dtype))
print ('itemsize :'+str(B.itemsize))
print ('data :'+str(B.data)+ '\n')


# Création de deux matrices de dimensions 3x3 de 0 à 8 puis de 2 à 8
C1 = np.arange(9).reshape(3, 3)
print ("Création d'une matrice C1 de dimension : "+ str(C1.shape))
print (str(C1) + '\n')

C2 = np.arange(2,11).reshape(3, 3)
print ("Création d'une matrice C1 de dimension : "+ str(C2.shape))
print (str(C2) + '\n')


# Calcul de produit de matrices C1 et C2 en utilisant '*' ou 'dot'
C1_C2 = C1 * C2
print ("Produit * de C1 par C2 :\n"+ str(C1_C2)+'\nCorrespond à la multiplication terme à terme.\n')

C1_dot_C2 = np.dot(C1,C2)
print ("Produit dot de C1 par C2 :\n"+ str(C1_dot_C2)+'\nCorrespond au produit matricielle classique.\n')


# Calcul de transposé de la matrice C1_dot_C2
transpose_C1_dot_C2 = C1_dot_C2.transpose()
print ("Transposé de la matrice dot de C1 * C2 :\n"+ str(transpose_C1_dot_C2)+'\n')


# Calcul de déterminant de la matrice C1_C2
print ("Déterminant de la matrice dot de C1 * C2 : " +str(np.linalg.det(C1_C2))+ '\n')

# Calcul de l'inverse de la matrice C1_C2
print ("Inverse de la matrice dot de C1 * C2 : \n" +str(np.linalg.inv(C1_C2))+ '\n')


# Calcul de solution de système d'équation de la matrice C1_dot_C2
solution= np.array([1,2,3])
systeme = np.linalg.solve(C1_C2,solution)
print("Les solutions du système C1 * C2 (pour les valeurs de 'solution') : \n " + str(systeme) + '\n')

# Calcul de valeurs et vecteurs propres de la matrice C1_dot_C2
print("Les valeurs propres et vecteurs propres de la matrice C1 * C2 correspond à \n(1er tableau = valeurs propres et2ème tableau = vecteurs propres) : \n " + str(np.linalg.eig(C1_C2)))