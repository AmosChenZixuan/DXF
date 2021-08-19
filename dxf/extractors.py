from dxf.geometry import PolyLine, Block
from dxf.drawer import Drawer

X1 = '10'
Y1 = '20'
X2 = '11'
Y2 = '21'

'''
==== Dxf ====

Block               - Geometry Pieces
    PolyLine        - Curved line represented as vertices
        Vertex      - Points
    SEQEND          - End of list of vertices
ENDBLK              - End of one piece/block
...
EOF                 - End of File

=============
'''


def extract_dxf(doc, drawer:Drawer):
    while True:
        line = extract_line(doc)
        if line == 'EOF':
            break
        if line == 'BLOCK':
            blk = extract_block(doc, relocate=False)
            drawer.add(blk)
    return drawer

def extract_line(doc):
    return next(doc).strip()
    
def extract_polyline(doc):
    xBuf, yBuf = [], []
    fVertex = False
    while True:
        line = extract_line(doc)
        if line == 'SEQEND':
            break
        if line == 'VERTEX':
            fVertex = not fVertex
        if fVertex and line == X1:
            xBuf.append(float(extract_line(doc)))
        if fVertex and line == Y1:
            yBuf.append(float(extract_line(doc)))
            fVertex = False
    return PolyLine(xBuf, yBuf)

def extract_block(doc, relocate=True):
    pBuf = []
    while True:
        line = extract_line(doc)
        if line == 'ENDBLK':
            break
        if line == 'POLYLINE':
           pBuf.append(extract_polyline(doc))
    return Block(pBuf, relocate)