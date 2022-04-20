"""
File: node.py

Node classes for one-way linked structures and two-way
linked structures.
"""

class Node:

    def __init__(self, data, previous=None, next=None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next
        self.previous = previous

class Knot:
    """Lightweight, nonpublic
    class for storing a singly linked node.
    """

    __slots__ = "_element", "_next"     # streamline memory usage

    def __init__(self, element, next):  # initialize node’s fields
        self._element = element         # reference to user’s element
        self._next = next               # reference to next node
