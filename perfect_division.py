# function to find factorial of number
def find_factorial_numbers(number_to_check):
    for index in range(1, int((number_to_check / 2)) + 1):
        if number_to_check % index == 0:
            yield index


# function check if the sum of the divisors are making the perfect division
def check_for_perfection(number_to_check):
    sum_of_factors = 0
    factors_generator = find_factorial_numbers(number_to_check)
    for number in factors_generator:
        sum_of_factors += number
    return sum_of_factors == number_to_check


if __name__ == '__main__':
    number_to_check = 1
    while 1:  # check for all numbers
        if check_for_perfection(number_to_check):
            print(number_to_check)
        number_to_check += 1 # next number
