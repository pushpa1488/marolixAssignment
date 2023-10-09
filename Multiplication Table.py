#Create a Python program that uses a for loop to generate and print the multiplication table for a given number. The user should input the number for which they want to see the multiplication table.
input_num=10
mult_num=int(input("Enter the multiplication number = "))
for i in range(1,input_num+1):
    result=mult_num*i
    print(mult_num,'*',i,'=',result)
