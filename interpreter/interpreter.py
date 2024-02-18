import math

# x = 0
# y = 0
# z = 0


def main():
    expression = input("Expression (x y z): ").strip()
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)
    if y == "+":
        print("{:.1f}".format(x + z))
    elif y == "-":
        print("{:.1f}".format(x - z))
    elif y == "/":
        if z == 0:
            print("diveded by zero not defined")
        else:
            print("{:.1f}".format(x / z))
    elif y == "*":
        print("{:.1f}".format(x * z))
    else:
        print("error")
    return float


main()