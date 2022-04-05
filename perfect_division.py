from math import sqrt


def div(number_to_check):
    for i in range(1, number_to_check):
        if number_to_check % i == 0:
            yield i


def check_for_perfection(number_to_check):
    Sum = 0
    generator = div(number_to_check)
    for number in generator:
        Sum += number
        if Sum > number_to_check:
            return False
        elif Sum == number_to_check:
            return number_to_check


num = 1

while 1:  # check for all numbers
    is_perfect = check_for_perfection(num)
    if is_perfect == num:
        print(is_perfect)
    num += 1

