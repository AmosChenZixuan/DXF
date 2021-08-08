from extractors import X1
import matplotlib.pyplot as plt

class Drawer:
    def __init__(self):
        self._elements = []

    def add(self, element):
        self._elements.append(element)

    def plot(self):
        for e in self._elements:
            e.plot()

    @staticmethod
    def show():
        plt.show()

    @staticmethod
    def save(path="Figure.png"):
        plt.savefig(path)

    @staticmethod
    def setCanvas(x0, x1, y0, y1, no_axis=True):
        plt.xlim((x0, x1))
        plt.ylim((y0, y1))
        if no_axis:
            plt.axis('off')
