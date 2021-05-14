from zad2 import file_char_counter


def test_zad2():
    assert file_char_counter("plik.txt") == {
        "v": 3,
        "a": 7,
        "n": 4,
        "i": 4,
        "t": 5,
        "s": 2,
        " ": 4,
        "u": 1,
        "m": 2,
        "e": 1,
        "o": 1,
    }
