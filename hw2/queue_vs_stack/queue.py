from .linked_list import Node


class Queue:
    """Очередь (FIFO - First In, First Out) на основе связного списка"""
    
    def __init__(self):
        self._front = None  # Начало очереди (откуда извлекаем)
        self._rear = None   # Конец очереди (куда добавляем)
        self._size = 0
    
    def enqueue(self, data):
        """Добавить элемент в конец очереди"""
        new_node = Node(data)
        
        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        
        self._size += 1
    
    def dequeue(self):
        """Удалить и вернуть элемент из начала очереди"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        data = self._front.data
        self._front = self._front.next
        
        # Если очередь стала пустой, обнуляем rear
        if self._front is None:
            self._rear = None
        
        self._size -= 1
        return data
    
    def front(self):
        """Посмотреть элемент в начале очереди без удаления"""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._front.data
    
    def is_empty(self):
        """Проверить, пуста ли очередь"""
        return self._front is None
    
    def size(self):
        """Получить размер очереди"""
        return self._size
    
    def __len__(self):
        """Размер очереди для len()"""
        return self._size
    
    def __str__(self):
        """Строковое представление очереди"""
        if self.is_empty():
            return "Queue([])"
        
        elements = []
        current = self._front
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return f"Queue([{', '.join(elements)}])"
    
    def __repr__(self):
        return self.__str__()
