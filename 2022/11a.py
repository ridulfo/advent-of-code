import re 
with open("inputs/day11.txt") as f:
    s = f.read()

# s = """Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1"""

class Monkey:
    def __init__(self, description, monkeys):
        self.monkeys = monkeys
        numbers = [list(map(int, re.findall(r"\s(\d+)", line))) for line in description.split("\n")]
        self.starting_numbers = numbers[1]
        self.divisor = numbers[3][0]
        self.true = numbers[4][0]
        self.false = numbers[5][0]
        self.op = re.findall(r"Operation: new = (.*)\n", description)[0]
        self.count_throws = 0
    
    def throw_all_items(self):
        while len(self.starting_numbers) > 0:
            item = self.starting_numbers.pop(0)
            old = item
            new = eval(self.op)
            new = new //3
            if new % self.divisor == 0:
                self.monkeys[self.true].starting_numbers.append(new)
            else:
                self.monkeys[self.false].starting_numbers.append(new)
            self.count_throws += 1
    
    def __str__(self):
        return "Monkey: " + str(self.starting_numbers)

monkeys= []
for monkey in s.split("\n\n"):
    monkeys.append(Monkey(monkey, monkeys))

for round in range(1, 21):
    for monkey in monkeys:
        monkey.throw_all_items()
a, b = sorted([monkey.count_throws for monkey in monkeys])[-2:]
print(a*b)


