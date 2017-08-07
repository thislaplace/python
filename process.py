#!/usr/bin/python 
#coding=utf-8

num = 9
if num >= 0 and num <= 10:
    print '0<=num<=10'
else:
    print 'hehe'

print '-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-'

numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []

while len(numbers) > 0:
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

print numbers
print even
print odd
print '-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-'

for letter in 'Python':
    print letter
print '-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-'

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print fruits[index]
print '-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-'

for num in range(10, 20):
    for i in range(2, num):
        if num%i == 0:
            j=num/i
            print '%d = %d x %d' % (num, i, j)
            break
    else:
        print num, 'is a prime'
print '-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-'


i = 2
while i < 100:
    j = 2
    while(j <= i/2):
        if not(i%j):break
        j = j + 1
    if(j > i/2):print i,'is prime'
    i = i + 1

