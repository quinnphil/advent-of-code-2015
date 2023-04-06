
from collections import defaultdict, deque
import re


circuit = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i""".split("\n")

def get_state(circuit):
    state = defaultdict(int)
    queue = deque(circuit)
    i = 0
    while queue and state.get('a') is None and i < 10000:
        i+=1
        com = queue.popleft()
        # Set register
        if match := re.match('(\d+) -> (\w+)', com):
            val = int(match.group(1))
            reg = match.group(2)
            print(val, reg)
            state[reg] = val
        # AND
        elif match := re.match('(\w+) (\w+) ([a-z0-9]+) -> (\w+)', com):
            i1 = state.get(match.group(1))
            opr = match.group(2)
            if match.group(3).isalpha():
                i2 = state.get(match.group(3))
            else:
                i2 = int(match.group(3))
            reg = match.group(4)
            print(f"{i1=} {opr=} {i2=} {reg=} : {com}")
            # Can we process?
            if i1 is None or i2 is None:
                print(f'Not enough info to process {len(queue)}')
                queue.append(com)
                continue
            match opr:
                case "AND": val = i1 & i2
                case "OR": val = i1 | i2
                case "LSHIFT": val = (i1 | 65536) << int(i2)
                case "RSHIFT": val = (i1 | 65536)  >> int(i2)
            state[reg] = val
        elif match := re.match('NOT (\w+) -> (\w+)', com):
            i1 = state.get(match.group(1))
            if i1 is None:
                print(f'Not enough info to process {len(queue)}')
                queue.append(com)
                continue
            reg = match.group(2)
            val = ~i1
            state[reg] = val

        if state[reg] < 0:
            state[reg] = 65536 + state[reg]
        if state[reg] >= 65535:
            state[reg] = state[reg] % 65535


        else:
            print(com)

        # AND
        # OR
        # NOT
        # LSHIFT
        # RSHIFT
    return state

def print_state(state):
    for k in sorted(list(state.keys())):
        print(k, "=>", state[k])


# print("Test")
# state = get_state(circuit)
# print_state(state)

def read_data(path_data):
    with open(path_data) as fh:
        data = fh.read().splitlines()

    return data


print("Part 1")
circuit = read_data('data/day_07.txt')
state = get_state(circuit)
print_state(state)
print(state.get('a'))