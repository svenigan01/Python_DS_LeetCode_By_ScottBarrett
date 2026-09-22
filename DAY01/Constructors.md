# DAY01 — Classes, Pointers & Constructors

> Scott Barrett Python DSA course — Day 1 notes.

## 1. Classes

### Concept

- A class is a **cookie-cutter**: built-in types like `int` and `str` are classes, and you stamp out instances (objects) from them.
- Inside a method, `self` refers to the instance the method was called on — it's passed implicitly.

### Example — the `Cookie` class

```python
class Cookie:
    def __init__(self, color):   # self is the instance, passed implicitly
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one color is:', cookie_one.getColor())
print('Cookie two color is:', cookie_two.getColor())

cookie_one.setColor('yellow')

print('Cookie one color is:', cookie_one.getColor())
print('Cookie two color is:', cookie_two.getColor())
```

**Expected output:**

```
Cookie one color is: green
Cookie two color is: blue
Cookie one color is: yellow
Cookie two color is: blue
```

## 2. Pointers

### Concept

- Variables are **pointers** to objects in memory.
- **Immutable** objects (e.g. `int`): assigning a new value points the variable at a *different* object — other variables pointing at the old object are unaffected.
- **Mutable** objects (e.g. `dict`): mutating in place keeps the *same* object, so every variable pointing at it sees the change.
- When nothing points at an object anymore, Python's garbage collector frees that memory.

### Example 1 — integers are immutable

```python
num1 = 11
num2 = num1            # num2 points at the SAME object as num1

print('Before num2 is updated:')
print('num1 is:', num1)
print('num2 is:', num2)
print('num1 id:', id(num1))
print('num2 id:', id(num2))    # same id -> same object

num2 = 22             # num2 now points at a DIFFERENT object

print('After num2 is updated:')
print('num1 is:', num1)
print('num2 is:', num2)
print('num1 id:', id(num1))    # unchanged
print('num2 id:', id(num2))    # different id
```

**Expected output** (ids vary on every run):

```
Before num2 is updated:
num1 is: 11
num2 is: 11
num1 id: 14062597538816
num2 id: 14062597538816
After num2 is updated:
num1 is: 11
num2 is: 22
num1 id: 14062597538816
num2 id: 14062597538960
```

### Example 2 — dicts are mutable

```python
dict1 = {'value': 11}
dict2 = dict1             # dict2 points at the SAME object as dict1

print('Before dict2 is updated:')
print('dict1 is:', dict1)
print('dict2 is:', dict2)
print('dict1 id:', id(dict1))
print('dict2 id:', id(dict2))    # same id -> same object

dict2['value'] = 22      # mutates the shared object in place

print('After dict2 is updated:')
print('dict1 is:', dict1)        # dict1 sees the change too
print('dict2 is:', dict2)
print('dict1 id:', id(dict1))    # same object, same id
print('dict2 id:', id(dict2))
```

**Expected output** (ids vary on every run):

```
Before dict2 is updated:
dict1 is: {'value': 11}
dict2 is: {'value': 11}
dict1 id: 14062597538816
dict2 id: 14062597538816
After dict2 is updated:
dict1 is: {'value': 22}
dict2 is: {'value': 22}
dict1 id: 14062597538816
dict2 id: 14062597538816
```

## 3. Constructors

### Concept

- The constructor (`__init__`) builds a new instance: a fresh object is allocated, its attributes are set, and it is returned.
- Linked-list construction, step by step: `Node(4)` → a node with `value = 4` and `next = None`; `LinkedList(4)` → `head` and `tail` both point at that node, `length = 1`.

### Example — `Node` and `LinkedList` constructors

```python
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


my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
```

**Expected output:**

```
Head: 4
Tail: 4
Length: 1
```

### Methods to build next

These `LinkedList` methods will be implemented in the coming days:

```python
class LinkedList:
    def append(self, value):
        ...

    def pop(self):
        ...

    def insert(self, index, value):
        ...

    def prepend(self, value):
        ...
```
