# Sets

#includes a data type for sets
#Curly braces or the set() function can be used to create sets

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)


# show that duplicates have been removed
>>> 'orange' in  		# fast membership testing
True
>>> 'kiwi' in basket
False


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a 							# unique letters in a
a - b 						# letters in a but not in b
a | b 						# letters in a or b or both
a & b 						# letters in both a and b
a ^ b 						# letters in a or b but not both


----------------------------------------------------------------------------

fruits = {"apple", "banana" , "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)


fruits.add("cucumber")
fruits
fruits.update("grape", "water malon") 	# input as seperated single words
fruits
fruits.removed("banana")
fruits
fruits.discard("kiwi")
fruits





>>>Dictionaries

#Dictionaries

#Another Useful data type built into Python is the disctionary

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel


del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'sape' not in tel


dict([('sape',4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}

{x: x**2 for x in (2, 4, 6)}
{x: x**3 for x in (1, 2, 3, 4, 5)}


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items();
	print(k, v)

	# Create index for value
for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)


questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}? It is {1}.'.format(q, a))
	
