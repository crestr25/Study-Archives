def merge_sort(l):

    if len(l) == 1:
        return l

    return merge(merge_sort(l[:len(l)//2]), merge_sort(l[len(l)//2:]))

def merge(l1, l2):
    print(l1, l2)
    res = []
    while l1 and l2:

        if l1[0] < l2[0]:
            res.append(l1.pop(0))
        else:
            res.append(l2.pop(0))
    if l1:
        print(l1)
        res.extend(l1)
    else:
        print(l2)
        res.extend(l2)
    print(res)

    return res



if __name__ == "__main__":
    l = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    # l = [5, 3, 4, 7, 2]
    print(merge_sort(l))
