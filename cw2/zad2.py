
def char_counter(chars):
    repetition_dict = {}
    for char in chars.lower():
        if char in repetition_dict.keys():
            repetition_dict[char] += 1
        else:
            repetition_dict[char] = 1
    return repetition_dict

def file_char_counter(file_name: str) -> dict:
    try:
        with open(file_name, 'r') as rf:
            content = rf.read()
        print(content, "\n")
        return char_counter(content)
    except IOError:
        print("No file with provided name accessible\n")

while True:
    print ("\n1. Count manually provided set of characters \n2. Count set of characters from a file.\n3. End\n")
    menu = input("Selected option: ")
    if menu == '1':
        chars = input("Input a set of characters: ")
        print(char_counter(chars), "\n")
    elif menu == '2':
        read_file = input("Input file name to read from: ")
        print(file_char_counter(read_file), "\n")
    else: 
        print("End\n")
        break