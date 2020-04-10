import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

# I am trying to make a loop that will ask for the user input
# and run magic 8 ball game.
# I added this sepretly from the book. The book only does what
#is in the if Yes statment
while(True):
    print('Spin the 8 ball, Yes or no')
    userInput = input()
    if userInput == 'Yes' or userInput == 'yes':
        #r = random.randint(1, 9)
        #fortune = getAnswer(r)
        #print(fortune)
        print(getAnswer(random.randint(1,9))) #This line is a consolidation of the last three lines
    elif userInput == 'No' or userInput == 'no':
        break
    else:
        print('Not right input, try again')
        continue