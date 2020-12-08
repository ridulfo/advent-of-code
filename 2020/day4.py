import re

def getPass():
    with open("inputDay4.txt", "r") as f:
        passports = list()
        for passport in f.read().strip().split("\n\n"):
            passport = re.split(" |\n", passport)
            passDict = dict()
            for field in passport:
                key, value = field.split(":")
                passDict[key] = value
            passports.append(passDict)
        return passports

def part1():
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return sum([1 for passport in getPass() if all(field in passport for field in fields)])

def part2():
    validation = {
            "byr" : lambda x: int(x) in range(1920, 2003),
            "iyr" : lambda x: int(x) in range(2010, 2021),
            "eyr" : lambda x: int(x) in range(2020, 2031),
            "hgt" : lambda x: int(x[:-2]) in range(150, 194) if "cm" in x[-2:] else (int(x[:-2]) in range(59, 77) if "in" in x[-2:] else False),
            "hcl" : lambda x: bool(re.search(r"^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$", x)),
            "ecl" : lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            "pid" : lambda x: bool(re.search(r"^\d{9}$", x))
        }
    count = 0
    for p in getPass():
        if not all(field in p for field in validation.keys()): continue
        if not all(validation[k](v) for k,v in p.items() if k != "cid"): continue
        count += 1
    return count

print(part1())
print(part2())
