# DAY01 — Classes, Pointers & Constructors

> Scott Barrett Python DSA course — Day 1 notes.
> Runnable examples: [examples.py](examples.py)

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
