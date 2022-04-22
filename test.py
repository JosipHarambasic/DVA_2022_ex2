import array as arr
def arrs(n):
    sol = None
    # check if all elements in ls are integers
    if all([isinstance(item, int) for item in n]) and all([100000 >= item >= -100000 for item in n]):
        n.sort()
        for idx in range(len(n)-1):
            if n[-1] <= 0:
                sol = 1
            elif n[idx+1] - n[idx] > 1 and n[idx] > 0:
                sol = n[idx] + 1
            else:
                sol = n[-1] + 1
        return sol
    else:
        return "Only integeras are allowed"


print(arrs([-1, 2,3]))
