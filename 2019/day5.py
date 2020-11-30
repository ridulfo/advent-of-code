
def runComputer(code):
    """
    ABCDE
     1002

    DE - two-digit opcode,      02 == opcode 2
     C - mode of 1st parameter,  0 == position mode
     B - mode of 2nd parameter,  1 == immediate mode
     A - mode of 3rd parameter,  0 == position mode,
                                      omitted due to being a leading zero
    """
    i = 0  # index
    while code[i] != 99:
        curcode = str(code[i])
        curcode= curcode.zfill(5)
        print(curcode)
        opcode = int(curcode[-2:])
        m1 = int(curcode[-3])
        m2 = int(curcode[-4])
        m3 = int(curcode[-5])

        if opcode == 1 or opcode == 2:
            param1 = code[code[(i+1)]] if m1 == 0 else code[(i+1)]
            param2 = code[code[(i+2)]] if m2 == 0 else code[(i+2)]

            value = 0
            if opcode == 1:
                value = param1 + param2
            elif opcode == 2:
                value = param1 * param2

            if m3 == 0:
                code[code[(i+3)]] = value
            else:
                code[(i+3)] = value
            i += 4

        elif opcode == 3:
            param1 = int(input("Input: "))
            if m1 == 0:
                code[code[(i+1)]] = param1
            i+=2

        elif opcode == 4:
            param1 = code[code[(i+1)]] if m1 == 0 else code[(i+1)]
            print(param1)
            i+=2

        elif opcode == 5:
            param1 = int(code[code[(i+1)]] if m1 == 0 else code[(i+1)])
            param2 = int(code[code[(i+2)]] if m2 == 0 else code[(i+2)])
            if param1!=0:
                i= param2
            else:
                i+=3
        elif opcode == 6:
            param1 = int(code[code[(i+1)]] if m1 == 0 else code[(i+1)])
            param2 = int(code[code[(i+2)]] if m2 == 0 else code[(i+2)])
            if param1 == 0:
                i= param2
            else:
                i+=3
        elif opcode == 7:
            param1 = code[code[(i+1)]] if m1 == 0 else code[(i+1)]
            param2 = code[code[(i+2)]] if m2 == 0 else code[(i+2)]
            param3 = code[i+3] if m3 == 0 else i+2

            if param1<param2: 
                code[param3] = 1
            else:
                code[param3] = 0
            i+=4

        elif opcode == 8:
            param1 = code[code[(i+1)]] if m1 == 0 else code[(i+1)]
            param2 = code[code[(i+2)]] if m2 == 0 else code[(i+2)]
            param3 = code[i+3] if m3 == 0 else i+2

            if param1==param2: 
                code[param3] = 1
            else:
                code[param3] = 0
            i+=4

    return code[0]

with open("inputDay5.txt", "r") as f:
    runComputer([int(x) for x in f.read().split(",")])
