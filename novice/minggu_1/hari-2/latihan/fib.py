def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    
    while a < n:
        print(b)
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fib(6))
print(fib2(6))