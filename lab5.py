def read_graph_from_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    root = int(lines[0])
    edges = [tuple(map(int, line.split(','))) for line in lines[1:]]

    graph = {}
    for u, v in edges:

        
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    return root, graph

def find_min_depth(root, graph):
    queue = [(root, 1, [root])]
    visited = []

    while queue:
        node, depth, path = queue.pop(0)

        if node not in graph or not graph[node]:
            return depth, path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append((neighbor, depth + 1, path + [neighbor]))

    return 0, []

def write_result_to_file(filename, depth, path):
    with open(filename, 'w') as f:
        f.write(f"{depth}\n")
        f.write(" " + " > ".join(map(str, path)))


def main():
    root, graph = read_graph_from_file('input.txt')
    depth, path = find_min_depth(root, graph)
    write_result_to_file('output.txt', depth, path)

if __name__ == "__main__":
    main()

