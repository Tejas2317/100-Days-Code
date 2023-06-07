#day12Write a program to find Sum of digits of a number
def s(n):
    sum=0
    while n!=0:
       c=n%10
       sum=sum+c
       n=n//10
    return sum
n=int(input())
print(s(n))