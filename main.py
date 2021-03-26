import time

def Tokenise(string):
    return string.split(">")


def prnt(thing):
    if do_print:
        print(thing)


def RAAval(string):
    if string[1] == "R":
        return RAAval(string[1:])
    return RAA[string[1:]]


def value(string):
    if string[0] == "R":
        return RAAval(string)
    try:
        return int(string)
    except:
        return string

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
        instruction = value(ins[1:])
    
    # Reading memory into RAA
    if ins[0] == "*":
        RAA[value(ins[1:])] = mem[pointer]

    # Moving pointer using integer constants and RAA
    if ins[0] == "@":
        pointer = int(value(ins[1:]))
        try:
            errorQuery = mem[pointer]
        except:
            mem[pointer] = 0
    
    # Setting memory values with integer constants and RAA
    if ins[0] == "$":
        mem[pointer] = value(ins[1:])
    
    # Incrementing memory values with integer constants and RAA
    if ins[0] == "i":
        mem[pointer] += int(value(ins[1:]))
    
    # Adding delays in milliseconds(w/ RAA)
    if ins[0] == "#":
        time.sleep(value(ins[1:]) / 1000)
    
    # Conditional Jumps
    if ins[0] == "?":
        if mem[pointer] == value(ins[1:].split(':')[0]):
            instruction = value(ins[1:].split(':')[1])
    
    # Print
    if ins[0] == ".":
        print(mem[pointer])
    
    # Adding memory and RAA values into a RAA value
    if ins[0] == "%":
        if type(value(ins[1:].split(':')[0])) == int:
            RAA[ins[1:].split(':')[1]] += mem[value(ins[1:].split(':')[0])]
        else:
            RAA[ins[1:].split(':')[1]] += value(ins[1:].split(':')[0])

    # Ending
    prnt(f"{instruction}: {ins} {pointer}: {mem[pointer]}")


do_print = input("Enable Debug Mode? y/n: ") == "y"
string = input("Enter Code: ")
list = Tokenise(string)
pointer = 0
instruction = 0
mem = {0: 0}
RAA = {}
while instruction < len(list):
    run(list[instruction])
    prnt(f"mem:{mem}")
    prnt(f"RAA:{RAA}")
