import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3):
        self.k = k
    def aprendizaje(self, X, C):
        self.X=X #Matriz de vectores
        self.c=C #Clases de los vectores
        self.nmuestras = X.shape[1]#Cantidad de muestras
        print(X.shape[1])
    def clasification(self, Y):
        clases=[]
        for i in range(Y.shape[1]):
            distancias=np.empty(self.nmuestras)
            for n in range(self.nmuestras):
                distancias[n]=Euclidiana(self.X[:,n],Y[:,i])
            kdistancias = np.argsort(distancias)
            ketiqueta=self.c[kdistancias[:self.k]]
            c = Counter(ketiqueta).most_common(1)
            clases.append(c[0][0])
        return clases
def Euclidiana(x,y):
    return np.sqrt(np.sum((x-y)**2))