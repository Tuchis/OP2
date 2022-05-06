"""
Stack to queue converter.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack
from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    """
    Returns queue from the stack.
    """
    queue = ArrayQueue()
    elems = []
    for elem in stack:
        elems.append(elem)
    for elem in elems[::-1]:
        queue.add(elem)
    return queue

def main():
    """
    MAIN FUNCTION
    """
    stack = ArrayStack()
    for i in range(10):
        stack.add(i)
    queue = stack_to_queue(stack)
    print(queue)
    #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(stack)
    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(stack.pop())
    #9
    print(queue.pop())
    #9
    stack.add(11)
    queue.add(11)
    print(queue)
    #[8, 7, 6, 5, 4, 3, 2, 1, 0, 11]
    print(stack)
    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 11]


if __name__ == "__main__":
    main()
