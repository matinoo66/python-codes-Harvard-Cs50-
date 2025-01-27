from fuel import gauge , convert
import pytest
def main():
    test_correct_input()
    test_zero_division()
    test_value()

def test_value():
    with pytest.raises(ValueError):
        convert('cat/dog')

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_correct_input():
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('99/100') == 99 and gauge(99) == 'F'
    assert convert('1/100') == 1 and gauge(1) == 'E'



if __name__ == "__main__":
    main()
