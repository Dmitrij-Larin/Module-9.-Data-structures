class Node:
    """Создаём класс Node"""
    def __init__(self, data, next_node=None):
        """Задаём атрибуты класса Node"""
        self.data = data
        self.next_node = next_node


class Stack:
    """Создаём класс Stack"""
    def __init__(self, stack_size=5, top=None):
        """Задаём атрибуты класса Stack"""
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        """Добавляем данные в Stack"""
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            print("Стэк переполнен")
            return "Стэк переполнен"

    def pop(self):
        """Удаляем данные из Stack"""
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    def is_empty(self):
        """Проверяем, пуст ли Stack"""
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        """Проверяем, заполнен ли Stack"""
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):
        """Отчищаем Stack"""
        while self.top:
            self.pop()

    def get_data(self, index):
        """Дабавляем данные в Stack и проверяем их по индексу"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):
        """Определяем размер Stack"""
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        """Определяем количество числовых данных в Stack"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter


# stack = Stack()
# stack.push(1)
# stack.push("sta")
# stack.push(2)
# stack.push(2.5)
# stack.push("sta")
# print(stack.counter_int())