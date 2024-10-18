from bank import value

def main():
    #calling test functions:
    test_zero()
    test_twenty()
    test_hundred()


#test return 0
def test_zero():
    assert value("hello mat") == 0
    assert value("HeLlo ") == 0
    assert value("Hello MAT") == 0

#test return 20
def test_twenty():
    assert value("hi bro") == 20
    assert value("HELL o man") == 20
    assert value("HEy") == 20


#test return 100
def test_hundred():
    assert value("yo bro") == 100
    assert value("my name is john") == 100

if __name__ == "__main__":
    main()

