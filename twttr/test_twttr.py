from twttr import shorten


def main():
    test_lower_upper()
    test_number()
    test_punct()


def test_lower_upper():
    assert shorten("sajt") == "sjt"
    assert shorten("SAJT") == "SJT"
    assert shorten("SaJt") == "SJt"


def test_number():
    assert shorten("54j7") == "54j7"


def test_punct():
    assert shorten(".sajt!") == ".sjt!"

if __name__ == "__main__":
    main()