import csv

def read_csv(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    farms = [x.strip() for x in rows[0]]
    stores = [x.strip() for x in rows[1]]
    roads = []
    for row in rows[2:]:
        u, v, c = row[0].strip(), row[1].strip(), int(row[2].strip())
        roads.append((u, v, c))

    return farms, stores, roads

def build_graph(farms, stores, roads):
    graph = {}

    def add_edge(u, v, c):
        if u not in graph:
            graph[u] = {}
        if v not in graph[u]:
            graph[u][v] = 0
        graph[u][v] += c

    for u, v, c in roads:
        add_edge(u, v, c)

    for farm in farms:
        add_edge('SRC', farm, 10**9)
    for store in stores:
        add_edge(store, 'SNK', 10**9)

    return graph

def bfs(graph, flow, source, sink, parent):
    queue = [source]
    visited = {source: True}
    parent[source] = None

    while queue:
        u = queue.pop(0)
        for v in graph.get(u, {}):
            residual = graph[u][v] - flow[u][v]
            if v not in visited and residual > 0:
                parent[v] = u
                visited[v] = True
                if v == sink:
                    return True
                queue.append(v)
    return False

def edmonds_karp(graph, source, sink):
    flow = {}
    nodes = set()
    for u in graph:
        nodes.add(u)
        for v in graph[u]:
            nodes.add(v)

    flow = {}
    for u in nodes:
        flow[u] = {}
        for v in nodes:
            flow[u][v] = 0

    max_flow = 0
    parent = {}

    while bfs(graph, flow, source, sink, parent):
        path_flow = 10**9
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v] - flow[u][v])
            v = u

        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u

        max_flow += path_flow

    return max_flow

def main():
    farms, stores, roads = read_csv('roads.csv')
    graph = build_graph(farms, stores, roads)
    max_delivery = edmonds_karp(graph, 'SRC', 'SNK')
    print("Максимальна кількість автомобілів:", max_delivery)

if __name__ == "__main__":
    main()

