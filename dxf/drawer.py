import matplotlib.pyplot as plt

class Drawer:
    def __init__(self):
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def plot(self):
        for e in self.elements:
            e.plot()

    @staticmethod
    def show():
        plt.show()

    @staticmethod
    def save(path="Figure.png"):
        plt.savefig(path, bbox_inches='tight', pad_inches=0)

    @staticmethod
    def setCanvas(x0, x1, y0, y1, no_axis=True):
        plt.xlim((x0, x1))
        plt.ylim((y0, y1))
        if no_axis:
            plt.xticks([])
            plt.yticks([]) 
            plt.axis('off')
