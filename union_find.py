class Set:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0 * size]


    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]


    def union(self, i, j):
        x = self.find(i)
        y = self.find(y)

        if x == y:
            return
        
        x_rank = self.rank[x]
        y_rank = self.rank[y]

        if x_rank < y_rank:
            self.parent[x] = y
        elif y_rank > x_rank:
            self.parent[y] = x
        else:
            self.parent[x] = y
            self.rank[y] = x