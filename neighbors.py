from sets import Set


def dfs(adj, index, visited, current_cluster):
    visited.add(index)
    current_cluster.append(index)

    for node in range(len(adj)):
        if node not in visited and adj[index][node] == '1':
            dfs(adj, node, visited, current_cluster)

    return current_cluster, visited


def count_clusters(adj):
    visited = Set([])
    num_clusters = 0

    for i in range(len(adj)):
        if i in visited:
            continue
        cluster, visited = dfs(adj, i, visited, [])
        print cluster
        if cluster:
            num_clusters += 1

    print 'Clusters: ', num_clusters


if __name__ == "__main__":
    MATRIX = ['10010', '01001', '00100', '10010', '01001']

    count_clusters(MATRIX)
