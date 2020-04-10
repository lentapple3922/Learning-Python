def spam():
    global eggs
    eggs = 'Spam' #this is the global

def bacon():
    eggs = 'Bacon' #this is a local

def ham():
    print(eggs) #this is the global

eggs = 42 #this is the global

spam()
print(eggs)


def test():
    eggs = 4
    #print(eggs)
    #global eggs #causes error because it was already defined as a local variable, there for always being one
    #print(eggs)
#test()

def test2():
    print(bacon)
bacon = 43

test2()