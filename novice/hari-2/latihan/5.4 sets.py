basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

print('orange' in basket)                 # fast membership testing

print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
a                                  # munculin string a

print(a - b)                              # char ada di a tapi ga ada di b

print(a | b)                              # munculin semua karakter yang ada di keduanya
print(a & b)                              # munculin karakter yang di pake di keduanya

print(a ^ b )                             # munculin karakter selain yang ada di keduaya