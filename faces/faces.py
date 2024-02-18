import string


def main():
    user_input = input("Hi!: ")
    for r in ((":)", "🙂"), (":(", "🙁")):
        user_input = user_input.replace(*r)
    print(user_input)


main()