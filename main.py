import time

def Tokenise(string):
    return string.split(">")


def value(string):
    if string[0] == "R":
        return RAAval(string)
    elif string[0] == "M":
        return mem[value(string[1:])]
    try:
        return int(string)
    except:
        return string


def Arithmetic(operand, values):
    if len(values) > 2:
        print(f"Arithmetic Error @{instruction}: More than two arguments: {values}")

    # Add
    if operand == "+":
        if values[1][0] == "R":
            RAA[values[1][1:]] += value(values[0])
        elif values[1][0] == "M":
            mem[int(values[1][1:])] += value(values[0])

    # Subtract
    elif operand == "-":
        pass

    # Multiply
    elif operand == "*":
        pass

    # Divide
    elif operand == "/":
        pass

    # Modulo
    elif operand == "%":
        pass


def prnt(thing):
    if do_print:
        print(thing)


def RAAval(string):
    if string[1] == "R":
        return RAAval(string[1:])
    return RAA[string[1:]]

def run(ins):
    global pointer
    global instruction

    # Weird errors
    pointer  = pointer
    instruction = instruction
    
    instruction += 1
    if ins == "":
        print(f"{instruction}: {ins} {pointer}")
        return

    # Pointer shifting
    # Use: ...>++>++++>+>++++++++++...
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
    # Use: ...>!0>!45>!Rvalue>...
    if ins[0] == "!":
        instruction = value(ins[1:])
    
    # Reading memory into RAA
    # Use: ...>*some value to be referenced later>...
    if ins[0] == "*":
        RAA[value(ins[1:])] = mem[pointer]

    # Moving pointer using integer constants and RAA
    # Use: ...>@2>@0>@Rvalue
    if ins[0] == "@":
        pointer = int(value(ins[1:]))
        try:
            errorQuery = mem[pointer]
        except:
            mem[pointer] = 0
    
    # Setting memory values with integer constants and RAA
    # ...>$12>$-19>$Rvalue
    if ins[0] == "$":
        mem[pointer] = value(ins[1:])
    
    # Incrementing memory values with integer constants and RAA
    # Use: ...>i1>iRvalue>i12>...
    if ins[0] == "i":
        mem[pointer] += int(value(ins[1:]))
    
    # Adding delays in milliseconds(w/ RAA)
    # Use: ...>#100>#142>#Rvalue>...
    if ins[0] == "#":
        time.sleep(value(ins[1:]) / 1000)
    
    # Conditional Jumps
    # Use: ...>?5:14>?Rvalue1:Rvalue2>...
    if ins[0] == "?":
        if mem[pointer] == value(ins[1:].split(':')[0]):
            instruction = value(ins[1:].split(':')[1])
    
    # Print
    # Use: ...>.>...
    if ins == ".":
        print(mem[pointer])
    
    # Basic Arithmetic
    # Use: ..>%+15:value>%-value1:value2>%+M2:Rbob...
    if ins[0] == "%":
        Arithmetic(ins[1],ins[2:].split(":"))

    # End step
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
