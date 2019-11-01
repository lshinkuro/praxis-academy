import json





# some JSON:
x ={ "name":"John", "age":30, "city":"New York"}

# parse x:
y = json.dumps(x)

# the result is a Python dictionary:
print(y) 

x=json.loads(y)
print(x)

def tri_recursion(k):
      if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
      else:
        result = 0
        return result

print("\n\nRecursion Example Results")
tri_recursion(6)