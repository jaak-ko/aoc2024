from numpy import inf
from itertools import count

def get_anti_nodes(x1, y1, pairs, data, part2 = False) -> set[tuple[int, int]]:

    anti_nodes = set()
    i = 1
    for x2, y2 in pairs:
        for i in count(1):
            max_x, min_x, dx = max(x1, x2), min(x1, x2), abs(x2 - x1)
            max_y, min_y, dy = max(y1, y2), min(y1, y2), abs(y2 - y1)

            k = -(y1 - y2)/(x1 - x2) if dx != 0 else inf

            if k > 0:
                cands = [(max_x + dx*i, min_y - dy*i), 
                         (min_x - dx*i, max_y + dy*i)]
            if k < 0:
                cands = [(min_x - dx*i, min_y - dy*i), 
                         (max_x + dx*i, max_y + dy*i)]
            if k == 0:
                cands = [(min_x - dx*i, y1), 
                         (max_x + dx*i, y1)]
            if k == inf:
                cands = [(x1, min_y - dy*i), 
                         (x1, max_y + dy*i)]
                
            cands = {(nx, ny) 
                     for nx, ny in cands 
                     if 0 <= nx < len(data) and 0 <= ny < len(data)}
            anti_nodes.update(cands)

            if part2 and i == 1: anti_nodes.update({(x1, y1), (x2, y2)})
            if not part2 or len(cands) == 0: break

    return anti_nodes


def parts(data) -> tuple[int, int]:

    def find_pairs(x, y, f, data) -> set[tuple[int, int]]:
        return {(j, i) 
                for i, row in enumerate(data) 
                for j, cell in enumerate(row) 
                if cell == f and (i, j) != (y, x)}

    anti_nodes = set()
    anti_nodes2 = set()
    for i, row in enumerate(data):
        for j in range(len(row)):
            if row[j] != '.':
                pairs = find_pairs(j, i, row[j], data)
                anti_nodes.update(
                    get_anti_nodes(j, i, pairs, data))
                anti_nodes2.update(
                    get_anti_nodes(j, i, pairs, data, True))
    
                
    return len(anti_nodes), len(anti_nodes2)
    

def main():
    with open('day8/input.txt', 'r') as f:
        data = list(map(list, f.read().splitlines()))

    p1_res, p2_res = parts(data)
    print(f"part 1: {p1_res}\npart 2: {p2_res}")

if __name__ == '__main__':
    main()