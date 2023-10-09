# Write a Python program that takes an integer as input and uses a while loop to reverse the digits of the number. For example, if the input is 12345, the program should print 54321.

Number=int(input("Enter the digits = "))
i=0
while (0<Number):
    i=(i*10)+(Number%10)
    Number=Number//10
print(i)    
   

    