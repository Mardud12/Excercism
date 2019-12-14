def square_of_sum(number):
    n= 0
    for i in range(1,number +1):
        n+=i
    return n**2

def sum_of_squares(number):
    n = 0
    for i in range (1, number+1):
        n += i**2
    return n


def difference_of_squares(number):
    return (abs(square_of_sum(number) - sum_of_squares(number)))
