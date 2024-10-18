from plates import is_valid

def main():
    test_min_and_max_chars()
    test_starts_with_two_letters()
    test_number_middle()
    test_number_zero()
    test_punctuation()


def test_min_and_max_chars():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_starts_with_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False

def test_number_middle():
    assert is_valid("AAAA22") == True
    assert is_valid("AA22AA") == False


def test_number_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("PI3.4") == False
    assert is_valid("PI3!4") == False
    assert is_valid("PI I4") == False


if __name__ == "__main__":
    main()

