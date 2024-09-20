def yes():
    yes = True
def no():
    no = True
a = int(input("First value: "))
a = int(a)
b = int(input("Second value: "))
b = int(b)
c = input("Addition?: ")
if c == "yes":
    print(a+b)
if c == "no":
    d = input("Subtraction?: ")
if d == "yes":
    print(a-b)
    e = input("Multiplication?: ")
if e == "yes":
    print(a*b)
f = input("Division: ")
if f == "yes":
    z = print(a/b)
g = input("Make the second value an exponent?: ")
if g == "yes":
    print(a**b)
h = input("Floor Division?: ")
if h == "yes":
    print(a//b)
i = input("Modulo: ")
if i == "yes":
    print(a % b)
j = input("round?: ")
if j == "yes": 
    print(round(z))