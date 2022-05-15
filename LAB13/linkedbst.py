"""
File: linkedbst.py
Author: Ken Lambert
"""
import random
import time
import sys

from Files.abstractcollection import AbstractCollection
from Files.bstnode import BSTNode
from Files.linkedstack import LinkedStack

sys.setrecursionlimit(300000)

class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            string = ""
            if node != None:
                string += recurse(node.right, level + 1)
                string += "| " * level
                string += str(node.data) + "\n"
                string += recurse(node.left, level + 1)
            return string

        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right != None:
                    stack.push(node.right)
                if node.left != None:
                    stack.push(node.left)

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        return None

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)

        recurse(self._root)
        return iter(lyst)

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        return None

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        return None

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""

        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self._root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal,
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
                # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def lift_max_in_left_subtree_to_top(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            current_node = top.left
            while not current_node.right == None:
                parent = current_node
                current_node = current_node.right
            top.data = current_node.data
            if parent == top:
                top.left = current_node.left
            else:
                parent.right = current_node.left

        # Begin main part of the method
        if self.isEmpty(): return None

        # Attempt to locate the node containing the item
        item_removed = None
        pre_root = BSTNode(None)
        pre_root.left = self._root
        parent = pre_root
        direction = 'L'
        current_node = self._root
        while not current_node == None:
            if current_node.data == item:
                item_removed = current_node.data
                break
            parent = current_node
            if current_node.data > item:
                direction = 'L'
                current_node = current_node.left
            else:
                direction = 'R'
                current_node = current_node.right

        # Return None if the item is absent
        if item_removed == None: return None

        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not current_node.left == None \
                and not current_node.right == None:
            lift_max_in_left_subtree_to_top(current_node)
        else:

            # Case 2: The node has no left child
            if current_node.left == None:
                new_child = current_node.right

                # Case 3: The node has no right child
            else:
                new_child = current_node.left

                # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = new_child
            else:
                parent.right = new_child

        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self._size -= 1
        if self.isEmpty():
            self._root = None
        else:
            self._root = pre_root.left
        return item_removed

    def replace(self, item, new_item):
        """
        If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        probe = self._root
        while probe != None:
            if probe.data == item:
                old_data = probe.data
                probe.data = new_item
                return old_data
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    @staticmethod
    def height1(top):
        '''
        Helper function
        :param top:
        :return:
        '''
        while top is not None:
            heights = []
            if top.left is not None:
                heights.append(LinkedBST.height1(top.left) + 1)
            if top.right is not None:
                heights.append(LinkedBST.height1(top.right) + 1)
            if len(heights) == 0:
                return 1
            return max(heights)
        return 0

    def height(self):
        '''
        Return the height of tree
        :return: int
        '''
        return LinkedBST.height1(self._root) - 1

    def is_balanced(self):
        '''
        Return True if tree is balanced
        :return:
        '''
        top = self._root
        def check_height_difference(top):
            return abs(LinkedBST.height1(top.left) - LinkedBST.height1(top.right)) <= 1
        def is_balanced_recurse(top):
            if not check_height_difference(top):
                return False
            else:
                if top.left is not None:
                    return is_balanced_recurse(top.left)
                if top.right is not None:
                    return is_balanced_recurse(top.right)
                return True
        return is_balanced_recurse(top)


    def range_find(self, low, high):
        '''
        Returns a list of the items in the tree, where low <= item <= high."""
        :param low:
        :param high:
        :return:
        '''
        lister = LinkedBST.list_parse(self._root)
        return [i for i in lister if i >= low and i <= high]

    @staticmethod
    def list_parse(top):
        """
        Helping function that returns list of all elements
        @param top:
        @return:
        """
        lister = []
        if top is not None:
            lister += [top.data]
            if top.left is not None:
                lister += (LinkedBST.list_parse(top.left))
            if top.right is not None:
                lister += (LinkedBST.list_parse(top.right))
        return sorted(lister)

    def rebalance(self):
        '''
        Rebalances the tree.
        :return:
        '''
        lister = LinkedBST.list_parse(self._root)
        tree = LinkedBST()

        def tree_create(tree, lister, node):
            tree.add(lister[len(lister) // 2])
            if len(lister[:len(lister) // 2]):
                tree_create(tree, lister[:len(lister) // 2], node)
            if len(lister[len(lister) // 2 + 1:]):
                tree_create(tree, lister[len(lister) // 2 + 1:], node)
            return tree

        self._root = tree_create(tree, lister, tree._root)._root

    def successor(self, item):
        """
        Returns the smallest item that is larger than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        lister = LinkedBST.list_parse(self._root)
        try:
            return [i for i in lister if i > item][0]
        except IndexError:
            return None
        # top = self._root
        # path = []
        # try:
        #     while top.data is not item:
        #         path.append(top.data)
        #         if top.data < item:
        #             top = top.right
        #         else:
        #             top = top.left
        # except AttributeError:
        #     return None
        # print(f"Path {path}")
        # # print(top.data)
        # if top.right is not None:
        #     top = top.right
        # else:
        #     for element in path[::-1]:
        #         if element > item:
        #             return element
        # while top.left is not None:
        #     top = top.left
        # return top.data


    def predecessor(self, item):
        """
        Returns the largest item that is smaller than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        # top = self._root
        # path = []
        # try:
        #     while top.data is not item:
        #         path.append(top.data)
        #         if top.data < item:
        #             top = top.right
        #         else:
        #             top = top.left
        # except AttributeError:
        #     return None
        # print(f"Path {path}")
        # # print(top.data)
        # if top.left is not None:
        #     top = top.left
        # else:
        #     for element in path[::-1]:
        #         if element < item:
        #             return element
        # while top.right is not None:
        #     top = top.right
        # return top.data
        lister = LinkedBST.list_parse(self._root)
        try:
            return [i for i in lister if i < item][-1]
        except IndexError:
            return None


    def demo_bst(self, path):
        """
        Demonstration of efficiency binary search tree for the search tasks.
        :param path:
        :type path:
        :return:
        :rtype:
        """
        words = []
        with open(path, encoding="utf-8") as file:
            for line in file:
                words.append(line.strip().split()[0])
        random_words = random.sample(words, 10000)

        # List test
        list_time_start = time.time()
        for word in random_words:
            words.index(word)
            # word in words
        list_time = time.time() - list_time_start
        print(f"Time of searching of 10000 words in list"
              f" using default methods: {list_time}")

        # Binary tree test (orderly addition)
        tree = LinkedBST()
        random_words_limited = random.sample(words[:1000], 1000)
        tree.add(words[0])
        top = tree._root
        for word in words[1:1000]:
            top.right = BSTNode(word)
            top = top.right
            tree._size += 1
        # for index in range(len(words)):
        #     tree.add(words[index])
        #     print(index)
        tree_orderly_time_start = time.time()
        for index in range(len(random_words_limited)):
            tree.find(random_words_limited[index])
        tree_orderly_time_end = time.time() - tree_orderly_time_start
        print(f"Time of searching of 10000 words in tree,"
        f"that was added orderly: {tree_orderly_time_end * 240 * 240}")
        print(f"Due to the problems with big bin trees, the tree is limited only to 240th part of the real array, and the actual time would be very big, so that's why there is no sense to run the whole array")

        # Binary tree test (random addition)
        tree = LinkedBST()
        for word in random.sample(words, len(words)):
            tree.add(word)
        tree_random_time_start = time.time()
        for word in random_words:
            tree.find(word)
        tree_random_time_end = time.time() - tree_random_time_start
        print(f"Time of searching of 10000 words in tree, "
              f"that was added randomly: {tree_random_time_end}")

        # Binary tree test (Balanced)
        tree.rebalance()
        tree_balanced_time_start = time.time()
        for word in random_words:
            tree.find(word)
        tree_balanced_time_end = time.time() - tree_balanced_time_start
        print(f"Time of searching of 10000 words in tree, "
              f"that was balanced: {tree_balanced_time_end}")




if __name__ == "__main__":
    random.seed(1337)
    b = LinkedBST()
    for i in range(30):
        b.add(random.randint(1,100))
    print(b)
    print(b.is_balanced())
    b.rebalance()
    print(b.is_balanced())
    print(b)
    print(b.successor(5))
    print(b.successor(55))
    print(b.predecessor(65))
    print(b.predecessor(47))
    print(b.predecessor(5))
    b = LinkedBST()
    b.demo_bst("words.txt")
