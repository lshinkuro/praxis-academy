

class Vector():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return 'Vector (%d ,%d)'%(self.a,self.b)

    def __add__(self,other):
        return Vector(self.a + other.a,self.b + other.b)

v1=Vector(6,7)
v2=Vector(5,6)
v3=Vector(4,3)
print(v1 + v2 + v3)