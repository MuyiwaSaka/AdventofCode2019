import math

def interprete_intcode(fg):
    machine = fg.split(",")
    ptr = 0
    running = 1
    while running > 0:
        chk = int(machine[ptr])
        if chk == 1:
            machine[int(machine[ptr + 3])] = str(int(machine[int(machine[ptr + 1])]) + int(machine[int(machine[ptr + 2])]))
        elif chk == 2:
            machine[int(machine[ptr + 3])] = str(int(machine[int(machine[ptr + 1])]) * int(machine[int(machine[ptr + 2])]))
        elif chk == 99:
            running = 0
        else:
            running = 0
        ptr = ptr + 4
    return machine


# Test The Machine using prior test data
interprete_intcode("1,0,0,0,99") # validated
interprete_intcode("2,3,0,3,99") # validated
interprete_intcode("2,4,4,5,99,0") # validated
interprete_intcode("1,1,1,4,99,5,6,0,99") # validated

def generate_output(noun,verb):
    h = open("day2input.txt","r")
    f = h.read()
    lst = f.split(",")
    lst[1], lst[2] = str(noun), str(verb)
    feed = ",".join([str(x) for x in lst])
    output = interprete_intcode(feed)
    return output

print("First Star Code")
print(generate_output(12, 2))

print("Second Star Code")
results = {"Noun":0, "Verb":0}
for x in range(99):
    for y in range (99):
        output = generate_output(x,y)
        v=  int(output[0])
        if v == 19690720:
            results["Noun"],results["Verb"] = x, y
            break
        else:
            continue
        break

finalvar = 100 * results["Noun"] + results["Verb"]
print(finalvar)