#fibonaci 4.6

# menampilan fibonaci
def fib(n):
     a,b=0,1
     while a<n:
       print(a,end ='  \n')
       a,b=b,a+b
     print()

fib (2000)
