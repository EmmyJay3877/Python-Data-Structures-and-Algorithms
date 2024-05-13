"""
There is a bi-directional graph with n vertices, where each 
vertex is labeled from 0 to n - 1 (inclusive). The edges in the 
graph are represented as a 2D integer array edges, where each 
edges[i] = [ui, vi] denotes a bi-directional edge between vertex 
ui and vertex vi. Every vertex pair is connected by at most one edge, 
and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from 
vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if 
there is a valid path from source to destination, or false otherwise.
"""


class Solution(object):
    def bfs(self, graph, start, destination):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            current_vertex = queue.popleft()
            if current_vertex == destination:
                return True
            for neighbor in graph[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False
        
    def validPath(self, n, edges, source, destination):
        graph = {}
        for i in range(n):
            graph[i] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return self.bfs(graph, source, destination)
