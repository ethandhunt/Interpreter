import time

def Tokenise(string):
    return string.split(">")


def run(ins):
    global pointer
    global instruction
    pointer = pointer
    instruction = instruction
    ins + ""
    instruction += 1
    if ins == "":
        print(f"{instruction}: {ins} {pointer}")
        return

    # Pointer shifting
    if ins[0] == "+":
        for thing in ins[1:].split("+"):
            pointer += 1
            try:
                errorQuery = mem[pointer]
            except:
                mem[pointer] = 0
    if ins[0] == "-":
        for thing in ins[1:].split("-"):
            pointer -= 1
            try:
                errorQuery = mem[pointer]
            except:
                mem[pointer] = 0
    

    # Goto Functionality
    if ins[0] == "!":
        instruction = int(ins[1:])
    
    # Reading memory into RAA
    if ins[0] == "*":
        RAA[ins[1:]] = mem[pointer]

    # Moving pointer using integer constants
    if ins[0] == "@":
        pointer = int(ins[1:])
    
    # Changing memory values with integer constants
    if ins[0] == "$":
        mem[pointer] = int(ins[1:])
    
    # Incrementing memory values with integer constants
    if ins[0] == "i":
        mem[pointer] += int(ins[1:])
    
    # Adding delays in microseconds
    if ins[0] == "#":
        time.sleep(int(ins[1:]) / 100)

    # Ending
    print(f"{instruction}: {ins} {pointer}: {mem[pointer]}")


string = input("Enter Code: ")
list = Tokenise(string)
pointer = 0
instruction = 0
mem = {}
RAA = {}
while instruction < len(list):
    run(list[instruction])
    print(mem)
