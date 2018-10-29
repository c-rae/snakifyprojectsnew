#Sum of three numbers
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#Hi John
a = input()
print("Hi " + a)

#Square
a = int(input())
print(a*a)

#Area of right angle triangle
b = int(input())
h = int(input())
print(0.5*b*h)

#Hello, Harry
name = input()
print("Hello, " + name + "!")

#Apple Sharing
n = int(input())
k = int(input())
print(k // n)
print(k % n)

#Previous and Next
a = input()
b = str(int(a) + 1)
c = str(int(a) - 1)
print("The next number for the number " + a + " is " + b)
print("The previous number for the number " + a + " is " + c)

#Two timestamps
hour1 = input()
minute1 = input()
second1 = input()
h1 = int(hour1) * 3600
m1 = int(minute1) * 60
s1 = int(second1) 
hour2 = input()
minute2 = input()
second2 = input()
h2 = int(hour2) * 3600
m2 = int(minute2) * 60
s2 = int(second2)
time1 = int(h1+m1+s1)
time2 = int(h2+m2+s2)
answer = time2-time1
print(answer)

#School Desks
a = input()
b = input()
c = input()
a1 = int(a) // 2
b1 = int(b) // 2
c1 = int(c) // 2
a2 = int(a) % 2
b2 = int(b) % 2
c2 = int(c) % 2
tde = int(a1+b1+c1+a2+b2+c2)
print(tde)