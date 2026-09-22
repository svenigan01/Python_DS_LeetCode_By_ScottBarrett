"""DAY03 runnable demo: the most common list methods."""

nums = [1, 2, 3]
print("start:        ", nums)

nums.append(4)
print("append(4):    ", nums)

nums.extend([5, 6])
print("extend([5, 6]):", nums)

nums.insert(1, 10)
print("insert(1, 10):", nums)

nums.remove(2)
print("remove(2):    ", nums)

last = nums.pop()
print("pop() ->", last, " | list:", nums)

second = nums.pop(1)
print("pop(1) ->", second, " | list:", nums)

print("index(3) ->", nums.index(3))
print("count(3) ->", nums.count(3))

nums.sort()
print("sort():       ", nums)

nums.reverse()
print("reverse():    ", nums)

copy = nums.copy()
print("copy() ->", copy)

nums.clear()
print("clear():      ", nums)
