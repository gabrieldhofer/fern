import matplotlib.pyplot as plt
from random import randint
import random
          


class Barnsley:
    def __transform(self,x,y):
        r = randint(1, 100)
        if r == 1:
            return (0), (0.16*y)
        if r>= 16 and r<= 100:
            return (0.85*x + 0.04*y), (-0.04*x + 0.85*y + 1.6)
        if r>= 9 and r<= 15:
            return (0.2*x - 0.26*y), (0.23*x + 0.22*y + 1.6)
        if r>= 2 and r<= 8:
            return (-0.15*x + 0.28*y), (0.26*x + 0.24*y + 0.44)

    def __show(self):
        plt.scatter(self.__x, self.__y, s = 0.2, edgecolor ='green')
        plt.axis('off')
        plt.savefig('fern.png')
        plt.show()

    def __call__(self, iterations):
        self.__x = [0]
        self.__y = [0]
        for i in range(iterations):
            x2, y2 = self.__transform(self.__x[-1], self.__y[-1])
            self.__x.append(x2)
            self.__y.append(y2)
        self.__show()

fern = Barnsley()
fern(50000)


