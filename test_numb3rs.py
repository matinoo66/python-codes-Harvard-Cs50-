from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate(r"5.4.3.2.1") == False
    assert validate(r"253.128.256") == False
    assert validate(r"128.255.132.1") == True
    assert validate(r"1") == False

def test_range():
    assert validate(r"255.255.255.254") == True
    assert validate(r"1000.25.255.255") == False
    assert validate(r"127.257.0.45") == False
    assert validate(r"127.1.950.100") == False
    assert validate(r"255.255.255.512") == False





if __name__ == "__main__":
    main()
