def char_counter(chars):
    chars = chars.lower()
    repetition_dict = {}
    for char in set(chars):
        repetition_dict[char] = chars.count(char)
    return repetition_dict

# if __name__ == "__main__":
chars = input("Input a set of characters: ")
print(char_counter(chars))
