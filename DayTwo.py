import math

def interprete_intcode(fg):
    print("Input: {}".format(fg))
    machine = fg.split(",")
    pstate = 0
    running = 1
    while running > 0:
        chk = int(machine[pstate])
        if chk == 1:
            machine[int(machine[pstate+3])] = int(machine[int(machine[pstate+1])]) + int(machine[int(machine[pstate+2])])
        elif chk == 2:
            machine[int(machine[pstate+3])] = int(machine[int(machine[pstate+1])]) * int(machine[int(machine[pstate+2])])
        elif chk == 99 :
            running = 0
        else:
            running = 0
        pstate = pstate + 4
    print machine

#Test The Machine using prior test data
interprete_intcode("1,0,0,0,99") # validated
interprete_intcode("2,3,0,3,99") # validated
interprete_intcode("2,4,4,5,99,0") # validated
interprete_intcode("1,1,1,4,99,5,6,0,99") # validated

print("RUNNING MAIN CODE")
h= open("day2input.txt","r")
f= h.read()
brkdwn = f.split(",")
brkdwn[1]="12"
brkdwn[2]="2"
feed = ",".join([str(x) for x in brkdwn])

interprete_intcode(feed)
