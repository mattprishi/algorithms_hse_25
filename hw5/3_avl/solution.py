class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def get_balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def update_height(self, node):
        if node is None:
            return
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def rotate_right(self, z):
        y = z.left
        temp = y.right
        
        y.right = z
        z.left = temp
        
        self.update_height(z)
        self.update_height(y)
        
        return y
    
    def rotate_left(self, z):
        y = z.right
        temp = y.left
        
        y.left = z
        z.right = temp
        
        self.update_height(z)
        self.update_height(y)
        
        return y
    
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        else:
            return node
        
        self.update_height(node)
        
        balance = self.get_balance_factor(node)
        
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node, key):
        if node is None:
            return node
        
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            successor = self._get_min_node(node.right)
            node.key = successor.key
            node.right = self._delete_recursive(node.right, successor.key)
        
        if node is None:
            return node
        
        self.update_height(node)
        
        balance = self.get_balance_factor(node)
        
        if balance > 1 and self.get_balance_factor(node.left) >= 0:
            return self.rotate_right(node)
        
        if balance > 1 and self.get_balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        if balance < -1 and self.get_balance_factor(node.right) <= 0:
            return self.rotate_left(node)
        
        if balance < -1 and self.get_balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    def _get_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if node is None:
            return False
        
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
    
    def is_balanced(self):
        return self._is_balanced_recursive(self.root)
    
    def _is_balanced_recursive(self, node):
        if node is None:
            return True
        
        balance = self.get_balance_factor(node)
        if abs(balance) > 1:
            return False
        
        return self._is_balanced_recursive(node.left) and self._is_balanced_recursive(node.right)

