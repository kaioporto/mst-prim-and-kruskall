from grafo import Grafo
class GrafoListaAdj(Grafo):
    class Node(object):
        """
        Objeto de Nó da Lista Adjacência
        Atributos:
        - neighbor ( Vizinho )
        - e ( Aresta )
        - Tipo ( + / - )
        - Prox ( Próxima aresta na lista de Adjacência )
        - Ant ( Aresta Anterior na lsita de Adjacência ) | Se for duplamente encadeada
        """
        def __int__(self):
            self.neighbor = None
            self.edge = None
            self.Prox = None

    class Edge(object):
        """
        Objeto único para representar a aresta.
        Atributos:
        - vertex_one, No1 ( Um dos vértices desta Aresta e seu respectivo nó, isto é, vertex_one === No1.neighbor )
        - vertex_two, No2 ( Análogo em relação ao segundo vértice )
        """
        def __int__(self):
            self.vertex_one, self.No1 = None, None
            self.vertex_two, self.No2 = None, None
            self.weight = 0

    def set_quantity_vertices(self, quantity, VizinhancaDuplamenteLigada = False):
        """
        Define o número n de vértices>
       Se VizinhancaDuplamenteEncadeada = True, a lista encadeada dos
       vizinhos de um vértice é duplamente ligada ( permitindo remoção de aresta de tempo constante. )
        """
        super(GrafoListaAdj, self).set_quantity_vertices(quantity)
        self.L = [None] * (self.n+1)
        for i in range(1, self.n + 1):
            self.L[i] = GrafoListaAdj.Node() # nó cabeça
            self.VizinhancaDuplamenteLigada = VizinhancaDuplamenteLigada

    def RemoverAresta(self, uv):
        """
        Remove a aresta uv
        """
        def RemoverLista(a_node):
            a_node.Ant.Prox = a_node.Prox
            if a_node.Prox != None:
                a_node.Prox.Ant = a_node.Ant
        RemoverLista(uv.No1)
        RemoverLista(uv.No2)


    def add_edge(self, u, v, weight = 0):
        """
        Adiciona aresta uv
        """
        def AdicionarLista(u, v, e, Tipo):
            a_node = GrafoListaAdj.Node()
            a_node.neighbor, a_node.edge, a_node.Prox, self.L[u].Prox = v, e, self.L[u].Prox, a_node
            if self.VizinhancaDuplamenteLigada:
                self.L[u].Prox.Ant = self.L[u]
                if self.L[u].Prox.Prox != None:
                    self.L[u].Prox.Prox.Ant = self.L[u].Prox
            if self.orientado:
                a_node.Tipo = Tipo
            return a_node

        e = GrafoListaAdj.Edge()
        e.vertex_one, e.vertex_two, e.weight = u, v, weight
        e.No1 = AdicionarLista(u, v, e, "+")
        e.No2 = AdicionarLista(v, u, e, "-")
        self.m = self.m + 1
        return e

    def SaoAdj(self, u, v):
        """
        Retorna True se uv é uma aresta e False, caso contrário.
        """
        Tipo = "+" if self.orientado else "*"
        for w in self.get_neighbors(u, Tipo):
            if w == v:
                return True
            return False

    def get_neighbors(self, v, Tipo = "*", Fechada = False, use_node=False):
        """
        Retorna lista de Grafo.Node representando os vizinhos do vértice
        Se Fechada=True, o próprio v é incluído na lista.
        Tipo="*" significa listar todas as arestas incidentes em v. Se G é orientado
        Tipo="+" (resp. "-") significa listar apenas as arestas de saída ( resp. de entrada ) de v.
        use_node=False indica que a lista de vizinhos deve constituir da lista de vértices.
        Caso contrário, a lista é dos nós da lista encadeada de vizinhos (Node).
        """
        if Fechada:
            a_node = GrafoListaAdj.Node()
            a_node.neighbor, a_node.edge, a_node.Prox = v, None, None
            yield a_node if use_node else a_node.neighbor
        w = self.L[v].Prox
        while w != None:
            if Tipo == "*" or w.Tipo == Tipo:
                yield w if use_node else w.neighbor
            w = w.Prox