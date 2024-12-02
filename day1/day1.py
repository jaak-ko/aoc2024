import numpy as np
from collections import Counter

def p1(lines):
    return \
        np.sum(
            np.abs(
                np.subtract(sorted([l[0] for l in lines]), 
                            sorted([l[1] for l in lines])))
        )
        
def p2(lines):

    lefts = [l[0] for l in lines]
    rights = [l[1] for l in lines]

    return np.sum([i * rights.count(i) for i in lefts])
    

def main():
    with open("input.txt") as f:
        lines = [l.split('   ') for l in f.read().splitlines()]
        lines = [[int(l[0]), int(l[1])] for l in lines]

    print("part 1:", p1(lines))
    print("part 2:", p2(lines))

if __name__ == "__main__":
    main()