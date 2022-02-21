import math


def count_roots(a, b, c):
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    d = b ** 2 - 4 * a * c
    if d > 0:
        print("There are 2 roots")
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("x1 = %.1f \nx2 = %.1f" % (x1, x2))
    elif d == 0:
        print("There is 1 root")
        x = -b / (2 * a)
        print("x = %.1f" % x)
    else:
        print("There are 0 roots")
