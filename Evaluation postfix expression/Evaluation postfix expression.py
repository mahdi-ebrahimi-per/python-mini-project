def isNumber(x) -> str:
    num = "0123456789"    
    flag = 0

    if len(x) == 0:
        return True if x in num else False
    
    else:
        for i in x:
            if i in num:
                flag = 1
            else:
                flag = 0

    return True if flag==1 else False


def postfix_eval(expression) -> str:
    expression = expression.split(' ')
    stack = []
    op = {"*"}

    for i in expression:
        if isNumber(i):
            stack.append(i)
        

        else:
            try:
                a, b = stack.pop(), stack.pop()
                stack.append(eval(str(b) + i + str(a)))
            except:        
                raise ValueError("input expression is incorrect!")

    if len(stack) == 1 : return stack[0]




print(postfix_eval("7 4 -3 * 1 5 + / *"))