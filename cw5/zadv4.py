import operator
ops = {'+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.div,
       '^':operator.pow,
       }

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def calculate(equation):
    stack = []
    result = 0
    for i in equation:
        if is_number(i):
            stack.insert(0,i)
        else:
            if len(stack) < 2:
                print ('Error: insufficient values in expression')
                break
            else:
                print (f'stack: {stack}')
                if len(i) == 1:
                    n1 = float(stack.pop(1))
                    n2 = float(stack.pop(0))
                    result = ops[i](n1,n2)
                    stack.insert(0,str(result))
                else:
                    n1 = float(stack.pop(0))
                    result = ops[i](n1)
                    stack.insert(0,str(result))
    return result

def main():
    running = True
    while running:
        equation = input('enter the equation: ').split(' ')
        answer = calculate(equation)
        print (f'RESULT: {answer}')
        again = input('\nEnter another? ')[0].upper()
        if again != 'Y':
            running = False

if __name__ == '__main__':
    main()