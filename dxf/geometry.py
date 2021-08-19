import matplotlib.pyplot as plt
import numpy as np

class PolyLine:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return len(self.x)

    def plot(self):
        plt.plot(self.x, self.y, c='black')

class Block:
    def __init__(self, elements, relocate = True):
        self.elements = elements
        self.relocate = relocate

    def __len__(self):
        return len(self.elements)

    def plot(self):
        if self.relocate:
            xmin, xmax, ymin, ymax = float('inf'), -float('inf'), float('inf'), -float('inf')
            x,y = [], []
            for e in self.elements:
                x.append(np.array(e.x))
                y.append(np.array(e.y))
                xmin = min(x[-1].min(), xmin)
                xmax = max(x[-1].max(), xmax)
                ymin = min(y[-1].min(), ymin)
                ymax = max(y[-1].max(), ymax)

            for i in range(len(x)):
                m = x[i]; n = y[i]
                m -= (xmax + xmin)//2; n -= (ymax + ymin)//2
                plt.plot(m, n, c='black')
        else:
            for e in self.elements:
                e.plot()
