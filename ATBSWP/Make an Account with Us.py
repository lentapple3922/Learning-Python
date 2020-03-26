#This program is to let a user log in or create an account. Can only hold two people, new user and old user
print('Do you have an account?')
account = input()
if(account=='yes'):
    print('What is your username?')
    accountName = input()
    if(accountName == 'Kailan'):
        print('What is your password')
        accountPassword = input()
        if(accountPassword == 'ksh1234'):
            print('welcome '+ accountName)
        else:
            print('Wrong Password')
    else:
        print('User does not exsist')
else:
    print('Enter new username')
    newUser = input()
    print('Enter password')
    newPassword = input()
    print('Welcome, ' + newUser)