
'''Take two integers a and b as input from the user.
Compute the expression (a + b)2 >=(a2 + b2), and print the result on the console.
Compute the expression (a - b)2 - 3*a*b, and print the result on the console.'''

# Write your code
a =int(input("a: "))
b = int(input("b: "))
print((a+b)**2>=(a**2+b**2))
print((a-b)**2-3*a*b)

