def selection_sort(l: list):

    for i in range(len(l)):
        min_ind = i
        for j in range(i, len(l)):
            if l[min_ind] > l[j]:
                min_ind = j

        _temp = l[i]
        l[i] = l[min_ind]
        l[min_ind] = _temp 

        print(l)

if __name__ == "__main__":
    l = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    selection_sort(l)
