import time
intCode = [int(x) for x in  open('inputDay2.txt').read().split(',')]

def runComputer(code, replace1, replace2):
	code[1] = replace1
	code[2] = replace2
	index = 0
	while code[index]!=99:
		if code[index]==1:
			code[code[(index+3)]] = code[code[(index+1)]]+code[code[(index+2)]]
		elif code[index]==2:
			code[code[(index+3)]] = code[code[(index+1)]]*code[code[(index+2)]]
		index = (index+4)
	return code[0]

#Part 2
for noun in range(0,99+1):
	for verb in range(0,99+1):
		if runComputer(intCode.copy(), noun, verb) == 19690720:
			print(str(noun) + " : " + str(verb))
			print(100*noun+verb)
			
#Part 1
print(runComputer(intCode.copy(), 12,2))
