input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

max_quantities = {"red":12, "green": 13, "blue": 14}

def part1(input_str: str):
    count = 0
    for line in input_str.splitlines():
        gameId, reveals = line.split(":")
        gameId = int(gameId.replace("Game ", ""))

        reveals = reveals.strip().split(";")

        accepted = True
        for reveal in reveals:
            for cube in reveal.split(","):
                number, color = cube.strip().split(" ")
                if int(number) > max_quantities[color]:
                    accepted = False
                    break

        if accepted:
            count+=gameId
    return count

#with open("input02.txt") as f:
#    print(part1(f.read()))

from functools import reduce

def part2(input_str: str):
    games = []
    for line in input_str.splitlines():
        gameId, reveals = line.split(":")
        gameId = int(gameId.replace("Game ", ""))
        game_min = {}

        reveals = reveals.strip().split(";")

        for reveal in reveals:
            for cube in reveal.split(","):
                number, color = cube.strip().split(" ")
                number = int(number)
                if number > game_min.get(color, 0):
                    game_min[color] = number

        games.append(reduce((lambda x, y: x * y), game_min.values()))

    return sum(games)

with open("input02.txt") as f:
    print(part2(f.read()))
