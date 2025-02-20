from collections import defaultdict


def fib(n: int):
    cache = defaultdict(int)

    def fib_wrapper(n: int):
        if n == 1 or n == 2:
            return 1

        if cache[n]:
            return cache[n]

        cache[n] = fib_wrapper(n - 1) + fib_wrapper(n - 2)
        return cache[n]

    return fib_wrapper(n)


print(fib(5))
