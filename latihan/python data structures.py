buah = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
buah.count('apple')

buah.count('tangerine')  #Return the number of times x appears in the list.

print(buah.index('banana'))

buah.index('banana', 4)  # Find next banana starting a position 4

buah.reverse()
print(buah)

buah.append('grape') #Add an item to the end of the list. Equivalent to a[len(a):] = [x].
print(buah)

buah.sort() #Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
print(buah)

buah.pop()
print(buah)