# membuat fungsi rata-rata
import math
def rata_rata(*data):
    banyak_data = len(data)
    jumlah_data = sum(data)
    nilai_rata_rata = float(jumlah_data) / float(banyak_data)
    return nilai_rata_rata

a=rata_rata(8,9,7,6,7,8,9,8,6)
print(math.floor(a))

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