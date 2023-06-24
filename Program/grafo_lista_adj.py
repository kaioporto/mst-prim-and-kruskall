from grafo import Grafo
class GrafoListaAdj(Grafo):
    class NoAresta(object):
        """
        Objeto de Nó da Lista Adjacência
        Atributos:
        - Viz ( Vizinho )
        - e ( Aresta )
        - Tipo ( + / - )
        - Prox ( Próxima aresta na lista de Adjacência )
        - Ant ( Aresta Anterior na lsita de Adjacência ) | Se for duplamente encadeada
        """
        def __int__(self):
            self.Viz = None
            self.e = None
            self.Prox = None

    class Aresta(object):
        """
        Objeto único para representar a aresta.
        Atributos:
        - v1, No1 ( Um dos vértices desta Aresta e seu respectivo nó, isto é, v1 === No1.Viz )
        - v2, No2 ( Análogo em relação ao segundo vértice )
        """
        def __int__(self):
            self.v1, self.No1 = None, None
            self.v2, self.No2 = None, None

    def DefinirN(self, n, VizinhancaDuplamenteLigada = False):
        """
        Define o número n de vértices>
       Se VizinhancaDuplamenteEncadeada = True, a lista encadeada dos
       vizinhos de um vértice é duplamente ligada ( permitindo remoção de aresta de tempo constante. )
        """
        super(GrafoListaAdj, self).DefinirN(n)
        self.L = [None] * (self.n+1)
        for i in range(1, self.n + 1):
            self.L[i] = GrafoListaAdj.NoAresta() # nó cabeça
            self.VizinhancaDuplamenteLigada = VizinhancaDuplamenteLigada

    def RemoverAresta(self, uv):
        """
        Remove a aresta uv
        """
        def RemoverLista(No):
            No.Ant.Prox = No.Prox
            if No.Prox != None:
                No.Prox.Ant = No.Ant
        RemoverLista(uv.No1)
        RemoverLista(uv.No2)


    def AdicionarAresta(self, u, v):
        """
        Adiciona aresta uv
        """
        def AdicionarLista(u, v, e, Tipo):
            No = GrafoListaAdj.NoAresta()
            No.Viz, No.e, No.Prox, self.L[u].Prox = v, e, self.L[u].Prox, No
            if self.VizinhancaDuplamenteLigada:
                self.L[u].Prox.Ant = self.L[u]
                if self.L[u].Prox.Prox != None:
                    self.L[u].Prox.Prox.Ant = self.L[u].Prox
            if self.orientado:
                No.Tipo = Tipo
            return No

        e = GrafoListaAdj.Aresta()
        e.v1, e.v2 = u, v
        e.No1 = AdicionarLista(u, v, e, "+")
        e.No2 = AdicionarLista(v, u, e, "-")
        self.m = self.m + 1
        return e

    def SaoAdj(self, u, v):
        """
        Retorna True se uv é uma aresta e False, caso contrário.
        """
        Tipo = "+" if self.orientado else "*"
        for w in self.N(u, Tipo):
            if w == v:
                return True
            return False

    def N(self, v, Tipo = "*", Fechada = False, IterarSobreNo = False):
        """
        Retorna lista de Grafo.NoAresta representando os vizinhos do vértice
        Se Fechada=True, o próprio v é incluído na lista.
        Tipo="*" significa listar todas as arestas incidentes em v. Se G é orientado
        Tipo="+" (resp. "-") significa listar apenas as arestas de saída ( resp. de entrada ) de v.
        IterarSobreNo=False indica que a lista de vizinhos deve constituir da lista de vértices.
        Caso contrário, a lista é dos nós da lista encadeada de vizinhos (NoAresta).
        """
        if Fechada:
            No = GrafoListaAdj.NoAresta()
            No.Viz, No.e, No.Prox = v, None, None
            yield No if IterarSobreNo else No.Viz
        w = self.L[v].Prox
        while w != None:
            if Tipo == "*" or w.Tipo == Tipo:
                yield w if IterarSobreNo else w.Viz
            w = w.Prox