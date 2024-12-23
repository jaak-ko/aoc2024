from functools import cache

@cache
def count(stone, iteration):
    # if you're wondering, i myself am not this smart

    if iteration == 0: return 1
    if stone == 0: return count(1, iteration-1)

    string = str(stone)
    length = len(string)

    if length % 2 == 0:
        return count(int(string[:length//2]), iteration - 1) + \
               count(int(string[length//2:]), iteration - 1)
    
    return count(stone * 2024, iteration - 1)

def main():

    with open('day11/input.txt') as f:
        data = list(map(int, f.read().strip().split(' ')))

    for i, part in zip((25, 75), ("part 1", "part 2")):
        print(f"{part}: {sum(count(stone, i) for stone in data)}")

if __name__ == '__main__':
    main()