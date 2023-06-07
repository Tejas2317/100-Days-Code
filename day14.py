#day14Write a program to reverse a given number
def rev(n):
    s=0
    while n!=0:
        c=n%10
        s=(s*10)+c
        n=n//10
    return s
n=int(input())
print(rev(n))
    
    