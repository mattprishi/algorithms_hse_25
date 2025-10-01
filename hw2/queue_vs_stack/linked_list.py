class Node:
    """Узел связного списка"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"
