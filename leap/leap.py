def is_leap_year(year):
    x = int(year)
    if x%100 == 0 and x%400 !=0:
        return False
    if x%100 == 0 and x%400 == 0:
        return True
    if x%4 ==0:
        return True
    else:
        return False