
def make_disk(data):
    id = 0
    disk = []
    for i, n in enumerate(data):
        disk += [id] * int(n) if (is_file := i % 2 == 0) else [-1] * int(n)
        if is_file: id += 1

    return disk


def p1(data) -> int:

    disk = make_disk(data)
    while disk.count(-1) > 0:

        if disk[-1] != -1: disk[disk.index(-1)] = disk.pop()
        else: disk.pop()

    return sum([i * n for i, n in enumerate(disk)])


def main():

    with open('day9/input.txt', 'r') as f:
        data = f.read().strip()

    print(p1(data))

if __name__ == '__main__':
    main()