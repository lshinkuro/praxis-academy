# class Animal :
#  def __init__(self,name,category,limbs,bulu):
#    self.name=name
#    self.limbs=limbs
#    self.category=category
#    self.bulu=bulu


# animal= Animal("dog","hewan",4,"rambut")
# print("A",animal.name,"is a",animal.category,".")
# print("it has",animal.limbs,"limbs","juga punya",animal.bulu)

# combs = []
# for x in [1,2,3]:
#     for y in [3,9,0,1,4]:
#         if x != y:
#             combs.append((x,y))

# print(combs)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12,7],
]
transposed = []
for i in range(2):
    transposed.append([row[i] for row in matrix])

print(transposed)

# dragonball_super_character = ["Son Goku", "Vegeta", "Beerus", "Trunks", "Whiz", "Champa"]
# for character in dragonball_super_character:
#     print (character)

# bil1=int(input("masukan angka:"))
# bil2=int(input("masukan angka2:"))
# c=bil1+bil2
# print(c/2)

# x, y, z = [int(x) for x in input().split()]

# num=int(input("masukin bilangan"))
# if num >1:
#     for i in range(2,num):
#         if (num %i)==0:
#             print(num,"num bukan bilangan prima")
#             print(i,"kali",num/i,"=",num)
#             break
#         else:
#             print(num,"adalah bilangan prima")
# else:
#     print(num,"bukan bilangan prima")

# num =int(input("masukan bilangan"))
# if num >1 :
#     for i in range(2,num):
#         if(num %i)==0:
#             print(num,"num bukan bilangan prima")
#             print(i ,"kali",num/i,"=",num)
#             break
#         else:
#             print("num adalah bilangan prima")
# else:
#     print("num bukan bilangan prima")

n =int(input("masukan row yang lu pengen"))
i,j=0,0
for i in range(0,n):
    print(i)
    for j in range(0,i+1):
        print("*",end="")

# batas =5
# i,j=0,0
# for i in range(1,batas):
#     print()
#     for j in range(1,batas+1):
#         print("+",end="")
