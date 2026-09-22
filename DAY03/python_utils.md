# DAY03 — Python Utilities: List Methods

> Quick-reference cheat sheet for the most common `list` operations.

```python
nums = [1, 2, 3]
```

| Method | Example | What it does |
|---|---|---|
| `append(x)` | `nums.append(4)` | Adds one item to the end |
| `extend(iterable)` | `nums.extend([5, 6])` | Adds every item from the iterable |
| `insert(i, x)` | `nums.insert(1, 10)` | Inserts `x` at index `i` |
| `remove(x)` | `nums.remove(2)` | Removes the first occurrence of `x` |
| `pop()` | `nums.pop()` | Removes and returns the last item |
| `pop(i)` | `nums.pop(1)` | Removes and returns the item at index `i` |
| `index(x)` | `nums.index(3)` | Returns the index of the first occurrence of `x` |
| `count(x)` | `nums.count(3)` | Returns how many times `x` appears |
| `sort()` | `nums.sort()` | Sorts the list in place (ascending) |
| `reverse()` | `nums.reverse()` | Reverses the list in place |
| `copy()` | `nums.copy()` | Returns a shallow copy of the list |
| `clear()` | `nums.clear()` | Removes all items from the list |

## In-place vs. returning a new list

- `sort()`, `reverse()`, and `clear()` mutate the list and return `None`.
- `sorted(nums)`, `reversed(nums)`, and `nums.copy()` leave the original untouched.
