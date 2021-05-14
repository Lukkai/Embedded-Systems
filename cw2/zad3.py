from os import read


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
        with open(file_name, "r") as rf:
            content = rf.read()
        print(content, "\n")
        return char_counter(content)
    except IOError:
        print("No file with provided name accessible\n")


def least_occuring(dictionary):
    return [
        min(dictionary, key=dictionary.get),
        dictionary[min(dictionary, key=dictionary.get)],
    ]


def list_min_value(num_list: list) -> dict:
    # input: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    num_list = [int(each) for each in num_list]
    min_value = min(num_list)
    id_list = [each for each in range(len(num_list)) if num_list[each] == min_value]
    print("Num list: ", num_list)
    print("min val: ", min_value)
    print("id list: ", id_list)
    return {"Min value": min_value, "Id": id_list}


while True:
    print(
        "\n1. Count manually provided set of characters \n2. Count set of characters from a file.\n3. Search for the least occuring character.\n4. End\n"
    )
    menu = input("Selected option: ")
    if menu == "1":
        chars = input("Input a set of characters: ")
        print(char_counter(chars), "\n")
        print("The first least occuring character is (char, repetitions): ", least_occuring(char_counter(chars)))
    elif menu == "2":
        read_file = input("Input file name to read from: ")
        print(file_char_counter(read_file), "\n")
        print(
            "The first least occuring character is (char, repetitions): ",
            least_occuring(file_char_counter(read_file)),
        )
    elif menu == "3":
        mstring = input("Provide a list of numbers (ex. 1, 2, 3, etc.):\n")
        string = mstring.strip("[").strip("]")
        num_list = string.split(", ")
        print(list_min_value(num_list))
    else:
        print("\nGoodbye\n")
        break