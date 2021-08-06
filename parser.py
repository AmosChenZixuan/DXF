import matplotlib.pyplot as plt
from extractors import PolyLineExtractor

pe = PolyLineExtractor()
x,y = None,None

#with open('circle-.dxf', 'r') as doc:
with open('ZH-XJ-20174240-部件-v3.dxf', 'r') as doc:

    i = 0
    while True:
        line = next(doc).strip()
        if line == 'EOF':
            break
        if line == 'POLYLINE':
            x,y = pe.extract(doc)
            plt.plot(x,y)
            i += 1


        # if i > 0:
        #     break

plt.show()