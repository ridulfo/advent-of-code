def getCode():
    with open("input8.txt" ,"r") as f:
        lines = list()
        for line in f.read().strip().split("\n"):
            op, arg = line.split(" ")
            lines.append([op, int(arg)])
        return lines

def part1():
    code = getCode()
    past = set()
    pc = 0
    curr = code[pc]
    acc = 0
    while pc not in past and pc<len(code):
        past.add(pc)
        if curr[0]=="acc":
            acc+=curr[1]
        elif curr[0]=="jmp":
            pc+=curr[1]
            curr = code[pc]
            continue
        pc+=1
        curr = code[pc]

    return acc

def part2():
    def run(program):
        past = set()
        pc = 0
        acc = 0
        while pc<len(program):
            curr = program[pc]
            if pc in past:
                return (False, acc)
            past.add(pc)
            if curr[0]=="acc":
                acc+=curr[1]
            elif curr[0]=="jmp":
                pc+=curr[1]
                continue
            pc+=1

        return (True, acc)

    code = getCode()
    
    for i in range(len(code)):
        if code[i][0] in ["jmp","nop"]:
            code[i][0] = "jmp" if code[i][0]=="nop" else "nop"
            status, value = run(code)
            if status: break
            code[i][0] = "jmp" if code[i][0]=="nop" else "nop"
    return value
        
print(part1())
print(part2())
