def fibonnaci_recursive(n):
    # O(2^n)
    if n < 2:
        return n

    return fibonnaci_recursive(n - 1) + fibonnaci_recursive(n - 2)

def fibonnaci_iterative(n):
    # O(n)
    a = 0 
    b = 1
    c = 0

    if n < 2:
        return n

    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return c

if __name__ == "__main__":
    print(fibonnaci_recursive(5))
    print(fibonnaci_iterative(5))
