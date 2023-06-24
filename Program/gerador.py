from uniao import UniaoDisjunta
from grafo_lista_adj import GrafoListaAdj
from grafo_matriz_adj import GrafoMatrizAdj
def ArvoreGerMinima(G: GrafoListaAdj|GrafoMatrizAdj):
    S = UniaoDisjunta(G.n)
    for v in G.V():
        S.Insere(v)

    ET = []; E = []

    for v in G.V():
        for w_no in G.N(v, IterarSobreNo=True):
            if w_no.Viz < v:
                E.append(w_no.e)
    E.sort(key=lambda e: e.w)
    for e in E:
        v,w = e.v1, e.v2
        if S.Conjunto(v) != S.Conjunto(w):
            S.Une(v, w)
            ET.append(e)
    return ET