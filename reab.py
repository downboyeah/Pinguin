def arithmetic (a, b, op):
    if op == "+": 
        return a + b
    elif op == "-":
        return a - b
    elif op == "/":
        return a / b
    elif op == "*":
        return a * b
    else:
        return "неизвестная операция"

def calc (a, b, op):
    p = arithmetic(a, b, op)
    print(str(a) + " " + op  + " " + str(b) + " = " + str(p))


calc(2, 4, "+")
calc(5, 7, "+")
calc(3, 108, "*")
calc(6, 17, "*")
calc (12, 13, "/")
calc(13, 14, "*")
calc(168, 56, "-")
calc(567, 456, " ")
calc(12345, 768, "-")
calc(-673, -346, "-")