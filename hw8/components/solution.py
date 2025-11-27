def find_connected_components(graph):
    if not graph:
        return []
    
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)
    
    visited = set()
    components = []
    
    def dfs(node, component):
        visited.add(node)
        component.add(node)
        
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)
    
    for node in all_nodes:
        if node not in visited:
            component = set()
            dfs(node, component)
            components.append(sorted(list(component)))
    
    return sorted(components)

