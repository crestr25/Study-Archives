def bubble_sort(l: list):
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                print(l)
    return l

def print_alg(l):
    print(f"{i} " for i in l)

if __name__ == "__main__":
    l = [1, 3, 5, 15, 2, 5] 
    print(bubble_sort(l))
