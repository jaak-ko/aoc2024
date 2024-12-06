
from copy import deepcopy

def starting_point(data):
    for y, row in enumerate(data):
        if not all(row[x] == "." or row[x] == '#' for x in range(len(row))):
            x = next(row.index(x) for x in ['^', 'v', '<', '>'] if x in row)
            mark  = row[x]
            return x, y, mark


def check(x, y, mark, width, heigth) -> bool:

    match mark:
        case '^':
            return y > 0
        case 'v':
            return y < heigth - 1
        case '<':
            return x > 0
        case '>':
            return x < width - 1
    

def move_guard(x, y, mark, data) -> tuple[int, int, str]:

    match mark:
        case '^':
            return (x, y-1, mark) if data[y-1][x] != "#" else (x, y, '>')
        case 'v':
            return (x, y+1, mark) if data[y+1][x] != "#" else (x, y, '<')
        case '<':
            return (x-1, y, mark) if data[y][x-1] != "#" else (x, y, '^')
        case _:
            return (x+1, y, mark) if data[y][x+1] != "#" else (x, y, 'v')


def loops(x, y, mark, data) -> bool:

    data[y][x] = "#"
    x, y, mark = starting_point(data)

    seen = set()
    while check(x, y, mark, len(data[0]), len(data)):

        seen.add((x, y, mark))
        x, y, mark = move_guard(x, y, mark, data)

        if (x, y, mark) in seen:
            return True

    return False


def p1(data) -> tuple[int, set]:
    
    x, y, mark = starting_point(data)
    p1_pos = set() ; p2_path = set()

    while check(x, y, mark, len(data[0]), len(data)):
        
        x, y, mark = move_guard(x, y, mark, data)
        p1_pos.add((x, y))
        p2_path.add((x, y, mark))

    return len(p1_pos), p2_path


def p2(data, p2_seen) -> int:

    x, y, mark = starting_point(data)
    start = (x, y)
    blocks = set()

    for x, y, mark in p2_seen:
        if (x, y) == start:
            continue
        
        if loops(x, y, mark, deepcopy(data)):
            blocks.add((x, y))

    return len(blocks)


def main():

    with open("day6/input.txt") as f:
        data = list(map(list, f.read().splitlines()))

    p1_result, p2_path = p1(data)
    p2_result = p2(data, p2_path)

    print(f"part 1: {p1_result}\npart 2: {p2_result}")

if __name__ == "__main__":
    main()