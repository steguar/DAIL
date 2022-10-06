# problem 1
s = input('insert a string: ')
x = int(input('insert a positive integer less than '+str(len(s))+': '))
print(s[x],s[-x])

# problem 2
s = input('insert a string: ')
x = int(input('insert a positive integer less than '+str(len(s))+': '))
print(s[x:len(s)-x+1])

# problem 3
n = int(input('insert an integer: '))
s = 0
for i in range(n):
    s = s+i
print(s)

# problem 4
n = int(input('insert an integer: '))
s = 0
for i in range(n):
    x = int(input("insert the "+str(i+1)+'-th integer: '))
    s = s+x
print(s)

# problem 5
x = int(input('insert an integer: '))
y = int(input('insert an integer: '))
p = 0
for i in range(y):
    p = p+x
print(p)

# problem 6
x = int(input('insert an integer: '))
p = 1
for i in range(1,x+1):
    p = p*i
print(p)

# problem 7
s = 0
while True:
    x = int(input('insert an integer: '))
    if x == 0:
        break
    s = s+x
print(s)

# problem 8
n = int(input('insert an integer: '))
m = int(input('insert an integer: '))
q = 0
r = n
while r>=m:
    r = r-m
    q += 1
print(q, r)

# problem 9
T1 = eval(input('insert a tuple: '))
n = int(input('insert an integer: '))
if n not in range(len(T1)):
    print(T1)
else:
    T2 = T1[:n]+(-T1[n],)+T1[n+1:]
    print(T2)



