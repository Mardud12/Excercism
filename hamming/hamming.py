def distance(strand_a, strand_b):

    #a = list(strand_a)
    #b = list(strand_b)
    x = 0
    y = 0

    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must contain the same amout of letters or any!')

    while True:

        try:

            if strand_a[x] == strand_b[x]:
                x +=1

            if strand_a[x] != strand_b[x]:
                y += 1
                x += 1

        except:
            break
    return y

print(distance('ABC', 'BCA'))