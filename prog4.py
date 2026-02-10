#1RUA25BCA0011 ASWATHEE S
def fib(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        a=b
        b=a+b
n=int(input("enter number "))
fib(n)
