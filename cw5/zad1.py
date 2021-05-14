#Kalkulator RPN (Odwrotna notyfikacja polska) - Laboratorium 5
import operator
oper={'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
dzialac= True
print("Kalkulator w RPN. Program można zakończyć podając samą \".\" na wejscie.")
while dzialac:
    try:
        stack=[]
        for x in str.split(input()):
            if x in oper:
                a=stack.pop()
                b=stack.pop()
                c=oper[x](b,a)
            elif x==".":
                dzialac=False
                print("Koniec dzialania programu.")
                break
            else:
                c=float(x)
            stack.append(c)
        assert len(stack) <=1
        if len(stack)==1:
            print(stack.pop())
    except EOFError:
        break
    except:
        print("Cos nie dziala")