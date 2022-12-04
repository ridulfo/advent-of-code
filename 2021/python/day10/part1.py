ex = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
types = "()", "[]", "{}", "<>"

def stack_check(line):
    stack = [line[0]]
    for c in line[1:]:
        print(" ".join(stack), " - " , c)
        for type in types:
            if stack[-1] == type[0] and c == type[1]:
                stack.pop()
                break
            else:
                stack.append(c)
                break

for line in ex.splitlines():
    stack_check(line)
    exit()