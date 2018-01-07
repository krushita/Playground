# https://gist.github.com/SonechkaGodovykh/18f60a3b9b3e6812c071456f61f9c5a6

class UnionFind:

    def __init__(self, N):
        self.ids = range(N)
        self.size = [1] * (N)  #Create array of N elements initialized to 1

    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)
        if proot == qroot:
            return

        if self.size[proot] < self.size[qroot]: # p subtree is smaller
            self.ids[proot] = qroot # Make q as root of p (i.e. p as child of q)
            self.size[qroot] += self.size[proot] # Increase size of q
        else:
            self.ids[qroot] = proot # Make p as root of q
            self.size[proot] += self.size[qroot]

    def root(self, p):
        i = p
        while (i != self.ids[i]):
            #self.ids[i] = self.ids[self.ids[i]] # Path compression
            i = self.ids[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

if __name__ == "__main__":
    uf = UnionFind(10)
    for (p, q) in [(3, 4), (4, 9), (8, 0), (2, 3), (5, 6), (5, 9),
                  (7, 3), (4, 8), (6, 1)]:
        uf.union(p, q)
    print "UF : {}".format(uf.ids)

    print "Connected(0,1) = {}".format(uf.connected(0, 1))
