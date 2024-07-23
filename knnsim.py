from math import sqrt
from collections import Counter
import matplotlib.pyplot as plt
from GENERICKNN import KNN
# %%
coordenadasA = [[2, 4], [3, 3], [4, 4], [3, 5], [5, 4], [4, 3], [3, 6], [4, 5], [5, 3], [3, 4]]
coordenadasB = [[-1, -4], [-4, -1], [-3, -4], [-4, -5], [-5, -4], [-3, -1], [-4, -6], [-5, -5], [-6, -1], [-4, -3]]
clasesstr = ["A", "B"]
e = []
obj = [2,5]
objs = [[-6, -1], [0, 0], [-5, -5], [-1, -4], [0, -1], [4, 3], [5, -5], [-3, -6], [-1, -3], [-5, -1]]

for obj1 in objs:
    x = KNN(coordenadasA,coordenadasB,obj1)
    x.matxy()
    x.KNNR(7)

# %% 
all_coords = coordenadasA + coordenadasB
xA, yA = zip(*coordenadasA)
xB, yB = zip(*coordenadasB)
xC, yC = zip(*objs)
plt.scatter(xA, yA, c='red', label='Clase A')
plt.scatter(xB, yB, c='blue', label='Clase B')
plt.scatter(xC, yC, c='yellow', label='Sin clase')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Coordenadas y Clasificaciones')
plt.legend()
plt.grid(True)
plt.show()
