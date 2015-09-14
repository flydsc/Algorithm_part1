class QuickUnionUF:
    def __init__(self, N):
        self.id = [i i in range(N)]

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(p)

    def union(self, p, q):
        i = root(p)
        j = root(q)
        id[i] = j
