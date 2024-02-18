from plates import is_valid


def main():
    test_punctuation()
    test_length()
    test_starting_letters()
    test_middle_numbers()
    test_first_number_zero()
    test_valid()


def test_punctuation():
    assert is_valid("AA!BB?") == False


def test_length():
    assert is_valid("ABCDEFG") == False
    assert is_valid("A") == False


def test_starting_letters():
    assert is_valid("12ABCD") == False


def test_middle_numbers():
    assert is_valid("AAA11A") == False


def test_first_number_zero():
    assert is_valid("AAA011") == False


def test_valid():
    assert is_valid("ABCDEF") == True



if __name__ == "__main__":
    main()