from grafo import Grafo
class GrafoMatrizAdj(Grafo):
    def DefinirN(self, n):
        """
        Define o número n de vértices>
        """
        super(GrafoMatrizAdj, self).DefinirN(n)
        self.M = [None]*(self.n + 1)
        for i in range(1, self.n + 1):
            self.M[i] = [0] * (self.n + 1)

    def RemoverAresta(self, u, v):
        """
        Remove a aresta uv
        """
        self.M[u][v] = 0
        if not self.orientado:
            self.M[v][u] = 0
        self.m = self.m - 1

    def AdicionarAresta(self, u, v):
        """
        Adiciona aresta uv
        """
        self.M[u][v] = 1
        if not self.orientado:
            self[v][u] = 1
        self.m = self.m + 1

    def SaoAdj(self, u, v):
        """
        Retorna True se e somente se uv é uma aresta.
        """
        return self.M[u][v] == 1

    def N(self, v, Tipo = "*", Fechada = False, IterarSobreNo = False):
        """
        Retorna lista de vértices vizinhos do vértice v. Se Fechada = True, o próprio v é incluido na lista.
        Tipo = "*" significa listar todas as arestas incidentes em v. Se G é orientado, Tipo = "+" (rest. "-")
        significa listar apenas as arestas de saída (resp. entrada) de v.
        """
        if Fechada:
            yield v
        w = 1
        t = "+" if Tipo == "*" and self.orientado else Tipo
        while w <= self.n:
            if t == "+":
                orig, dest, viz = v, w, w
            else:
                orig, dest, viz = w, v, w
            if self.SaoAdj(orig, dest):
                yield w
            w = w + 1
            if w > self.n and t == "+" and Tipo == "*":
                t,w = "-", 1

