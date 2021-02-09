class Board:
    def __init__(self):
        self._info = [[" " for j in range(10)] for i in range(10)]

        self._map = {0:(1,1),1:(1,4),2:(1,7),3:(4,1),4:(4,4),5:(4,7),6:(7,1),7:(7,4),8:(7,7)}

        self.loadBoard()

    def paint(self):
        for i in self._info:
            out = ""
            for j in i:
                out += j
            print(out)

    def set(self,k,l):
        i = self._map[k][0]
        j = self._map[k][1]
        position = [(i,j),(i,j+1),(i+1,j),(i+1,j+1)]

        for h in position:
            self._info[h[0]][h[1]] = l
        
    def loadBoard(self):
        line = ["=" for i in range(10)]
        data = [0,3,6,9]

        for i in data:
            self._info[i] = line
        
        for i in self._info:
            for j in data:
                i[j] = "'"

        
        
