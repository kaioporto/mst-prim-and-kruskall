# Árvores geradoras mínimas (minimum cost spanning tree)

##Entendendo o algoritmo
- Primeiro, árvore geradora (spanning tree), sem o custo mínimo ainda.
- Partindo de um exemplo: um grafo cíclico c6
	- Ao retirar uma aresta, temos uma árvore
	- (árvore - grafo conexo que não possui ciclos)
	- (um grafo é uma arvore sse existir um, e apenas um caminho entre cada par de vértices)

> Definição: spanning tree é um subgrafo de um grafo G, contendo o mesmo conjunto de vertices e um subconjunto das arestas
	
	* subgrafo S esta contido em G
	* S = (V', E')
	* V = V'
	* |E'| = |V| \- 1

Ou seja, o número de arestas da arvore geradora é sempre o número de vértices do supergrafo menos 1. Remove-se uma aresta do grafo original (escolha arbitrária)
	

Então, para um dado grafo, quantas arvores geradoras podemos criar?
	no caso do C6, podemos gerar 6 arvores geradoras diferentes (tirando uma aresta de cada vez)

Se eu acrescentar uma aresta ao c6, formando outro ciclo, como por exemplo do 3 pro 5, ou do 2 pro 6, precisariamos 


### Grafo com pesos nas arestas




## Algoritmo de Kruskal

Objetivo de encontrar a arvore geradora de menor custo em um grafo (com pesos nas arestas)

O algoritmo encontra um subconjunto do grafo G tal que

	- cada vértice pertencente ao V' pertence a arvore
	- a soma dos pesos é o mínimo entre todas as arvores geradoras que podem ser formada a partir desse grafo


- passo a passo
	- ordena as arestas de acordo com seus pesos
	- começa a adicionar as arestas a arvore a partir da menor peso até a de maior peso 
	- só adiciona aresta que não forma ciclo. arestas que conectam somente componentes disconexos 


