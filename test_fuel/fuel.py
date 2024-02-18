def main():
    v = get_int("Fraction: ")
    if v <= 0.01:
        print("E")
    elif v >= 0.99:
        print("F")
    else:
        print(f"{v:.0%}")

def get_int(prompt):
    while True:
        try:
            x = input(prompt)
            split = x.split("/")
            if "/" not in x:
                raise ValueError
            a = split[0]
            b = split[1]
            a = int(a)
            b = int(b)
            if a > b:
                raise ValueError
        except(ValueError, ZeroDivisionError):
                pass
        else:
            p = a / b
            return p


main()