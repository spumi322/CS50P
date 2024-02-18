vowels = {"a": "",
          "e": "",
          "i": "",
          "o": "",
          "u": "",
          "A": "",
          "E": "",
          "I": "",
          "O": "",
          "U": ""}


def main():
    original_text = input("Input: ").strip()
    new_text = shorten(original_text)
    print(new_text)


def shorten(word):
    vowelless = ""
    for letter in word:
        if letter not in vowels:
            vowelless += letter
    return vowelless


if __name__ == "__main__":
    main()