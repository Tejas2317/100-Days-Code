# Day 9 Write a program to find Number of digits in an integer
n = int(input())
count = 0
c = n

while c != 0:
    c = c // 10
    count += 1

print(count)
