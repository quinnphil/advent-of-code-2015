import numpy as np

def get_data(path_data):
    with open(path_data) as fh:
        lines = fh.read().splitlines()

    return lines

def get_commands(data):
    commands = []
    for line in data:
        line = line.replace('turn off', 'turn-off')
        line = line.replace('turn on', 'turn-on')
        command = line.split(' ')
        commands.append([command[0],
                         [int(i) for i in command[1].split(',')],
                         [int(i) for i in command[3].split(',')],
                         ])
    return commands



print("Part 1")

data = get_data('data/day_06.txt')
commands = get_commands(data)


def part_1(commands):

    lights = np.zeros((1000, 1000), dtype=bool)
    for command in commands:
        if command[0] == "turn-on":
            lights[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1] = 1
        if command[0] == "turn-off":
            lights[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1] = 0
        if command[0] == "toggle":
            lights[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1] = ~lights[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1]
    return lights.sum()


print(part_1(commands))

def part_2(commands):

    lights = np.zeros((1000, 1000), dtype=int)
    for command in commands:
        if command[0] == "turn-on":
            lights[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1] += 1
        if command[0] == "turn-off":
            lights[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1] -= 1
            lights[lights<0] = 0

        if command[0] == "toggle":
            lights[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1] = lights[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1] + 2
    return lights.sum()


print("\nPart 2")
print(part_2(commands))

