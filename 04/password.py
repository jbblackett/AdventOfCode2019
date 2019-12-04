def checkDouble(x):
    for i in range(5):
        if str(x)[i] == str(x)[i+1] and str(x).count(str(x)[i]) <= 2:
            return True
    return False

def checkIncreasing(x):
    sort = "".join(sorted(str(x)))
    if str(x) == sort:
        return True
    return False

lowerLimit = 254032
upperLimit = 789860

possiblePasswords = []
for i in range(lowerLimit, upperLimit+1):
    if checkDouble(i) and checkIncreasing(i):
        possiblePasswords.append(i)

print(len(possiblePasswords))
