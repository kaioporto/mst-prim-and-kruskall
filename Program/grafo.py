class Grafo(object):
    """
    Classe Base para as classes GrafoListaAdj e GrafoMatrizAdj
    """
    def __int__(self, orientado = False):
        self.n, self.m, self.orientado = None, None, orientado

    def DefinirN(self, n):
        """
        Define o número n de vértices
        """
        self.n, self.m = n,0

    def V(self):
        """
        Retorna a Lista de Vértices
        """
        for i in range(1, self.n + 1):
            yield i

    def E(self, IterararSobreNo = False):
        """
        Retorna lista de aresta uv, onde u é um inteiro e v é um inteiro se o grafo é GrafoMatrizAdj
        ou InterarSobreNo=False; v é GrafoListaAdj.NoAresta, caso contrário.
        """
        for v in self.V():
            for w in self.N(v, Tipo = "+" if self.orientado else "*", IterararSobreNo=IterararSobreNo):
                enumerar = True
                if not self.orientado:
                    wint = w if isinstance(w, int) else w.Viz
                    enumerar = v < wint
                if enumerar:
                    yield (v, w)