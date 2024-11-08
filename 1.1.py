from typing import Union
import pytest






def factorial(n):
    assert type(n) is int, "Złe dane"
    assert n >= 0, "Liczba nie może być ujemna!"
    assert n < 101, "Too much!"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result



def test_factorial_positiv():
    assert factorial(5)==120

def test_factorial_zero():
    assert factorial(0)==1

def text_factorial_negative():
    with pytest.raises(ValueError, match="Is negative!") as error_info:
            factorial(-5)


print(text_factorial_negative())


'''
if __name__== "__main__":
    print(factorial(5))
    try:
        print(factorial(n=-2))
    except Exception as error:
        print(error)
    try:
        print(factorial('6'))
    except Exception as error:
        print(error)
    try:
        print(factorial("6"))
    except Exception as error:
        print(error)
    try:
        print(factorial(5.5))
    except Exception as error:
        print(error)
    try:
        print(factorial(100))
    except Exception as error:
        print(error)
'''