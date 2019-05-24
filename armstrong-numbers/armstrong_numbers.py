def is_armstrong_number(number):

    sum = 0
    counted = len(str(number))

    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** counted
        temp //= 10

    if sum == number:
        return True
    else:
        return False

is_armstrong_number(153)