
def p1(data):
    
    xmas_samx = [['X', 'M', 'A', 'S'], ['S', 'A', 'M', 'X']] ; count = 0

    for y, row in enumerate(data):
        for x in range(len(row)):

            # vertical and diagonal
            if y >= 3:
                vert = [data[y-j][x] for j in range(4)]
                dl = [data[y-j][x-j] for j in range(4)] if x >= 3 else None
                dr = [data[y-j][x+j] for j in range(4)] if x+3 < len(row) else None

                count += sum([d in xmas_samx for d in [vert, dl, dr]])

        # horizontal
        count += row.count("XMAS") + row.count("SAMX")

    return count


def p2(data):
    
    mas_sam = [['M', 'A', 'S'], ['S', 'A', 'M']] ; count = 0

    for y in range(1, len(data)-1):
        for x in range(1, len(data[y])-1):

            d1 = [data[y+j][x+j] for j in range(-1, 2)]
            d2 = [data[y+j][x-j] for j in range(-1, 2)]

            count += d1 in mas_sam and d2 in mas_sam

    return count

def main():

    with open("day4/input.txt", "r") as file:
        data = file.read().splitlines()

    print(f"part 1: {p1(data)}\npart 2: {p2(data)}")

if __name__ == "__main__":
    main()