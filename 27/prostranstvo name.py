def test_function():
    def inner_function():
        print('Я в области функции test_function')

    print('Я из области функции inner_function')
    inner_function()

test_function()