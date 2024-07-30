def recursive_factorial(n):
    if n == 2:
        # Factoriral of 2 is 2
        return 2

    return n * recursive_factorial(n - 1)

def iterative_factorial(n):
    res = 1
    for i in range(2, n + 1):
        # starts on 2
        res *= i

    return res


if __name__ == "__main__":

    print(recursive_factorial(3))
    print(iterative_factorial(3))
