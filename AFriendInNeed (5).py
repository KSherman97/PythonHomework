################################
# Kyle Sherman                 #
# Homework #2 - Friend In Need #
# Due 9/7/2017                 #
################################

# imports and function definitions
# function passes in the money variable
# then determines if it is <, >, or = 0
# will return a result based on the decision structures
def calcMoney(money):
    money = money
    if(money == 0):
        result = ("Best wishes, " + nameString) 
    if(money > 0):
        result = ("May I borrow ${:0,.2f}".format(money / 2, 2) + ", " + nameString + "?")
    if(money < 0):
        result = ("I'm sorry, you're in debt, " + nameString)
    return result

nameString = input("What is your name? ")
print ("Hello, " + nameString)

# While loop to validate the input and only allow a number
# Accepts decimal or whole
# Try - Except is the python way of doing a try catch
# will ensure that the input allowed is valid
validInput = False
while validInput == False:
    try:
        money = float(input("How much money do you have, " + nameString + "? $"))
        validInput = True
        print(calcMoney(money))
        
    except ValueError:
        print("That is not a valid input! You must enter a number, either whole or decimal.")
        print()


