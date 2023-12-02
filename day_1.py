with open('data/day_1') as f:
    data = f.readlines()


def part_1():
    sum_calibration_values = 0

    for line in data:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        
        sum_calibration_values += int(digits[0] + digits[-1])

    return sum_calibration_values


def part_2():
    letters_digit = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    sum_calibration_values = 0

    for line in data:
        digits = []
        for i,char in enumerate(line):
            if char.isdigit():
                digits.append(char)
            for d,val in enumerate(letters_digit):
                if line[i:].startswith(val):
                    digits.append(str(d + 1))
        
        sum_calibration_values += int(digits[0] + digits[-1])

    return sum_calibration_values


print(f'Part 1: {part_1()}')
print('-----------------')
print(f'Part 2: {part_2()}')


