def is_valid(isbn):
    x = isbn.replace('-','')
    result = 0
    n = 10
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(x) != 10:
        return False
    else:

        for i in x:
            if i == "X" and x[9]== 'X':
                i = 10
            if str(i) in alpha :
                return False

            result +=(int(i)*n)
            n -=1

    if result % 11 == 0:
        return True

    else:
        return False

print(is_valid('3-598-21508-8'))
