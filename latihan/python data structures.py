fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits.count('tangerine')  #Return the number of times x appears in the list.

fruits.index('banana')

fruits.index('banana', 4)  # Find next banana starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape') #Add an item to the end of the list. Equivalent to a[len(a):] = [x].
print(fruits)

fruits.sort() #Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
print(fruits)

fruits.pop()
print(fruits)