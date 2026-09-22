"""DAY04: singly linked list with append, prepend, pop, and insert."""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        """Add a node to the end. O(1)."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        """Add a node to the start. O(1)."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        """Remove and return the last node. O(n)."""
        if self.length == 0:
            return None
        current = self.head
        previous = self.head
        while current.next is not None:
            previous = current
            current = current.next
        self.tail = previous
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current

    def insert(self, index, value):
        """Insert a node at index. O(n)."""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


if __name__ == "__main__":
    my_linked_list = LinkedList(4)
    my_linked_list.append(7)
    my_linked_list.prepend(1)
    my_linked_list.insert(2, 99)

    my_linked_list.print_list()

    popped = my_linked_list.pop()
    print("popped:", popped.value)

    my_linked_list.print_list()
