
'''9451 ---->he only line of input has single integer representing the number days the ship was travelling.



25 Y 10 M 26 D ------> No.of days in the year:month:day format.'''

#Type Content here...
a = int(input())
b = a//365
c = (a-b*365)//30
print(b,"Y",c,"M",a-(b*365+c*30),"D")




