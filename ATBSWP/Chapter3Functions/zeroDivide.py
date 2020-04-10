def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


#could also be written line this

#def spam(divideBy):
    #return 42/divideBy


#try:                  This way it will only print to line 23 and skip over line 24
    #print(spam(2))    because line 23 causes an error and it will skip to the exept statment
    #print(spam(12))
    #print(spam(0))
    #print(spam(1))
#exept ZeroDivisionError:
    #print('Error: Invalid Argument')