def fib(n):
    a, b = 0, 1
    while b < n:
        yield b
        a, b = b, a + b


def fib1(n):
    result = []
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
        result.append(b)
    return result


def func(*args, **kwargs):
    print(args, kwargs, sep='\n')


# print(fib1(1000000))
func(1, 2, 3, k=3, r=5)


# print(0, end=' ')
# for i in fib(10000000):
#     print(i, end=' ')
