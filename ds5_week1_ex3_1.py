import networkx as nx
import matplotlib.pyplot as plt
import random

def create_star(k):
    graph = nx.Graph()

    for i in range(1, k+1):
        graph.add_edge(0,i)

    return graph 

def add_page(graph, M):
    new_page= len(graph.nodes)
    nodes = list(graph.nodes)
    degrees =[]

    for node in nodes:
        degrees.append(graph.degree(node))

    chosen = random.choices(nodes, weights=degrees, k=M)

    for node in chosen:
        graph.add_edge(new_page, node)

    return graph 


def create_network(N, M, k):
    graph = create_star(k)

    while len(graph.nodes) < N:
        graph = add_page(graph, M)

    return graph

def page_rank(graph, steps):
    nodes = list(graph.nodes)
    page = random.choice(nodes)

    visits = {}

    for node in nodes:
        visits[node] = 0

    for i in range(steps):
        visits[page] += 1

        neighbours = list(graph.neighbors(page))

        if random.random() < 0.85:
            page = random.choice(neighbours)
        else:
            page = random.choice(nodes)

    for node in nodes:
        visits[node] = visits[node] / steps

    return visits

def draw_network(graph):
    nx.draw(graph, with_labels=True)
    plt.show()

def draw_pagerank(rank):
    plt.hist(rank.values())
    plt.show()

N = 400
M = 4
k = 5

graph = create_network(N, M, k)
draw_network(graph)
rank = page_rank(graph, 10000)
draw_pagerank(rank)