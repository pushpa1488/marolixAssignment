#Write a Python program that calculates and prints the sum of all the even numbers from 1 to 50 using a for loop.
Num=50
result=0
for i in range(1,Num+1):
    # print(i)
    if i%2==0:
        result+=i
print(result)