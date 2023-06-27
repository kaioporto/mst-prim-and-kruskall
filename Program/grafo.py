class Grafo(object):
    """
    Classe Base para as classes GrafoListaAdj e GrafoMatrizAdj
    """
    def __int__(self, orientado = False):
        self.n, self.m, self.orientado = None, None, orientado

    def set_quantity_vertices(self, quantity):
        """
        Define o número n de vértices
        """
        self.n, self.m = quantity,0

    def get_vertices(self):
        """
        Retorna a Lista de Vértices
        """
        for i in range(1, self.n + 1):
            yield i

    def E(self, IterararSobreNo = False):
        """
        Retorna lista de aresta uv, onde u é um inteiro e v é um inteiro se o grafo é GrafoMatrizAdj
        ou InterarSobreNo=False; v é GrafoListaAdj.Node, caso contrário.
        """
        for v in self.get_vertices():
            for w in self.get_neighbors(v, Tipo = "+" if self.orientado else "*", IterararSobreNo=IterararSobreNo):
                enumerar = True
                if not self.orientado:
                    wint = w if isinstance(w, int) else w.neighbor
                    enumerar = v < wint
                if enumerar:
                    yield (v, w)