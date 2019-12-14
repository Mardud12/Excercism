def convert(number):
    result=''
    x = int(number)
    while True:

        if x%3==0:
            result += "Pling"
        if x%5==0:
            result += "Plang"
        if x%7==0:
            result += "Plong"
        if x% 3 != 0 and x%5!=0 and x%7!=0:
            result += str(number)
        break
    return result

