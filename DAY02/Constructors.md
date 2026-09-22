# DAY02 — Constructors (continued): Doubly Linked List

> Scott Barrett Python DSA course — Day 2 notes.

## Concept

- A **doubly linked list** node stores a `prev` pointer as well as `next`, so the list can be traversed backwards.
- `append` runs in **O(1)**: link the new node after the current tail, then move the `tail` pointer forward.

## Code

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(8)

my_doubly_linked_list.print_list()
```

**Expected output:**

```
7
8
```

## Cleanup notes (2026-09-22)

- Added the missing `self.length = 1` in `__init__` — the original `append` incremented `self.length`, which would have raised `AttributeError` on a list built this way.
- Added the `print_list` method, which the original notes called but never defined.
