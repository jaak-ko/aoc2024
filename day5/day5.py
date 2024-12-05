
def in_order(ordr, inst):
    for f, l in inst:
        if any(ordr[i] == l and f in ordr[i:] for i in range(len(ordr))) or \
           any(ordr[i] == f and l in ordr[:i] for i in range(len(ordr))):
            return False
        
    return True
    

def order(inst, ordr):

    while True:
        is_ordered = True
        for i in range(len(ordr) - 1):
            if (ordr[i+1], ordr[i]) in inst:
                is_ordered = False
                ordr[i], ordr[i+1] = ordr[i+1], ordr[i]
        
        if is_ordered:
            return ordr


def p1(inst, ordrs):
    
    ordered = list(filter(lambda x: in_order(x, inst), ordrs))
    return sum([o[len(o)//2] for o in ordered])
    

def p2(inst, ordrs):
    
    un_ordered = list(filter(lambda x: not in_order(x, inst), ordrs))
    return sum([order(inst, l)[len(l)//2] for l in un_ordered])


def main():

    with open("day5/input.txt", "r") as file:
        inst, ordrs = file.read().split("\n\n")
        inst = [tuple(map(int, x.split('|'))) for x in inst.splitlines()]
        ordrs = [list(map(int, x.split(','))) for x in ordrs.splitlines()]

    print(f"part 1: {p1(inst, ordrs)}\npart 2: {p2(inst, ordrs)}")

if __name__ == "__main__":
    main()