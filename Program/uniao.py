class UniaoDisjunta:
    def __init__(self, n):
        self.Pai, self.n = [None] * (n + 1), 0

    def Une(self, u, v):
        Ru = self.Conjunto(u)
        Rv = self.Conjunto(v)

        if Ru != Rv:
            if -self.Pai[Ru] < -self.Pai[Rv]:
                self.Pai[Ru], self.Pai[Rv] = Rv, self.Pai[Rv] + self.Pai[Ru]
            else:
                self.Pai[Rv], self.Pai[Ru] = Ru, self.Pai[Rv] + self.Pai[Ru]

    def Conjunto(self, u):
        if self.Pai[u] > 0:
            self.Pai[u] = self.Conjunto(self.Pai[u])
            return self.Pai[u]
        else:
            return u

    def Insere(self, u):
        self.Pai[self.n + 1], self.n = -1, self.n + 1