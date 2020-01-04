#Tuple

Tuple - ()

t = 12345, 54321, 'hello!'
t[0]


# Turple may be nested:
 u = t, (1, 2, 3, 4, 5)
 u[1][2]
3
 u[0][0]
12345


# Tuples are immutable:
 t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


# but they can contain mutable objects:
 v = ([1, 2, 3], [3, 2, 1])
 v

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


# change Tuples Value
 x = ("apple", "banana", "cherry", "orange")
 y = list(x)
 y[1]
'banana'
 y[1] = "mango"
 y
['apple', 'mango', 'cherry', 'orange']
 x = tuple(y)
 x
('apple', 'mango', 'cherry', 'orange')


 f = list(fruits)
 f[4] = "pineapple"
 fruits = tuple(f)
 fruits
('apple', 'banana', 'cherry', 'orange', 'pineapple', 'melon', 'mango')