def calc(expr):
    while True:
        try:
            res = []
            for t in expr.split():
                if t in '+-*/':
                    t = str(res.pop(-2)) + t + str(res.pop())
                res.append(eval(t))
            return res[0] if res else 0
        except:
            return "Error! Blednie wprowadzone dane"

# exp = '40 4 * 3 3 - 70 +'
exp = input("RPN Calculator: ")
print(calc(exp))   # 160