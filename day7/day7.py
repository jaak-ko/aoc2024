from itertools import product
from operator import add, mul

def valid_line(correct_res, line, p2=False):

    ops = [add, mul] if not p2 else [add, mul, lambda a,b: int(str(a) + str(b))]

    nums = list(map(int, line.strip().split(' ')))

    for op_comb in list(product(ops, repeat=len(nums)-1)):
        res = nums[0]
        for j, op in enumerate(op_comb):
            res = op(res, nums[j+1])

        if int(correct_res) == res: return True

    return False


def p1(data):
    
    lines = list(filter(lambda x : valid_line(*x), data))
    return sum(int(i[0]) for i in lines), lines


def p2(data, valid_lines):

    invalids = list(filter(lambda x : x not in valid_lines, data))
    lines = list(filter(lambda x : valid_line(*x, True), invalids))
    return sum(int(i[0]) for i in lines)


def main():

    with open('day7/input.txt', 'r') as f:
        data = [x.split(':') for x in f.read().splitlines()]

    p1_res, valid_lines = p1(data)
    print(f"part 1: {p1_res}\npart 2: {p2(data, valid_lines) + p1_res}")

if __name__ == '__main__':
    main()