from dataclasses import dataclass
from collections import defaultdict

with open('data/day_03.txt') as fh:
    dirs = [d for d in fh.read()]


def visit_houses(dirs):
    houses = defaultdict(int)
    x = 0
    y = 0

    houses[(x, y)] = 1
    for dir in dirs:

        if dir == "^":
            y += 1
        elif dir == "v":
            y -= 1
        elif dir == "<":
            x -= 1
        elif dir == ">":
            x +=1
        houses[(x, y)] += 1
    return houses

@dataclass
class Sled:
    x: int = 0
    y: int = 0


def visit_houses_robo(dirs):
    houses = defaultdict(int)

    santa = Sled()
    robo = Sled()

    houses[(santa.x, santa.y)] = 1
    houses[(robo.x, robo.x)] = 1

    for i, dir in enumerate(dirs):

        if i % 2 == 0:
            sled = santa
        else:
            sled = robo

        if dir == "^":
            sled.y += 1

        elif dir == "v":
            sled.y -= 1

        elif dir == "<":
            sled.x -= 1

        elif dir == ">":
            sled.x +=1

        houses[(sled.x, sled.y)] += 1

    return houses


houses = visit_houses(dirs)
print("Part 1")
print(len(houses))


print("Part 2")
houses2 = visit_houses_robo(dirs)
print(len(houses2))
