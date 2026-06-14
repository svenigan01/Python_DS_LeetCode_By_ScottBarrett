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
  
  

