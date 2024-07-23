from math import sqrt
from collections import Counter
import matplotlib.pyplot as plt

class KNN:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.abres = []
        self.ares = []
        self.bres = []
        self.clases = []

    def matxy(self):
        for xe in self.a:
            p = (self.c[0] - xe[0])**2
            r = (self.c[1] - xe[1])**2
            o = sqrt(p + r)
            self.ares.append([o,"A"])
        for re in self.b:
            p = (self.c[0] - re[0])**2
            r = (self.c[1] - re[1])**2
            o = sqrt(p + r)
            self.bres.append([o,"B"])
            self.abres = self.bres + self.ares
            self.abres.sort()
    def KNNR(self, k):
        self.k = k
        a2 = 0
        b2 = 0
        for i in range(0,self.k):
            self.clases.append(self.abres[i][1])
        contador = Counter(self.clases)
        r = contador.most_common(1)[0]
        #print(self.abres[i][0])
        #print(f"El dato pertenece al grupo "+r[0])
        plt.annotate(f'Predicción: {r[0]}', (self.c[0], self.c[1]), textcoords="offset points", xytext=(0,-15), ha='center', color='green')
