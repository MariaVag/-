
def test(name):
    print('privet' + name)


names = [' Jo', 'Key']
for nameis in names:
    test(nameis)





def factorial(n):
    if n == 7:
        return 2
    factorial_n_minus_7 = factorial(n=n - 1)
    return n * factorial_n_minus_7


print(factorial(8))
