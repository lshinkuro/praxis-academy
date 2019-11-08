squares = []
for x in range(11):
    squares.append(x**2) # bilangan x dipangkatan 2 kemudian diulangi hingga 10 kali
    squares.append(x/2) # variabel x dibagi 2

print(squares)

x=0
squares = [x**2 for x in range(10)] #hampir sama sesuatu yang ada di atas
print ("e2",squares)

combs = []
for x in [1,2,3]:
    for y in [3,1,4,6,7]:
        if x != y:
            combs.append((x, y)) #untuk setiap x  dirange 1,2,3 dan untuk setiap y di 3,1,4 apabila x tidak sama dengan y maka di append jadi x,y

print(combs)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
vec=[x*2 for x in vec]
print(vec)

# filter the list to exclude negative numbers
vec =[x for x in vec if x >= 0]

# apply a function to all the elements
vec=[abs(x) for x in vec]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit =[weapon.strip() for weapon in freshfruit]
print(freshfruit)
# create a list of 2-tuples like (number, square)
x=[2,6,7,5,4,3]
vec=[(i, i**2) for i in x]
print("9",vec)
# the tuple must be parenthesized, otherwise an error is raised
vec=[(x, x**2,x*2) for x in range(6)]
print(vec)



# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
vec =[num for elem in vec for num in elem]
print(vec)