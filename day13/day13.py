import re

def p1(data, p2 = False):
    count = 0
    for item in data:

        x1, y1, x2, y2, gx, gy = map(int, re.findall(r'\d+', item))
        if p2:
            gx, gy = gx + 10000000000000, gy + 10000000000000

        a = (gx * y2 - gy * x2) / (x1 * y2 - x2 * y1)
        b = (gx - x1 * a) / x2
        if int(a) != a or int(b) != b:
            continue

        count += int(3*a+b)

    return count


def main():

    with open('day13/input.txt') as f:
        data = f.read().strip().split('\n\n')
        
    print(f"part 1: {p1(data)}\npart 2: {p1(data, True)}")

if __name__ == '__main__':
    main()