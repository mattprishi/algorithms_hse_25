from .linked_list import Node


class Stack:
    """Стек (LIFO - Last In, First Out) на основе связного списка"""
    
    def __init__(self):
        self._top = None
        self._size = 0
    
    def push(self, data):
        """Добавить элемент на вершину стека"""
        new_node = Node(data)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
    
    def pop(self):
        """Удалить и вернуть элемент с вершины стека"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data
    
    def peek(self):
        """Посмотреть элемент на вершине стека без удаления"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._top.data
    
    def is_empty(self):
        """Проверить, пуст ли стек"""
        return self._top is None
    
    def size(self):
        """Получить размер стека"""
        return self._size
    
    def __len__(self):
        """Размер стека для len()"""
        return self._size
    
    def __str__(self):
        """Строковое представление стека"""
        if self.is_empty():
            return "Stack([])"
        
        elements = []
        current = self._top
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return f"Stack([{', '.join(elements)}])"
    
    def __repr__(self):
        return self.__str__()
