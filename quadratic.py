import cmath

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

d = (b**2) - (4*a*c)

print("decriminant = ", d)

x1 = ((-b) + cmath.sqrt(d))/(2*a)
x2 = ((-b) - cmath.sqrt(d))/(2*a)

print("x1 = ", x1)
print("x2 = ", x2)
