import math
modules = []

f = open('input.txt', mode='r')
for line in f.readlines():
    modules.append(int(line[:-1]))

fuelCount = 0
for module in modules:
    fuel = math.floor(module / 3) - 2
    fuelCount += fuel

    fuelFuel = math.floor(fuel / 3) - 2
    while fuelFuel >=0:
        fuelCount += fuelFuel
        fuelFuel = math.floor(fuelFuel / 3) - 2

print(fuelCount)
