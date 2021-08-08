import matplotlib.pyplot as plt
from extractors import PolyLineExtractor
from drawer import Drawer
from geometry import PolyLine

pe = PolyLineExtractor()
drawer = Drawer()
drawer.setCanvas(-1500, 2500, -1000, 2000, no_axis=True)

#file_name = 'circle-'
file_name = 'ZH-XJ-20174240-部件-v3'

with open(f'{file_name}.dxf', 'r') as doc:

    i = 0
    while True:
        line = next(doc).strip()
        if line == 'EOF':
            break
        if line == 'POLYLINE':
            x, y     = pe.extract(doc)
            polyline =  PolyLine(x,y)
            drawer.add(polyline)
            i += 1
        if i > 6:
            break


drawer.plot()
#drawer.show()
drawer.save(f"{file_name}.png")