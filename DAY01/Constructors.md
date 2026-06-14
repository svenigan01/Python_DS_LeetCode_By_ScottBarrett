CLASSES

Concept

1. Cookie-cutter class
Built-in data-types int, str etc also cookie-cutter
class Cookie:
  def __init__(self, color): # self is implicit method
    self.color = color
  def getColor(self):
    return self.color
  def setColor(self, color):
    self.color = color

cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one color is: ', cookie_one.getColor())
print('Cookie two color is: ', cookie_two.getColor())
cookie_one.setColor('Yellow')
print('Cookie one color is: ', cookie_one.getColor())
print('Cookie two color is: ', cookie_two.getColor())

Output:
Cookie one color is: green
Cookie two color is: blue
Cookie one color is: Yellow
Cookie two color is: blue

E.g. LinkedList class
class LinkedList:
  def __init__(self, value):
  def append(self, value):
  def pop(self):
  def insert(self, index, value):
  def prepend(self, value):
  

POINTERS
Concept
1. Integers are immutable

num1 = 11
num2 = num1
print('Before num2 value is updated')
print('num1 is: ', num1)
print('num2 is: ', num2)
print('num1 points to: ', id(num1))
print('num2 points to: ', id(num2))
num2 = 22
print('After num2 value is updated')
print('num1 is: ', num1)
print('num2 is: ', num2)
print('num1 points to: ', id(num1))
print('num2 points to: ', id(num2))

Output:
num1 is: 11
num2 is: 11
num1 points to: 1234423
num1 points to: 1234423
After update
num1 is: 11
num2 is: 22
num1 points to: 1234423
num1 points to: 1234534

2. Dict elements are mutable

dict1 = {
          'value': 11
        }
dict2 = dict1
        
print('Before dict2 value is updated')
print('dict1 is: ', dict1)
print('dict2 is: ', dict2)
print('dict1 points to: ', id(dict1))
print('dict2 points to: ', id(dict2))
dict2['value'] = 22
print('After num2 value is updated')
print('dict1 is: ', dict1)
print('dict2 is: ', dict2)
print('num1 points to: ', id(dict1))
print('num2 points to: ', id(dict2))

Output:
dict1 is: {'value', 11}
dict2 is: {'value', 11}
dict1 points to: 14062597538816
dict1 points to: 14062597538816
After update
dict1 is: {'value', 22}
dict1 is: {'value', 22}
dict1 points to: 14062597538816
dict1 points to: 14062597538816
** If dictionary item has all pointers reassigned, garbage collector is run to release these locations

===========
Constructors

Concept:
1. Node and LinkedList constructors
   new_node = None -> new_node.value = 4 new_node.next = None
   my_linked_list = Node(4) -> None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1



my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                      


