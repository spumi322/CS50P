import random


def main():
    input_int = get_level("Level: ")
    r = 1
    s = 0
    t = 0
    for r in range(10):
        x = generate_integer(input_int)
        y = generate_integer(input_int)
        while True:
            z = input(f"{x} + {y} = ")
            if z == str(x + y):
                r += 1
                s += 1
                break
            elif z != str(x + y):
                while t in range(2):
                    t += 1
                    print("EEE")
                    break
                else:
                    r += 1
                    print(f"{x} + {y} = {x + y}")
                    break
            else:
                r += 1
                print("EEE")
                continue
    print(f"Score: {s}")


def get_level(prompt):
    while True:
        try:
            n = input(prompt)
            n = int(n)
            if n == 1 or n == 2 or n == 3:
                return n
            else:
                raise ValueError
        except ValueError:
            pass

def generate_integer(level):
    m = random.randrange(0, ((10 ** level) - 1))
    return m


if __name__ == "__main__":
    main()