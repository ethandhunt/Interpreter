import time
import binascii

def Tokenise(string):
    return string.split(">")


def intToString(n):
    # I have no idea how this works
    return binascii.unhexlify(format(n, "x").encode("utf-8")).decode("utf-8")


def stringToInt(string):
    # Or this
    return int(binascii.hexlify(string.encode("utf-8")), 16)

def RAAval(string):
    if string[1] == "R":
        return RAAval(string[1:])
    return RAA[string[1:]]


def value(string):
    if len(string.split("%")) > 1:
        operator = string.split("%")[1].split("|")[0]
        values = [string.split("%")[0], string.split("%")[1].split("|")[1]]
        if len(string.split("%")) > 2:
            print(f"InlineArithmetic Error@{instruction}: more than two arguments: {string}")
        elif operator == "+":
            return value(values[0]) + value(values[1])
        elif operator == "-":
            return value(values[0]) - value(values[1])
        elif operator == "*":
            return value(values[0]) * value(values[1])
        elif operator == "/":
            return value(values[0]) / value(values[1])
        elif operator == "mod":
            return value(values[0]) % value(values[1])
    elif string[0] == "R":
        return RAAval(string)
    elif string[0] == "M":
        return mem[value(string[1:])]
    elif string[0] == "P":
        return points[string[1:]]
    elif string == "pointer":
        return pointer
    elif string[0] == "a":
        thing = value(string[1:])
        if type(thing) == int:
            return intToString(thing)
        elif type(thing) == str:
            return stringToInt(thing)
        else:
            print("???")
    try:
        return int(string)
    except:
        return string


def Arithmetic(values):
    if len(values) > 3:
        print(f"Arithmetic Error @{instruction}: More than three arguments: {values}")
    
    operand = values[0]
    values = [values[1], values[2]]

    # Add
    if operand == "+":
        if values[1][0] == "R":
            RAA[values[1][1:]] += value(values[0])
        elif values[1][0] == "M":
            mem[int(values[1][1:])] += value(values[0])

    # Subtract
    elif operand == "-":
        if values[1][0] == "R":
            RAA[values[1][1:]] -= value(values[0])
        elif values[1][0] == "M":
            mem[int(values[1][1:])] -= value(values[0])

    # Multiply
    elif operand == "*":
        if values[1][0] == "R":
            RAA[values[1][1:]] *= value(values[0])
        elif values[1][0] == "M":
            mem[int(values[1][1:])] *= value(values[0])

    # Divide
    elif operand == "/":
        if values[1][0] == "R":
            RAA[values[1][1:]] /= value(values[0])
        elif values[1][0] == "M":
            mem[int(values[1][1:])] /= value(values[0])

    # Modulo
    elif operand == "mod":
        if values[1][0] == "R":
            RAA[values[1][1:]] = RAA[values[1][1:]] % value(values[0])
        elif values[1][0] == "M":
            mem[int(values[1][1:])] = mem[int(values[1][1:])] % value(values[0])
    
    else:
        print("???")


def condition(array):
    global instruction
    operator = array[0]
    item = value(array[1])
    instruct = value(array[2])
    thing = mem[pointer]
    if len(array) > 3:
        print(f"Conditional Error @{instruction}: More than three arguments: {array}")
    elif operator == "=":
        if item == thing:
            run(instruct)
    elif operator == "Gt":
        if item < thing:
            run(instruct)
    elif operator == "Lt":
        if item > thing:
            run(instruct)
    elif operator == "Dv":
        if int(thing / item) == thing / item:
            run(instruct)


def prnt(thing):
    if do_print:
        print(thing)

def run(ins):
    global pointer
    global instruction
    
    instruction += 1
    if ins == "":
        return
    if ins == "Debug":
        print(f"{instruction}: {ins} {pointer}")
        return

    # Pointer shifting
    # Use: ...>++>---->+>++++++++++...
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
    
    # Points
    # Use: ...>Pthing>P_other thing>P_moreThings>!thing>!_other thing>...
    if ins[0] == "P":
        points[ins[1:]] = instruction
    

    # Goto Functionality
    # Use: ...>!0>!45>!Rvalue>...
    if ins[0] == "!":
        instruction = value(ins[1:])
    
    # Reading memory into RAA
    # Use: ...>*some value to be referenced later>...
    if ins[0] == "*":
        RAA[value(ins[1:])] = mem[pointer]

    # Set the pointer using integer constants and RAA
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
        mem[pointer] += value(ins[1:])
    
    # Adding delays in milliseconds(w/ RAA)
    # Use: ...>#100>#142>#Rvalue>...
    if ins[0] == "#":
        time.sleep(value(ins[1:]) / 1000)
    
    # Conditional Jumps
    # Use: ...>?=:5:14>?Gt:Rvalue1:Rvalue2>...
    if ins[0] == "?":
        condition(ins[1:].split(":"))
        try:
            errorQuery = mem[pointer]
        except:
            mem[pointer] = 0
    
    # Print
    # Use: ...>.>...
    if ins == ".":
        print(mem[pointer])
    elif ins[0] == ".":
        print(value(ins[1:]))
    
    # Basic Arithmetic
    # Use: ..>%+:15:value>%-:value1:value2>%+:M2:Rbob...
    if ins[0] == "%":
        Arithmetic(ins[1:].split(":"))


    # End step
    prnt(f"{instruction}: {ins} {pointer}: {mem[pointer]}")
    prnt(f"mem:{mem}")
    prnt(f"RAA:{RAA}")


def start():
    global instruction
    global mem
    global RAA
    global pointer
    global points
    string = input("Enter Code: ")
    list = Tokenise(string)
    pointer = 0
    instruction = 0
    mem = {0: 0}
    RAA = {}
    points = {}
    while instruction < len(list):
        run(list[instruction])

do_print = input("Enable Debug Mode? y/n: ") == "y"
while True:
    start()