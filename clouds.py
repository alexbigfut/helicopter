from utils import randbool

class Clouds:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        
    def update(self, r = 1, mxr = 20, g = 1, mxg = 10):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1
                    if randbool(g, mxg):
                        self.cells[ri][ci] = 2
                else:
                    self.cells[ri][ci] = 0
                    
    def export_date(self):
        return {'cells': self.cells}
    
    def import_data(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.w)] for j in range(self.h)]
                    
                    
                    
                    