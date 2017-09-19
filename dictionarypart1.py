# Kyle Sherman
# 9/19/2017

A2B = {} # new instance of a dictionary
def mainMenu():
    validInput = False
    print("Dictionary Program by Kyle Sherman")
    print("1) Train Words")
    print("2) Display Words")
    print("3) Quit")
    action = input("What to do? ")
    while validInput == False:
        try:
            action = int(action)
            if(action == 1):
                train(A2B)
                validInput = True
            elif(action == 2):
                display(A2B)
                validInput = True
            elif(action == 3):
                exit()
                break
            else:
                print("That's not an option")
        except ValueError:
            print("That's not an option")

def display (d):
    print()
    for k, v in d.items():
        print(k , "<->" , v)
    
def train(d):
        running = True
        while(running):
            LanguageA = input("Enter a word in English: ")
            if(LanguageA == ""):
                running = False
                break
            else:
                LanguageB = input("Enter the translation: ")
                A2B[LanguageA] = LanguageB

doExit = False
while doExit == False:
    mainMenu()
