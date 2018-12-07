# 01.04 Finding the Largest or Smallest N Items

# Problem
# You want to make a list of the largest or smallest N items in a collection.

# Solution
# The 'heapq' module has two functions - nlargest() and nsmallest() - that do exactly what you want

import heapq


# simple list of numbers
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

# data list with more complicated data structures

portfolie = [
  {'name': 'IBM', 'share': 100, 'price': 91.1},
  {'name': 'AAPL', 'share': 50, 'price': 543.22},
  {'name': 'FB', 'share': 200, 'price': 21.09},
  {'name': 'HBQ', 'share': 35, 'price': 31.75},
  {'name': 'YHOO', 'share': 45, 'price': 16.35},
  {'name': 'ACME', 'share': 75, 'price': 115.65},
]

cheap = heapq.nsmallest(3, portfolie, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolie, key=lambda s: s['price'])

print(cheap)
print(expensive)