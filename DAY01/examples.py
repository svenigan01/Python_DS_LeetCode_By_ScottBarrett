"""DAY01 runnable examples: classes, pointers, and constructors."""

print("=== 1. Cookie class ===")


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

print()
print("=== 2a. Pointers: integers are immutable ===")

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

print()
print("=== 2b. Pointers: dicts are mutable ===")

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

print()
print("=== 3. Node and LinkedList constructors ===")


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
