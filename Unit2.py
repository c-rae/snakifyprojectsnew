#Last Digit of Integer
a = int(input())
print(a % 10)

#Tens Digit
n = int(input())
print((n // 10)%10)

#Sums of Digits
a = int(input())
aa = a % 10
bb = (a // 10) % 10
cc = (a // 100) % 10

b = aa + bb + cc
print(b)

#Fractional Part
from math import floor 
o = float(input())
w = floor(o)
f = o - w
print(f)

#First digit after decimal point
from math import floor
o = float(input())
w = floor(o)
f = o - w
a = (f * 10) // 1
print(a)

#Car Route
from math import ceil
n = float(input())
m = float(input())

print(ceil(m / n))

#Digital Clock
n = int(input())
hours = n // 60
minutes = n % 60
print(hours, minutes)

#Total Cost
a = int(input())
b = int(input())
n = int(input())
cost = n * (100 * a + b)
print(cost // 100, cost % 100)

#Clock Face - 1
h = int(input())
m = int(input())
s = int(input()) 
print(h * 30 + m * 30 / 60 + s * 30 / 3600)

#Clock Face - 2
alpha = float(input())
print(alpha % 30 * 12)