# 01.01 Unpackage a Sequence info Separate Variables

# Problem:
# You have an N-element tuple or sequence that you would like to 
# unpack into a collection of N variables.

# Solution:
# Any sequence (or iterable) can be unpacked into variables 
# using a simple assignment operation.
# The only requirement is that the number of variables and structure match the sequence.

# sample data
p = (4, 5, )
s = 'Hello'
data = [
  'ACME',
  50,
  91.1,
  (2012, 12, 21),
]

# ex01)
print('\n ex01)')
x, y = p
print(x)
print(y)

# ex02)
print('\n ex02)')
name, shares, price, date = data
print(name)
print(date)

# ex03)
print('\n ex03)')
name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon) 
print(day)

# ex04) - error example
print('\n ex04) - error example')
try:
  x, y, z = p
  print(x)
  print(y)
  print(z)
except Exception as e:
  print("%s: %s" % (e.__class__.__name__, e.message))

# ex05)
print('\n ex05)')
a, b, c, e, d = s
print(a)
print(b)
print(c)

# ex06)
print('\n ex06)')
_, shares, price, _ = data
print(shares)
print(price)