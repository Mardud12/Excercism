def factors(value):

    l = []
    i=2
    if value <2:
        pass
    while i-1<value:
        if value%i == 0:
            l.append(i)
            value /=i
        else:
            i +=1

    return l


print(factors(12))