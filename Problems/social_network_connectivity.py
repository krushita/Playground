# https://gist.github.com/SonechkaGodovykh/18f60a3b9b3e6812c071456f61f9c5a6

class UnionFind:

    def __init__(self, N):
        self.N = N
        self.ids = range(N)
        self.size = [1] * (N)  #Create array of N elements initialized to 1

    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)
        if proot == qroot:
            return

        root_size = 0
        if self.size[proot] < self.size[qroot]: # p subtree is smaller
            self.ids[proot] = qroot # Make q as root of p (i.e. p as child of q)
            self.size[qroot] += self.size[proot] # Increase size of q
            root_size = self.size[qroot]
        else:
            self.ids[qroot] = proot # Make p as root of q
            self.size[proot] += self.size[qroot]
            root_size = self.size[proot]

        return root_size == self.N #If tree under root is of size N, then all nodes are connected

    def root(self, p):
        i = p
        while (i != self.ids[i]):
            #self.ids[i] = self.ids[self.ids[i]] # Path compression
            i = self.ids[i]
            print "i = {}, ids[i] ={}".format(i, self.ids[i])
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

if __name__ == "__main__":
    uf = UnionFind(10)
    # 1-2-3-4-5-6-7-8-9
    friend_list = [(1,2,1), (2,3,2), (5,6,3), (3,6,4), (8,9,5), (7,3,6), (4,1,7), (1,3,8), (7,9,9), (1,0,10)]
    for (p, q, ts) in friend_list:
        all_connected = uf.union(p, q)
        if all_connected:
            print "All friends were connected at ts = {}".format(ts)
            break
    if not all_connected:
        print "All friends were not connected"

