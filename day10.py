# day 10 Write a program to find Factorial of a number
def fact(n):
    if n<=0:
        print("invalid number")
    if n==0:
        return 1
    else:
        return n*(n-1)
n=int(input())
print(fact(n))