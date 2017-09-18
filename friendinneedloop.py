# Kyle Sherman
# 9/7/2017

# A freind in need (loop) -= DUE 9/12/2017 =-

# Definitions and Declarations
def Loop(moneyDecimal):
    money = moneyDecimal
    isComplete = False
    while isComplete == False:
        letBorrowString = input("Can I borrow ${:0,.2f}".format(money) + "? ")
        if(letBorrowString.lower() == "no"):
            money = (money / 2)
            if(money < 1):
                print("Never mind.")
                isComplete = True
        if(letBorrowString.lower() == "yes"):
            isComplete = True
            print("Thank you for letting me borrow ${:0,.2f}".format(money) + "!")
        else:
            print("That is not valid input")

###################################################################################

# Main program code
# isValid allows me to run the program
# until the a valid input is entered
# utilizing a try except statement
nameString = input("What is your name? ")        
isValid = False
while isValid == False:
    moneyDecimal = input("How much money do you have, " + nameString + "? $")
    try:
        moneyDecimal = float(moneyDecimal)
        isValid = True
        Loop(moneyDecimal)
    except ValueError:
        print("That is not a valid input.")
