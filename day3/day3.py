import re
import numpy as np

def p1(lines) -> int:
    
    muls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", lines)
    return sum([int(mul[0]) * int(mul[1]) for mul in muls])
        
        
def p2(lines) -> int:

    inst = re.findall(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))', lines)

    result = 0
    to_do = True

    for i in inst:
        if i == "do()":
            to_do = True
        elif i == "don't()":
            to_do = False
        elif to_do and i.startswith("mul"):
            result += np.prod(tuple(map(int, re.findall(r"\d{1,3}", i))))

    return result


def main():

    with open("day3/input.txt") as f:
        lines = f.read()

    print(f"part 1: {p1(lines)}\npart 2: {p2(lines)}")

if __name__ == "__main__":
    main()