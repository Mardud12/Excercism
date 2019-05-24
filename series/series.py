def slices(series, length):
    digit = []
    start = 0
    end = length

    while True:
        if len(series)<length:
            raise ValueError("Bogus input.")
            break


        if length<=0:
            raise ValueError("Bogus input.")
            break

        x = series[start:end]
        start +=1
        end+=1

        if len(x) == length:
            digit.append(x)
        if end == len(series)+2:
            break
    return digit