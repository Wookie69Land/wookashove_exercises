def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_list(number):
    if number == 0:
        return [0]
    return [fib(n) for n in range(number)]


if __name__ == '__main__':
    print(fib_list(1))
    print(fib_list(3))
    print(fib_list(15))
    print(fib_list(0))