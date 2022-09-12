from sklearn import datasets
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#2.1 Classification - SVM

# 1 NORMALIZATION

#normalisation et standardisation 
#fit que sur la base d'apprentissage
#normalisation => traitement

breast_cancer = datasets.load_breast_cancer()

scaler = StandardScaler()
breast_cancer_normalised = scaler.fit(breast_cancer.data).transform(breast_cancer.data)

#fit calcul 
#application du calcul

# print(np.shape(breast_cancer.data))

# print(breast_cancer.data)
# print(breast_cancer_normalised)

#print(np.shape(breast_cancer_normalised))

#plt.scatter(breast_cancer.data[:, 0], breast_cancer.data[:, 1], c=breast_cancer.target, alpha=0.5)
#plt.scatter(breast_cancer_normalised[:, 0], breast_cancer_normalised[:, 1], c="red", alpha=0.5)

# plt.plot(breast_cancer_normalised[:, 0]) #normalisé autour de 0
# plt.plot(breast_cancer.data[:, 0]) #base non normalisé
# plt.legend()
# plt.show()

#2 DIVIDE DATASET

learning, tempo = train_test_split(breast_cancer_normalised, test_size=0.6)
validation, test = train_test_split(tempo, test_size=0.5)

print(np.shape(breast_cancer_normalised),np.shape(learning),np.shape(validation),np.shape(test))

plt.plot(learning[:, 0]) 
plt.plot(validation[:, 0])
plt.plot(test[:, 0])
plt.legend()
plt.show()