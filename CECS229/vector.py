class Vec:
    def __init__(self, D, f):
        self.D = D
        self.f = f
    def zero_vec(self, D):
        return Vec(D, {})

    def setitem(self, d, val):
        self.f[d] = val
    def getitem(self, d):
        return self.f[d] if (d in self.f[d]) else 0
    def scalar_mul(self, alpha):
        return Vec(self.D, {d :alpha*value for d, value in self.f.items()})
    def add(self, u, v):
        return Vec(self.D, {d : u.getitem(d) + v.getitme(d) for d in u.D})

def __main__():
    v =  ({0, 1, 2}, {0:0.2, 1:0.3, 2: 0.9})
    for key, val in v.f.iteritems():
        print(key, val)
if __name__ == "__main__":
    main()
#0 -> 0.2
#1 -> 0.3
#2 -> 0.9