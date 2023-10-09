#Write a Python function to calculate the factorial of a non-negative integer.
def factorial():
    if num<0:
        print("Factorial does not exit")
    else:
        fact=1
        i=1
        while i<=num:
            fact=fact*i
            num=num+1
            i=i=1
        print(fact)  

num=int(input("Enter the number = "))
factorial() 



# Write a function that checks if a given number is prime. 

# def prime(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             print("not prime number")
#             break
#     else:
#         print("prime number")        
    
# n=int(input("Enter the number = "))
# prime(n)   

# Create a function that takes a list of numbers as input and prints the sum of all the numbers in the list.
# def sum_num():
#     sum=0
#     for i in (sumnum):
#         sum=sum+int(i)
#     print(sum)

# sumnum=list(map(int,input("Enter the integer = ").split()))
# sum_num()

# def sum_num():
#     sum=0
#     for i in range(len(sumnum)):
#         sum+=sumnum[i]      
#     print(sum)
# sumnum=list(map(int,input("Enter the integer = ").split()))
# sum_num()

# Write a Python function to find the maximum number in a list of numbers.

# def FindMaxNum(Max_Num):
#     Maximum=Max_Num[0]
#     for i in (Max_Num):       
#         if i>Maximum:
#             Maximum=i
#     print("Maximum number = ",Maximum)
# Max_Num=list(map(int,input("Enter the integer = ").split()))
# FindMaxNum(Max_Num) 

