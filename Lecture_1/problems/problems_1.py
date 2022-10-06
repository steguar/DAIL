# problem 1
x = int(input('insert integer: '))
y = int(input('insert integer: '))
print(x+y)

# problem 2
h = int(input('insert hours: '))
m = int(input('insert minutes: '))
s = int(input('insert seconds: '))
print(3600*h+60*m+s)

# problem 3
s = input('insert a string: ')
print(' '*(20-len(s))+s)

# problem 4
x = int(input('insert an integer: '))
y = int(input('insert an integer: '))
if x<y:
    print("x is less than y")
elif x==y:
    print("x is equal to y")
else:
    print("x is greater than y")

# problem 5
expr = input('insert a valid mathematical expression: ')
x = eval(expr)
if x<0:
    print(-x)
else:
    print(x)

# problem 6
x = int(input('insert an integer: '))
y = int(input('insert an integer: '))
z = int(input('insert an integer: '))
if x>y:
    if x>z:
        print(x)
    else:
        print(z)
else:
    if y>z:
        print(y)
    else:
        print(z)

