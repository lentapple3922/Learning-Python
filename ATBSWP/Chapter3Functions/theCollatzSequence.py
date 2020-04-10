def collatz(number):
    intNumber = int(number)
    if intNumber % 2 == 0:  # Checks if number is evan
        intNumber = intNumber/2
        return intNumber
    elif intNumber % 2 == 1:
        intNumber = 3 * intNumber + 1
        return intNumber

print('Type a number: ', end='')  # Asks for user input to run in collatz
userInput = int(input())
while userInput > 1:
    print(collatz(userInput))
    userInput = collatz(userInput)
