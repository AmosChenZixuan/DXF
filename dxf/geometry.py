import matplotlib.pyplot as plt

class PolyLine:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return len(self.x)

    def plot(self):
        plt.plot(self.x, self.y, c='black')

class Block:
    def __init__(self, elements):
        self.elements = elements

    def __len__(self):
        return len(self.elements)

    def plot(self):
        for e in self.elements:
            e.plot()