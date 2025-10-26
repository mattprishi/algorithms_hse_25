class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def pre_order(self):
        result = []
        self._pre_order_recursive(self.root, result)
        return result
    
    def _pre_order_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)
    
    def in_order(self):
        result = []
        self._in_order_recursive(self.root, result)
        return result
    
    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.value)
            self._in_order_recursive(node.right, result)
    
    def post_order(self):
        result = []
        self._post_order_recursive(self.root, result)
        return result
    
    def _post_order_recursive(self, node, result):
        if node:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.value)
    
    def reverse_pre_order(self):
        result = []
        self._reverse_pre_order_recursive(self.root, result)
        return result
    
    def _reverse_pre_order_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._reverse_pre_order_recursive(node.right, result)
            self._reverse_pre_order_recursive(node.left, result)
    
    def reverse_in_order(self):
        result = []
        self._reverse_in_order_recursive(self.root, result)
        return result
    
    def _reverse_in_order_recursive(self, node, result):
        if node:
            self._reverse_in_order_recursive(node.right, result)
            result.append(node.value)
            self._reverse_in_order_recursive(node.left, result)
    
    def reverse_post_order(self):
        result = []
        self._reverse_post_order_recursive(self.root, result)
        return result
    
    def _reverse_post_order_recursive(self, node, result):
        if node:
            self._reverse_post_order_recursive(node.right, result)
            self._reverse_post_order_recursive(node.left, result)
            result.append(node.value)

