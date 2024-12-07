from itertools import product
from operator import add, mul

def valid_line(correct_res, line, p1=True):

    ops = [add, mul] if p1 else [add, mul, 'or']

    nums = list(map(int, line.strip().split(' ')))
    op_combs = list(product(ops, repeat=len(nums)-1))

    for op_comb in op_combs:
        res = nums[0]
        for j, op in enumerate(op_comb):

            if op == 'or': res = int(str(res) + str(nums[j+1])) ; j += 1
            else: res = op(res, nums[j+1])

        if int(correct_res) == res: return True

    return False


def p1(data):
    
    lines = list(filter(lambda x : valid_line(*x), data))
    return sum(int(i[0]) for i in lines), lines


def p2(data, valid_lines):

    invalids = list(filter(lambda x : x not in valid_lines, data))
    lines = list(filter(lambda x : valid_line(*x, p1=False), invalids))
    return sum(int(i[0]) for i in lines)


def main():

    with open('day7/input.txt', 'r') as f:
        data = [x.split(':') for x in f.read().splitlines()]

    p1_res, valid_lines = p1(data)
    print(f"part 1: {p1_res}\npart 2: {p2(data, valid_lines) + p1_res}")

if __name__ == '__main__':
    main()