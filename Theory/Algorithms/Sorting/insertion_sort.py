def insertion_sort(l):
    for i in range(len(l) - 1):
        if l[i+1] < l[i]:
            for j in range(i + 1):
                if l[i+1] < l[j]:
                    _temp = l[j]
                    l[j] = l[i+1]
                    l[i+1] = _temp

        print(l)




if __name__ == "__main__":
    l = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    insertion_sort(l)
