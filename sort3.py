#Sort 3 numbers into an ascending order

number = input("Please enter 3 numbers: ")
number = list(number)

a = int(number[0])
b = int(number[1])
c = int(number[2])

x = min(a, b, c) 
z = max(a, b, c)
y = (a + b + c) - (x + z)

print(a, b, c)
print(x, y, z)
