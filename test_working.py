from working import convert
import pytest

def main():
    test_syn()
    test_time()
    test_hour()
    test_minutes()

def test_syn():

    with pytest.raises(ValueError):
        convert("9 Am - 5 PM")

def test_time():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_hour():
    with pytest.raises(ValueError):
       convert("18 AM to 12 PM")

def test_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:30 PM")



if __name__ == "__main__":
    main()
