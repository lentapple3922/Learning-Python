def collatz(number):
    intNumber = int(number)
    if intNumber % 2 == 0:  # Checks if number is evan
        intNumber = intNumber/2
        return intNumber
    elif intNumber % 2 == 1:
        intNumber = 3 * intNumber + 1
        return intNumber


while True:  # Main game loop
    try:  # to check if the user inputs a string
        print('Type a number: ', end='')  # Asks for userInput to run in collatz
        userInput = int(input())

        while userInput > 1:  # Runs collatz function to get 1
            print(collatz(userInput))
            userInput = collatz(userInput)

    except ValueError:  # Deals with user typing a string
        print('Thats not a number, do you want to exit?')  # Asks user if they want to exit
        endProgram = input()
        if endProgram == 'Yes' or endProgram == 'yes':
            break  # will end program
        elif endProgram == 'No' or endProgram == 'no':
            continue  # will continue the loop
