"""
LAB 11 1
"""
from node import *


# A class implementing Multiset as a linked list.

class Multiset:
    """
    Class for multiset - linked list
    """

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __len__(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.next
            self._head = current
        return count

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def __str__(self):
        current = self._head
        values = []
        while current is not None:
            values.append(current.item)
            current = current.next
        return str(values)

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        """
        приймає один аргумент - посилання на однозв’язаний список, по черзі
        видаляє всі його вузли та повертає всі значення у list. Якщо remove_all
        це метод екземпляра класу, то визначення методу матиме вигляд remove_all(self)
        @return:
        """
        current = self._head
        values = []
        while current is not None:
            values.append(current.item)
            current = current.next
            self._head = current
        return values

    def split_half(self):
        """
        приймає посилання на однозв’язаний список, ділить його на два одноз'язані
        списки однакового розміру та повертає посилання на ці списки. Якщо в
        структурі тільки один вузол то метод повинен повертати None. Якщо у структурі
        непарна кількість елементів то перший список повинен бути довшим.
        Якщо split_half це метод екземпляра класу то визначення методу матиме
        вигляд split_half(self). Під час поділу на два однозв'язні списки спочатку
        слід наповнити один однозв'язний список, а тоді другий. При пошуку алгоритму
        поділу списку на дві частини вартує крім варіанту на основі знаходження
        кількості елементів у структурі подумати над іншими можливостями.
        @return:
        """
        mult_set = Multiset()
        start = self._head
        current = self._head
        size = len(self)
        if size == 1:
            return None
        for _ in range((size+1)//2):
            previous = current
            current = current.next
        self._head = start
        previous.next = None
        mult_set._head = current

        return str(self), str(mult_set)


    def extend(self, head1):
        """
        приймає посилання на два однозв'язані списки та повертає посилання на
        один список, який буде складатися з елементів цих списків. Всі елементи
        другого списку повинні бути додані до першого списку. Цей метод доцільно
        використати для перевірки чи коректно працює попередній метод extend(self.split_half()).
        @param head1:
        @return:
        """
        current = head1._head
        while current.next is not None:
            current = current.next
        current.next = self._head
        return head1
