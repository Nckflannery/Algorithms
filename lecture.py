#fib[1, 1, 2, 3, 5, 8, 13, 21, 34]
#num[0, 1, 2, 3, 4, 5,  6,  7,  8]


def rec_fib(n, cache={0:1, 1:1}):
    # # base cases
    # if n == 0:
    #     return 1
    # if n == 1:
    #     return 1
    if n in cache:
        return cache[n]
    else:
        cache[n] = rec_fib(n-1) + rec_fib(n-2)
        return cache[n]

# print(rec_fib(500))

# This version can run up to VERY HIGH numbers with no issues
def non_rec_fib(n):
    # base cases
    if n == 0:
        return 1
    if n == 1:
        return 1
    arr = [1,1]

    for _ in range(1, n):
        num = arr[-2]+arr[-1]
        arr.append(num)
    return num

print(non_rec_fib(5000))