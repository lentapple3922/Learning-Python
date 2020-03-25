# Basic Username and Password Prompt
print('What is your name?')
name = input()                  #Asks for Username
print('What is your Password')
password = input()              #Asks for password
if name =='Mary':
    print('Hello, '+ name)
    if password =='swordfish':  #Checks if Password is right
        print('Access granted.')
    else:
        print('Wrong password')
else:
    print('who are you')