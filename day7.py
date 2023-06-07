#Write a program to find Number of days in a given month of a given year
m = int(input('Enter the month: '))
y= int(input('Enter the year: '))
if(m>12):
  print('invalid month of year')
elif(m == 2 and (y%400 == 0) or ((y%100 != 0) and (y%4 == 0))):
 print('Number of days is 29')
elif(m == 2):
 print('Number of days is 28')
elif(m == 4 or m == 6 or m == 9 or m== 11): 
 print('Number of days is 30')
else:
 print('Number of days is 31')
    