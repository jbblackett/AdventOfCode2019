f = open("C:\\Users\\jacob\\OneDrive\\Python\\AdventOfCode\\03\\input.txt",'r').readlines()
wireAinstructions = f[0][:-1].split(',')
wireBinstructions = f[1][:-1].split(',')

def move(direction, steps, x1, y1):
    x = x1
    y = y1
    additionalCoords = []
    if direction == 'U':
        for i in range(steps):
            y = y + 1
            additionalCoords.append((x,y))
    elif direction == 'D':
        for i in range(steps):
            y = y - 1
            additionalCoords.append((x,y))
    elif direction == 'R':
        for i in range(steps):
            x = x + 1
            additionalCoords.append((x,y))
    elif direction == 'L':
        for i in range(steps):
            x = x - 1
            additionalCoords.append((x,y))
    return [(x,y), additionalCoords]

coordsA = []
coordsB = []
y = 0
x = 0
#Track A path
for instruction in wireAinstructions:
    direction = instruction[0]
    steps = int(instruction[1:])
    result = move(direction, steps, x, y)
    x = result[0][0]
    y = result[0][1]
    for coord in result[1]:
        coordsA.append(coord)

#Track B path
y = 0
x = 0
for instruction in wireBinstructions:
    direction = instruction[0]
    steps = int(instruction[1:])
    result = move(direction, steps, x, y)
    x = result[0][0]
    y = result[0][1]
    for coord in result[1]:
        coordsB.append(coord)

#Find matching coordinates (intersections)
coordsMatch = set(coordsA) & set(coordsB)

#find closest intersect to (0,0)
#closest = 9999999
#for intersect in coordsMatch:
#    x1 = 0
#    y1 = 0
#    x2 = intersect[0]
#    y2 = intersect[1]

#    dist = abs(x1 - x2) + abs(y1 - y2)
#    if dist < closest:
#        closest = dist

#find intersect with least combined steps
combined = 9999999
for intersect in coordsMatch:
    stepsA = coordsA.index(intersect) + 1
    stepsB = coordsB.index(intersect) + 1
    if stepsA + stepsB < combined:
        combined = stepsA + stepsB
    

print(combined)
