n = int(input("Specif the n:"))
sum_even = 0
sum_odd = 0

for i in range (n+1):
    if (i%2 == 0):
        print("Even number :", i)
    if (i%2 == 1):
        print("Odd number :", i)

#Sum of Even and Odd integer in N
for i in range (n+1):
    if (i%2 == 1):
        sum_even = sum_even + i

for i in range (n+1):
    if (i%2 == 0):
        sum_odd = sum_odd + i
        
print("Sum Even =", sum_even)
print("Sum Odd =", sum_odd)

