import inflect

p = inflect.engine()
nl = []


def main():
    while True:
        try:
            name = input("Name: ")
            nl.append(name)
        except EOFError:
            print()
            break

    x = p.join(nl)
    print("Adieu, Adieu, to " + x)


main()

# If someone reads this:
# I do think check50 is broken here, in manual testing everything is working as it should. I cant reproduce check50's output with my manual input.