import heapq


def dijkstra(graph, start, end=None):
    if not graph:
        return {} if end is None else None
    
    if start not in graph:
        return {} if end is None else None
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    previous = {node: None for node in graph}
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if end is not None and current_node == end:
            break
        
        if current_dist > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                distance = current_dist + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
    
    if end is not None:
        if distances[end] == float('inf'):
            return None
        return distances[end]
    
    return distances


def dijkstra_with_path(graph, start, end):
    if not graph:
        return None, []
    
    if start not in graph or end not in graph:
        return None, []
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    previous = {node: None for node in graph}
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if current_node == end:
            break
        
        if current_dist > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                distance = current_dist + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
    
    if distances[end] == float('inf'):
        return None, []
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return distances[end], path

