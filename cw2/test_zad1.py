from zad1 import char_counter

def test_zad2():
    chars = "Studentdbl"
    assert(char_counter(chars) == {'e': 1, 'd': 2, 'l': 1, 'n': 1, 's': 1, 'u': 1, 't': 2, 'b': 1})