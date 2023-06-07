#day13 sum of n numbers
def s(n):
    sum=0
    i=0
    while i<n+1:
    #for i in range(0,n+1):
        sum=sum+i
        i=i+1
    return sum   
n=int(input())
print(s(n))
