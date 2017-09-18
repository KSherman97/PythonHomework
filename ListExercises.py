def sigma(a):
    n = 0
    for x in a:
        n += x
    return n

a = [1, 2, 3]

print("Sum of the list(a): ", sigma(a))
print()

########################################

def chop(b):
    if(len(b) > 1):
        del b[0]
        del b[-1]
    else:
        b = []
    return b

b = [1, 2, 3, 4, 5, 6, 7]
print(b, "original")
while len(b) > 0:
    b = chop(b)
    if(len(b) > 0):
        print(b , "chop!")
    else:
        print(b, "List is empty!")
