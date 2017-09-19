# Kyle Sherman
# 9/19/2017

A2B = {} # new instance of a dictionary
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

train(A2B)
display(A2B)
