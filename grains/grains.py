def square(number):
    r= 2
    x1=1
    x = 0
    l = []
    if number not in range(1,65):
        raise ValueError ("Error is out of range")
    for i in range(1,65):
        if i == 1:
             x = x1
             l.append(x)
        else:
            x *=2
            l.append(x)
    return l[number-1]

def total():

    x1 = 1
    x = 0
    l = []
    for i in range(1, 65):
        if i == 1:
            x = x1
            l.append(x)
        else:
            x *= 2
            l.append(x)
    return sum(l)
