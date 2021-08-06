
X1 = '10'
Y1 = '20'
X2 = '11'
Y2 = '21'


class BaseExtractor:
    def reset_buffers(self):
        self.xBuf = []
        self.yBuf = []

    @staticmethod
    def get_line(doc):
        return next(doc).strip()

class PolyLineExtractor(BaseExtractor):
    def extract(self, doc):
        self.reset_buffers()
        fVertex = False
        while True:
            line = self.get_line(doc)
            if line == 'SEQEND':
                break
            if line == 'VERTEX':
                fVertex = not fVertex
            if fVertex and line == X1:
                self.xBuf.append(float(self.get_line(doc)))
            if fVertex and line == Y1:
                self.yBuf.append(float(self.get_line(doc)))
                fVertex = False
        return self.xBuf, self.yBuf
