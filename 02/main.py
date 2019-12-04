import csv
with open("input.txt", 'r') as f:
    reader = csv.reader(f)
    program = list(reader)[0]
for i in range(len(program)):
    program[i] = int(program[i])

noun = 0
verb = -1
while program[0] != 19690720:
    #reset program
    with open("input.txt", 'r') as f:
        reader = csv.reader(f)
        program = list(reader)[0]
    for i in range(len(program)):
        program[i] = int(program[i])

    #Change input values
    if verb < 99:
        verb += 1
    else:
        noun += 1
        verb = 0
    program[1] = noun
    program[2] = verb
    
    currentPos = 0
    while program[currentPos] != 99:
        opcode = program[currentPos]
        if opcode == 1:
            program[program[currentPos+3]] = program[program[currentPos+1]] + program[program[currentPos+2]]
        elif opcode == 2:
            program[program[currentPos+3]] = program[program[currentPos+1]] * program[program[currentPos+2]]
        currentPos += 4

print(100 * noun + verb)
