def stalin_sort(input_list):
    """
        Loops through list, removing any elements out of order
    """
    i = 0
    while i < len(input_list)-1:
        if input_list[i] > input_list[i+1]:
            input_list.pop(i+1)
        else:
            i += 1
    return input_list


def split_stalin_sort(input_list):
    """
        Returns 2 lists - kept and stalinized
    """
    tooinputtoofurious = []
    for i in input_list:
        tooinputtoofurious.append(i)

    kept_list = stalin_sort(input_list)

    tookepttoofurious = []
    for i in kept_list:
        tookepttoofurious.append(i)

    i = 0
    ii = 0
    while i < len(tookepttoofurious):
        while ii < len(tooinputtoofurious):
            if tookepttoofurious[i] == tooinputtoofurious[ii]:
                tooinputtoofurious.pop(ii)
                break
            else:
                ii += 1
        i += 1
    return [tookepttoofurious, tooinputtoofurious]


def recursively_stalining(input_list, i):
    """
        Recursive sort, returns sorted list
    """
    kept, split = split_stalin_sort(input_list)
    if len(split) != 0:
        new = split+kept
        return(recursively_stalining(new, i+1))
    else:
        return(kept)
