def Tokenise(string):
    return string.split(">")


def run(ins):
    global pointer
    global instruction
    pointer = pointer
    instruction = instruction
    ins + ""
    if ins == "":
        print(f"{instruction}: {ins} {pointer}")
        instruction += 1
        return
    # memory index altering
    if ins[0] == "+":
        for thing in ins[1:].split("+"):
            pointer += 1
    if ins[0] == "-":
        for thing in ins[1:].split("-"):
            pointer -= 1
    

    #Ending
    instruction += 1
    print(f"{instruction}: {ins} {pointer}")


string = input("Enter Code: ")
list = Tokenise(string)
pointer = 0
instruction = 0
while instruction < len(list):
    run(list[instruction])
