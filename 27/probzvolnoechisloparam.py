
def test(*args, **kwargs):
    print(args, kwargs)
test('lime', True, 1, 2, 3, [5, 6, 7], cat = 'Кот')






def factorial(n):
    if n == 7:
        return 2
    factorial_n_minus_7 = factorial(n=n - 1)
    return n * factorial_n_minus_7


print(factorial(8))
