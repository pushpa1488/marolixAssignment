# Write a Python program that takes an integer as input and prints "Even" if it's an even number and "Odd" if it's an odd number

Num=int(input("Enter the number = "))
if Num%2==0:
    print("Even number")
else:
    print("Odd number")

#-----------------------------------------------------------------------------------------------------

# Create a Python program that asks the user for their age. If the age is less than 18, it should print Create a Python program that asks the user for their age. If the age is less than 18, it should print "You are a minor." If the age is between 18 and 65, it should print "You are an adult." If the age is 65 or older, it should print "You are a senior citizen." If the age is between 18 and 65, it should print "You are an adult." If the age is 65 or older, it should print "You are a senior citizen."

Age=int(input("Enter the person age = "))
if Age<18:
    print("You are a minor")
elif Age>=18 and Age<=65:
    print("You are an adult")
else:
    print("You are a senior citizen")    

#----------------------------------------------------------------------------------------------------

#Write a Python program that takes a number as input and prints "Positive" if it's greater than zero, "Negative" if it's less than zero, and "Zero" if it's equal to zero.

Num=int(input("Enter the number = "))
if Num>0:
    print("Positive")
elif Num==0:
    print("Zero")
else:
    print("Negative")

#----------------------------------------------------------------------------------------------------

# Create a Python program that asks the user for their exam score (0-100) and prints "A" if the score is 90 or above, "B" if it's between 80 and 89, "C" if it's between 70 and 79, "D" if it's between 60 and 69, and "F" if it's below 60.

Score=int(input("Enter the student score = "))
if Score>=90:
    print("A")
elif Score>=80 and Score<=89:
    print("B")
elif Score>=70 and Score<=79:
    print("C")
elif Score>=60 and Score<=69:
    print("D")
else:
    print("F")

#--------------------------------------------------------------------------------------------------

# Write a Python program that asks the user for their password. If the password is "password123," print "Access granted." Otherwise, print "Access denied."

Password=input("Enter the password = ")
if Password =="password123,":
    print("Access granted")
else:
    print("Access denied")

#----------------------------------------------------------------------------------------------------

#Create a Python program that checks if a given year is a leap year. If the year is divisible by 4 but not divisible by 100, or it's divisible by 400, it's a leap year. Otherwise, it's not.

Year=int(input("Enter the Year = "))
if ((Year%400==0 or Year%100!=0)) and (Year%400==0):
    print("Its a leap year")
else:
    print("Not a leap year")

#-------------------------------------------------------------------------------------------------
#Write a Python program that converts a temperature from Celsius to Fahrenheit or vice versa. Ask the user for the input temperature and a choice of conversion. If the choice is "C to F," convert to Fahrenheit, and if it's "F to C," convert to Celsius.

print("Choice of conversion")
print('''1.C to F\n2.F to C''')
Temp=float(input("Enter the choise of temperature = "))
while True:
    if Temp==1:
        C=float(input('Enter the Celsius = '))
        F=(C*9/5)+32
        print("Celsius converted to Fahrenheit",F,'f')
        break
    else :
        if Temp==2:
            F=float(input('Enter the Fahrenheit = '))
            C=(Temp-32)/1.8
            print("Fahrenheit converted to Celsius",C,'c')
            break  

#-----------------------------------------------------------------------------------------------------------------------------------------
#Implement a simple menu-driven program in Python. Ask the user to choose an option from a menu (e.g., 1 for "Calculate Area," 2 for "Calculate Perimeter," 3 for "Exit"). Depending on their choice, perform the corresponding action or exit the program.

print("*********************************")
print("           MENU                  ")
print("*********************************")
print('''1.Calculate Area of circle
2.Perimeter of circle
3.Exit''')
import math
while True:
    User=int(input("Choose an option from a menu\n"))
    if User==1:
        r=int(input("Enter the radius = "))
        AreaCircle=math.pi*r*r
        print("Area of circle:",AreaCircle)
        break
    elif User==2: 
        r=int(input("Enter the radius = "))
        PerimeterCircle=2*math.pi*r
        print("Perimeter of circle:",PerimeterCircle)
        break
    else:
        if User==3:
            print("Exit")
            

#----------------------------------------------------------------------------------------------------------------------------
#Create a Python program that categorizes people into age groups based on the following criteria:
# 0-12 years: Child
# 13-19 years: Teenager
# 20-59 years: Adult
# 60+ years: Senior Ask the user for their age and print their age group.

Age=int(input('Enter the age of person = '))
while True:
    if Age>=0 and Age<=12:
        print("Child")
        break
    elif Age>=13 and Age<=19:
        print("Teenager")
        break
    elif Age>=20 and Age<=59:
        print("Adult")
        break
    else:
        if Age>=60:
            print("Senior")
            break 


