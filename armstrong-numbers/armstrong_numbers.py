def is_armstrong_number(number):

    s = str(number)
    total = 1
    counted = s.__len__()

    for num in s:
        total += int(num)

    return total*counted
print(is_armstrong_number(153))