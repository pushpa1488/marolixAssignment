# Password Verification:
# Create a Python program that asks the user to enter a password. Use a while loop to keep asking for the password until the user enters the correct password "secret123."

password=input('Enter the password = ')
correct_password='secret123'
while True:
    if correct_password!=password:
     pass_word=input("Passwords incorrect\nTry once again\n \n")
     password=pass_word
    
    else:
        print('Now you entered correct password ')
        break

