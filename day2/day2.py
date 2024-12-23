

def is_safe(l) -> bool:

    if sorted(l, reverse=True) != l and sorted(l) != l:
        return False
    
    return all( 0 != abs(l[i] - l[i+1]) <= 3 for i in range(len(l) - 1))   


def p1(lines) -> int:
    
    return sum([int(is_safe(l)) for l in lines])
        
        
def p2(lines) -> int:

    num_of_safes = 0
    for line in lines:
        if is_safe(line):
            num_of_safes += 1
        elif any(is_safe(line[:i] + line[i+1:]) for i in range(len(line))):
                num_of_safes += 1

    return num_of_safes
    

def main():

    with open("day2/input.txt") as f:

        lines = [list(map(int, line.split())) for line in f.readlines()]

    print(f"part 1: {p1(lines)}\npart 2: {p2(lines)}")


if __name__ == "__main__":
    main()