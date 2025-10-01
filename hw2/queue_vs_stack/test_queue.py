import pytest
from .queue import Queue


class TestQueue:
    """Тестовый класс для Queue"""
    
    def test_create_empty_queue(self):
        """Тест создания пустой очереди"""
        queue = Queue()
        assert queue.is_empty() is True
        assert queue.size() == 0
        assert len(queue) == 0
    
    def test_enqueue_single_element(self):
        """Тест добавления одного элемента"""
        queue = Queue()
        queue.enqueue(1)
        
        assert queue.is_empty() is False
        assert queue.size() == 1
        assert len(queue) == 1
        assert queue.front() == 1
    
    def test_enqueue_multiple_elements(self):
        """Тест добавления нескольких элементов"""
        queue = Queue()
        elements = [1, 2, 3, 4, 5]
        
        for element in elements:
            queue.enqueue(element)
        
        assert queue.size() == 5
        assert queue.front() == 1  # Первый добавленный элемент
    
    def test_dequeue_single_element(self):
        """Тест извлечения одного элемента"""
        queue = Queue()
        queue.enqueue(42)
        
        dequeued = queue.dequeue()
        assert dequeued == 42
        assert queue.is_empty() is True
        assert queue.size() == 0
    
    def test_dequeue_multiple_elements_fifo_order(self):
        """Тест извлечения элементов в порядке FIFO"""
        queue = Queue()
        elements = [1, 2, 3, 4, 5]
        
        # Добавляем элементы
        for element in elements:
            queue.enqueue(element)
        
        # Извлекаем в том же порядке
        dequeued_elements = []
        while not queue.is_empty():
            dequeued_elements.append(queue.dequeue())
        
        assert dequeued_elements == [1, 2, 3, 4, 5]
        assert queue.size() == 0
    
    def test_front_without_modification(self):
        """Тест просмотра элемента без изменения очереди"""
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        
        # Несколько раз проверяем front
        assert queue.front() == 10
        assert queue.front() == 10
        assert queue.size() == 2  # Размер не изменился
    
    def test_mixed_operations(self):
        """Тест смешанных операций"""
        queue = Queue()
        
        # Добавляем элементы
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.size() == 2
        
        # Извлекаем один
        assert queue.dequeue() == 1
        assert queue.size() == 1
        assert queue.front() == 2
        
        # Добавляем еще
        queue.enqueue(3)
        queue.enqueue(4)
        assert queue.size() == 3
        assert queue.front() == 2
        
        # Извлекаем все
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.is_empty() is True
    
    def test_dequeue_from_empty_queue_raises_exception(self):
        """Тест исключения при извлечении из пустой очереди"""
        queue = Queue()
        
        with pytest.raises(IndexError, match="dequeue from empty queue"):
            queue.dequeue()
    
    def test_front_empty_queue_raises_exception(self):
        """Тест исключения при просмотре пустой очереди"""
        queue = Queue()
        
        with pytest.raises(IndexError, match="front from empty queue"):
            queue.front()
    
    def test_queue_with_different_data_types(self):
        """Тест очереди с различными типами данных"""
        queue = Queue()
        
        queue.enqueue(1)
        queue.enqueue("hello")
        queue.enqueue([1, 2, 3])
        queue.enqueue({"key": "value"})
        
        assert queue.dequeue() == 1
        assert queue.dequeue() == "hello"
        assert queue.dequeue() == [1, 2, 3]
        assert queue.dequeue() == {"key": "value"}
    
    def test_queue_with_none_values(self):
        """Тест очереди с None значениями"""
        queue = Queue()
        
        queue.enqueue(None)
        queue.enqueue(1)
        queue.enqueue(None)
        
        assert queue.dequeue() is None
        assert queue.dequeue() == 1
        assert queue.dequeue() is None
        assert queue.is_empty()
    
    def test_large_queue(self):
        """Тест с большим количеством элементов"""
        queue = Queue()
        n = 1000
        
        # Добавляем много элементов
        for i in range(n):
            queue.enqueue(i)
        
        assert queue.size() == n
        assert queue.front() == 0
        
        # Извлекаем все
        for i in range(n):
            assert queue.dequeue() == i
        
        assert queue.is_empty()
    
    def test_string_representation(self):
        """Тест строкового представления очереди"""
        queue = Queue()
        
        # Пустая очередь
        assert str(queue) == "Queue([])"
        
        # Очередь с элементами
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        assert str(queue) == "Queue([1, 2, 3])"
        assert repr(queue) == str(queue)
    
    def test_queue_independence(self):
        """Тест независимости различных очередей"""
        queue1 = Queue()
        queue2 = Queue()
        
        queue1.enqueue(1)
        queue1.enqueue(2)
        
        queue2.enqueue("a")
        queue2.enqueue("b")
        
        assert queue1.size() == 2
        assert queue2.size() == 2
        assert queue1.front() == 1
        assert queue2.front() == "a"
        
        queue1.dequeue()
        assert queue1.size() == 1
        assert queue2.size() == 2  # Не изменился
    
    def test_enqueue_dequeue_alternating(self):
        """Тест чередующихся операций добавления и извлечения"""
        queue = Queue()
        
        # Добавляем и сразу извлекаем
        queue.enqueue(1)
        assert queue.dequeue() == 1
        assert queue.is_empty()
        
        # Повторяем несколько раз
        for i in range(5):
            queue.enqueue(i)
            assert queue.front() == i
            assert queue.dequeue() == i
            assert queue.is_empty()
    
    def test_queue_state_after_complete_empty(self):
        """Тест состояния очереди после полного опустошения"""
        queue = Queue()
        
        # Добавляем элементы
        for i in range(3):
            queue.enqueue(i)
        
        # Извлекаем все
        for i in range(3):
            queue.dequeue()
        
        # Проверяем, что очередь корректно пуста
        assert queue.is_empty()
        assert queue.size() == 0
        
        # Можем снова добавлять элементы
        queue.enqueue("test")
        assert queue.front() == "test"
        assert queue.size() == 1
    
    def test_queue_performance_pattern(self):
        """Тест паттерна использования очереди"""
        queue = Queue()
        
        # Имитируем работу очереди задач
        tasks = ["task1", "task2", "task3"]
        
        # Добавляем задачи
        for task in tasks:
            queue.enqueue(task)
        
        # Обрабатываем задачи
        processed = []
        while not queue.is_empty():
            task = queue.dequeue()
            processed.append(f"processed_{task}")
        
        assert processed == ["processed_task1", "processed_task2", "processed_task3"]
