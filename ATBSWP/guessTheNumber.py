#This is a guess the number game
import random
secretNumber = random.randint(1,20)
print('I am thinking of a random number between 1 and 20.')

#Ask the play to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is to low')
        print('You have guessed ' + str(guessesTaken) + ' out of 6 guesses') #added this to program to let user know how many guesses they have left
    elif guess > secretNumber:
        print('Your guess is to high')
        print('You have guessed ' + str(guessesTaken) + ' out of 6 guesses') #added this to program to let user know how many guesses they have left
    else:
        break #This condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed my number in '+str(guessesTaken)+' guesses!')
else:
    print('Nope. The number I was thinking of was '+str(secretNumber))