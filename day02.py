import math

def get_sides(l, w, h):
    return [(l * w), (w * h), (h * l)]

def get_area(sides):
    return sum(2 * side for side in sides)

def get_shortest_side(sides):
    shortest = sorted(sides)[0]
    return shortest

def get_paper(l, w, h):
    sides = get_sides(l, w, h)
    area = get_area(sides)
    shortest_side = get_shortest_side(sides)
    return area + shortest_side

def get_ribbon(sides):

    wrap = sum(sorted(sides * 2)[:4])
    bow = math.prod(sides)
    return wrap + bow




with open('data/day_02.txt') as fh:
    packages = []
    for line in fh.readlines():
        package = [int(s) for s in line.split('x')]
        packages.append(package)

print(packages)

print("Part 1")
paper = 0
for package in packages:
    paper += get_paper(*package)
print(paper)

print("\nPart 2")
ribbon = 0
for package in packages:
    ribbon += get_ribbon(package)
print(ribbon)