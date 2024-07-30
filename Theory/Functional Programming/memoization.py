import time


def fib(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


def cache_fib():
    cache_dict = {}

    def _internal_fib(n):
        if n in cache_dict:
            return cache_dict[n]
        else:
            if n < 2:
                return n
            else:
                cache_dict[n] = _internal_fib(n - 1) + _internal_fib(n - 2)
                return cache_dict[n]

    return _internal_fib


def fib_bottomup(n):
    answer = [0, 1]

    for i in range(2, n + 1):
        answer.append(answer[i - 2] + answer[i - 1])

    return answer.pop()


if __name__ == "__main__":
    n = 100

    start = time.perf_counter()

    fib_cache = cache_fib()
    res = fib_cache(n)

    stop = time.perf_counter()

    print(f"fib_functional({n}) = {res}, took {round(stop - start, 5)} seg")

    start = time.perf_counter()

    res = fib_bottomup(n)

    stop = time.perf_counter()

    print(f"fib_bottomup({n}) = {res}, took {round(stop - start, 5)} seg")
