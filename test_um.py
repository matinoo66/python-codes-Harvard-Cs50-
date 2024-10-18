from um import count

def main():
    test_upper_lower()
    test_word_um()
    test_space_um()

def test_upper_lower():
    assert count('Um, give me umbrella') == 1
    assert count('uM, tnx for um album') == 2

def test_word_um():
    assert count('yummi') == 0



def test_space_um():
    assert count('say Hellloo , um to umworld') == 1
    assert count('um?') == 1




if __name__ == "__main__":
    main()

