def nationalCode(Code):
    if len(Code) < 10 :
        raise ValueError('Input Code incorrect')
    try:
        num = list(map(int, list(Code)))[0:9]
        index_num = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        index_num.reverse()
        totals = zip(index_num, num)
        total_sum = sum([(value* key) for value,key in [(value, key) for key, value in totals]])
        if (total_sum % 11) >= 2:
            control = -(total_sum % 11) ; control += 11
            if int(Code[-1]) == int(control):
                return True
            else:
                return False
        else:
            if int(Code[-1]) == int(total_sum % 11):
                return True
            else:
                return False
    except:
        raise ValueError('Input Code incorrect')

print(nationalCode('0024848483'))
