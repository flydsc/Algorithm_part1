class QuickFindUF:
    id = []

    def __init__(self, N):
        self.id = []
        for i in range(N):
            self.id[i] = i

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if id[i] == pid:
                id[i] = qid
