from sklearn import datasets
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#1
#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

breast_cancer = datasets.load_breast_cancer()

#print (data.data)
#print (data.feature_names)

#2. 569 données avec 30 données 


#print(breast_cancer.data)

#divide by 2 the number of attributs 


pca = PCA(n_components=2)
donnee_fit = pca.fit(breast_cancer.data).transform(breast_cancer.data)
donnee_fit_transform = pca.fit_transform(breast_cancer.data) #calcul et enregistrement de la projection 

print(np.shape(donnee_fit_transform))
print(np.shape(breast_cancer.data))
#print(np.allclose(breast_cancer.data,donnee_fit_transform))

# print(donnee_fit, donnee_fit_transform) #maintenant en deux dimensions
# print(pca.explained_variance_ratio_)
# print(pca.singular_values_)


#machine learing -> une base d'apprentissage 
#                -> une base de test 

#affichage des valeurs 

plt.scatter(donnee_fit_transform[:, 0], donnee_fit_transform[:, 1], c=breast_cancer.target, alpha=0.5, label="samples")
plt.legend()
plt.show()

