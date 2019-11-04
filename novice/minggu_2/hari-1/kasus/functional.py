def greeting():
  print("hello world")
# Invoking the function
greeting()
# prints 'Hello World'

def square(a):
    return a*a

print (square(5))   #print 25 

def formalGreeting():
    print("How are you?")
def casualGreeting(): 
    print("What's up?")
def greet(type, greetFormal, greetCasual):
    if(type == 'formal'):
        greetFormal()
    elif(type == 'casual'):
        greetCasual()
  
# prints 'What's up?'

greet('casual', formalGreeting, casualGreeting)


arr1 = [1, 2, 3,4,5,6,7]
arr2 = []
for i in range(0,len(arr1)):
    arr2.append(arr1[i] * 2)
    i =i+1
# prints [ 2, 4, 6 ]
print(arr2)


def hitung(n):
  return  n*2

arr_1 = [1, 2, 3]
arr_2 = map(hitung,arr_1)

print(list(arr_2))

birthYear = [1975, 1997, 2002, 1995, 1985]
ages = []
for i in range (0,len(birthYear)):
    age = 2018 - birthYear[i]
    ages.append(age)
    i += 1
#  prints [ 43, 21, 16, 23, 33 ]
print("umur nya " ,ages)

persons = [
  { "name": 'Peter', "age": 16 },
  { "name": 'Mark', "age": 18 },
  { "name": 'John', "age": 27 },
  { "name": 'Jane', "age": 14 },
  { "name": 'Tony', "age": 24},
]
fullAge = []
for i in range(0,len(persons)):
    if persons[i]["age"] >= 18:
        fullAge.append(persons[i])
        i += 1

print(fullAge)

import functools

arr = [5, 7, 1, 8, 4]
sum = functools.reduce(lambda a,b : a+b,arr)
max = functools.reduce (lambda a,b : a if a > b else b,arr)
# // prints 25
print(sum)
print (max)

lis = [5, 7, 1, 8, 4]
jumlah = 0
for i in range (0,len(lis)):
    jumlah =jumlah + arr[i]
    i += 1
# prints 25
print ("jumlah nya : " ,jumlah)


strArray = ['JavaScript', 'Python', 'PHP', 'Java', 'C']

def mapForEach(arr,fn):
    newArray = []
    for i in range(0,len(strArray)):
        newArray.append(fn(arr[i]))
        i += 1
    return newArray

lenArray = mapForEach(strArray,len)

# // prints [ 10, 6, 3, 4, 1 ]
print(lenArray)