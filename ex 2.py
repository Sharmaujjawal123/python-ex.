'''Your task is to :

Take two single characters in variables a and b as input from the user.
Find the order of both the characters in a and b, and store them in another variables c and d respectively.
Perform the Bit-wise operations (&, |, ~, ^) on c and d (In the given sequence).
Print to the console, the result of every bit-wise operation (For printing the results please refer the visible sample test case).


Editorial:

Order means Unicode code value.
For example Unicode value of 'A' is 65 and 'a' is 97.
You can use ord() function to find the order of a and b.'''

# Write your code here
a= input()
b =input()
c =ord(a)
d= ord(b)
print("c&d=",c&d)
print("c|d=",c|d)
print("~c=",~c)
print("c^d=",c^d)

