

def walk_floors(floors):
    n = 0
    for floor in list(floors):
        if floor == "(":
            n += 1
        elif floor == ")":
            n -= 1
    return n


def walk_to(floors, stop_at):
    n = 0
    i = -1
    while n != stop_at:
        i += 1
        floor = floors[i]
        if floor == "(":
            n += 1
        elif floor == ")":
            n -= 1
    return i + 1


with open('data/day_01.txt') as fh:
    floors = fh.read()

print("Part 1")
print(walk_floors(floors))

print("Part 2")
print(walk_to(floors, -1))