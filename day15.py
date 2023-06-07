#day15 strong number
n=int(input())
fact=1
s=0
v=n
if n==0:
    s=s+fact
else:
    while v!=0:
        fact=1
        c=v%10
        for i in range(1,c+1):
            fact=fact*i
        s=s+fact
        v=v//10
if s==n:
    print("strong number")
else:
    print("not")
        