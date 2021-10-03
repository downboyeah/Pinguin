from math import sqrt 

def circle (r):
    "Вычисляет площадь окружности с радиусом r"
    return 3.14 * r * r

def rect (a, b):
    "Вычисляет площадь прямоугольника со сторонами a и b"
    rslt = a * b
    return rslt 

def inner_circle (a):
    "Вычисляет площать окружности, вписанной в квадрат со стороной a"
    r = a / 2
    return circle(r)

def right_triangle (a, b):
    "Вычисляет площадь прямоугольного треугольника с катетами a и b"
    return a * b / 2

def hypotenuse (a, b):
    "Вычисляет длину гипотенузы прямоугольного треугольника с катетами a и b"
    return sqrt (a**2 + b**2)

def outer_circle (x):
    "Вычисляет площадь окружности, описанной вокруг квадрата со стороной x"
    h = hypotenuse (x, x)
    r = h / 2
    rslt = circle (r)
    return rslt

def bagle (x):
    "Вычисляет площадь бублика, вокруг квадрата со стороной x"
    return outer_circle (x) - inner_circle (x)

print(circle(2))
print(circle(19))
print(circle(5))
print(rect(2,4))

print(inner_circle(4))

print(int(right_triangle(4,2)))

print(outer_circle(4))
print(outer_circle(45))
print(outer_circle(21))

print(bagle(8))