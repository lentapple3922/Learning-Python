import sys
print('Type q to quit')
while True:
    print('Enter a number:')
    spam = input()
    if spam == 1:
        print('Hello')
    elif spam == 2:
        print('Howdy')
    elif spam == 'q':
        sys.exit()
    else:
        print('Greetings!')