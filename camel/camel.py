import inflection

def main():
    snaked = inflection.underscore(input("CamelCase: "))
    print("snake_case: " + snaked)

main()
