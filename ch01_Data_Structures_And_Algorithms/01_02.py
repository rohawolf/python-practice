# 01.02 Unpacking Elements from Iterables of Arbitrary Length

# Problem
# You need to unpack N elements from an iterable, 
# but the iterable may be longer than N elements, 
# causing a 'too many values to unpack' exception.

# Solution
# Python 'star expressions' can be used to address this problem. 

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
records = [
  ('foo', 1, 2),
  ('bar', 'hello'),
  ('foo', 3, 4),
]
data = (
  'ACME',
  50,
  123.45,
  (12, 18, 2012),
)

line = 'nobody:8:-2;-2:Unprivileged User:/var/empty:/usr/bin/false'
items = [1, 10, 7, 4, 5, 9]


name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

records = [
  ('foo', 1, 2),
  ('bar', 'hello'),
  ('foo', 3, 4),
]

def do_foo(x, y):
  print('foo', x, y)

def do_bar(s):
  print('bar', s)

def sum(items):
  head, *tail = items
  return head + sum(tail) if tail else head

for tag, *args in records:
  if tag == 'foo':
    do_foo(*args)
  elif tag == 'bar':
    do_bar(*args)

uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

name, *_, (*_, year) = data
print(name)
print(year)

res = sum(items)
print(res)