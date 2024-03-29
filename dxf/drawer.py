import matplotlib.pyplot as plt

class Drawer:
    def __init__(self):
        plt.clf()
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
        figure = plt.gcf()
        figure.set_size_inches(5.12, 5.12)
        plt.savefig(path, dpi=100)

    @staticmethod
    def setCanvas(x0, x1, y0, y1, no_axis=True):
        plt.xlim((x0, x1))
        plt.ylim((y0, y1))
        if no_axis:
            plt.xticks([])
            plt.yticks([]) 
            plt.axis('off')
