'''
This script is able to generate fibonacci numbers in ~O(log(n)) (theoretically) time
the script uses a closed form derived using linear algebra, through the eigenvectors and eigenvalues of the
matrix representing the reccurence relation. 
'''
from time import time


# basic approaches
def fib_v1(n):
    '''time complexity: O(2^n)'''
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_v1(n - 1) + fib_v1(n - 2)


def fib_v2(n):
    '''time complexity: O(n)'''
    fib = [0, 1]

    if n > 1:
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])

    return fib[-1]


# approaches using eigenvalues / eigenvectors
def fib_v3(n):
    '''O(log(n)) because of square root'''
    '''fib_n = (1/sqrt(5))(((1+sqrt(5))/2)^k) - (1/sqrt(5))(((1-sqrt(5))/2)^k)'''
    return round(((1 / (5 ** 0.5)) * (((1 + (5 ** 0.5)) / 2) ** n)) - ((1 / (5 ** 0.5)) * (((1 - (5 ** 0.5)) / 2) ** n)))


def fib_v4(n):
    '''O(log(n))'''
    '''fib_n = (1/sqrt(5))(((1+sqrt(5))/2)^k)'''
    return round(((1 / (5 ** 0.5)) * (((1 + (5 ** 0.5)) / 2) ** n)))


def time_func(func, version, showOutput=True):
    start_time = time()
    output = ''

    for i in range(0, 1000):
        output += f'{func(i)}, '

    print(f'Function name: fib_v{version}')

    if showOutput:
        print(f'Output: {output}')
    print(f'Time taken: {time() - start_time}')


if __name__ == '__main__':
    # time_func(fib_v1, 1, showOutput=True)
    time_func(fib_v2, 2, showOutput=False)
    time_func(fib_v3, 3, showOutput=False)
    time_func(fib_v4, 4, showOutput=False)
