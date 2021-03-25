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
    
    # pointer shifting
    if ins[0] == "+":
        for thing in ins[1:].split("+"):
            pointer += 1
    if ins[0] == "-":
        for thing in ins[1:].split("-"):
            pointer -= 1
    

    #Ending
    print(f"{instruction}: {ins} {pointer}")


string = input("Enter Code: ")
list = Tokenise(string)
pointer = 0
instruction = 0
mem = {}
while instruction < len(list):
    run(list[instruction])
