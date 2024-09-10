# Variant 1
#
# number1 = float(input('Please enter 1st number: '))
# number2 = float(input('Please enter 2nd number: '))
#
# arithmetic_mean = (number1 + number2) / 2
# geometric_mean = (number1 * number2) ** 0.5
#
# print(f'Arithmetic_mean = {arithmetic_mean}')
# print(f'Geometric_mean = {round(geometric_mean, 3)}')


# Variant 2
#
import math

number1 = float(input('Please enter 1st number: '))
number2 = float(input('Please enter 2nd number: '))


def arithmetic_mean():
    return (number1 + number2) / 2


def geometric_mean():
    return math.sqrt(number1 * number2)


print(f'Arithmetic_mean = {arithmetic_mean()}')
print(f'Geometric_mean = {round(geometric_mean(), 3)}')