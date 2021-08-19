from dxf.extractors import extract_dxf
from dxf.drawer import Drawer

drawer = Drawer()
drawer.setCanvas(-1500, 2500, -1000, 2000, no_axis=True)

#file_name = 'circle-'
file_name = 'ZH-XJ-20174240-部件-v3'

with open(f'{file_name}.dxf', 'r', encoding='gb18030') as doc:
    drawer = extract_dxf(doc, drawer)


drawer.plot()
drawer.show()
#drawer.save(f"{file_name}.png")