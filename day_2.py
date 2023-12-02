from collections import defaultdict

data = {}
with open('data/day_2') as f:
    for index,line in enumerate(f.readlines()):
        data[index] = line


def part_1():
    limits_colors = {'red': 12, 'green': 13, 'blue': 14}
    sum = 0

    for index,value in data.items():
        possible = True
        game_id,line = value.split(':')
        for sets in line.split(';'):
            for balls in sets.split(','):
                num,color = balls.split()
                if int(num) > limits_colors.get(color):
                    possible = False
        if possible:
            sum += int(game_id.split()[1])

    return sum



def part_2():
    limits_colors = {'red': 12, 'green': 13, 'blue': 14}
    sum = 0

    for index,value in data.items():
        possible = True
        game_id,line = value.split(':')
        values = defaultdict(int)
        for sets in line.split(';'):
            for balls in sets.split(','):
                num,color = balls.split()
                values[color] = max(values[color], int(num))
                if int(num) > limits_colors.get(color):
                    possible = False
        
        score = 1
        for value in values.values():
            score *= value
        sum += score

    return sum


print(f'Part 1: {part_1()}')
print('-----------------')
print(f'Part 2: {part_2()}')