import heapq

def prim_mst(graph, start_vertex):
    mst = []
    visited = set()
    min_heap = [(0, start_vertex, None)]  # (weight, current_vertex, previous_vertex)

    while min_heap:
        weight, current_vertex, prev_vertex = heapq.heappop(min_heap)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)
        if prev_vertex is not None:
            mst.append((prev_vertex, current_vertex, weight))

        for neighbor, edge_weight in graph[current_vertex]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_vertex))

    return mst

# Example usage:
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 4), ('D', 2)],
    'C': [('A', 3), ('B', 4), ('D', 2)],
    'D': [('B', 2), ('C', 2), ('E', 5)],
    'E': [('D', 5)]
}

mst = prim_mst(graph, 'A')
print("Prim's MST:", mst)
