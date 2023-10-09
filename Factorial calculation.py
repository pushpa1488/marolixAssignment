#Factorial Calculation:
# Implement a Python program that calculates and prints the factorial of a given number using a for loop.
Num=int(input("Enter the number = "))
fact=1
if Num<0:
       print("Factorial does not exit")
else:
    for i in range(1,Num+1):
        fact=fact*i
    print("Factorial of a num is",fact)
    


        
