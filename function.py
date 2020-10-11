class function:
    def information(self,f):
        return f.split()

    def evaluate(self,x):
        return (self.m * x) + self.b

    def __init__(self,f):
        self.f = self.information(f)
        if "-" in self.f[2]:
            self.m = float("-" + self.f[2][1])
        else:
            self.m = float(self.f[2][0])
        if "-" in self.f[3]:
            self.b = float("-" + self.f[4])
        else:
            self.b = float(self.f[4])
