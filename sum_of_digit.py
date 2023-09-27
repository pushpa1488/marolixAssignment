#Implement a Python program that calculates and prints the sum of the digits of a given integer using a while loop.

Digits=int(input('Enter the sum of digits = '))
sum_digits=0
i=1
while i<=Digits:
    rem=Digits%10
    sum_digits=int(sum_digits)+int(rem)
    Digits=Digits/10
print(sum_digits)
