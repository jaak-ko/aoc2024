import numpy as np

def p1(lines) -> int:
    return \
        np.sum(
            np.abs(
                np.subtract(sorted([l[0] for l in lines]), 
                            sorted([l[1] for l in lines])))
        )
        
        
def p2(lines) -> int:

    lefts = [l[0] for l in lines]
    rights = [l[1] for l in lines]

    return np.sum([i * rights.count(i) for i in lefts])
    

def main():
    
    with open("day1/input.txt") as f:
        lines = [l.split('   ') for l in f.read().splitlines()]
        lines = [[int(l[0]), int(l[1])] for l in lines]

    print(f"part 1: {p1(lines)}\npart 2: {p2(lines)}")

if __name__ == "__main__":
    main()