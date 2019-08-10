import math

# Padding scheme code


char_num_dict = {
    "a": 41,
    "b": 42,
    "c": 43,
    "d": 44,
    "e": 45,
    "f": 46,
    "g": 47,
    "h": 48,
    "i": 49,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "0": 27,
    "1": 28,
    "2": 29,
    "3": 30,
    "4": 31,
    "5": 32,
    "6": 33,
    "7": 34,
    "8": 35,
    "9": 36,
    ".": 37,
    ",": 38,
    "?": 39,
    " ": 40,
    "&": 57,
}


num_char_dict = {
    41: "a",
    42: "b",
    43: "c",
    44: "d",
    45: "e",
    46: "f",
    47: "g",
    48: "h",
    49: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z",
    27: "0",
    28: "1",
    29: "2",
    30: "3",
    31: "4",
    32: "5",
    33: "6",
    34: "7",
    35: "8",
    36: "9",
    37: ".",
    38: ",",
    39: "?",
    40: " ",
    57: "&",
}


def add_length_to_message(message):
    while len(message) <= 30:
        message += "&"
    return message


def convert_to_numbers(message):
    char_list = []
    number_message = ""
    for char in message:
        char_list.append(char)
    for index in range(len(char_list)):
        char_list[index] = str(char_num_dict[char_list[index]])
    for number in char_list:
        number_message = number_message + number
    return number_message


def pad(text):
    lengthy_message = add_length_to_message(text)
    number_message = convert_to_numbers(lengthy_message)
    return int(number_message)


# de-padding scheme code


def convert_to_int_list(integer_message):
    number_list = []
    integer_message = str(integer_message)
    for i in range(0, len(integer_message), 2):
        number_list.append(integer_message[i:i+2])
    for i in range(0, len(number_list)):
        number_list[i] = int(number_list[i])
    return number_list


def convert_to_letters(number_list):
    plaintext = ""
    for number in number_list:
        plaintext = plaintext + num_char_dict[number]
    return plaintext


def remove_padding(str_with_57):
    plaintext = str_with_57.strip("&")
    return plaintext


def depad(padded_int):
    int_list = convert_to_int_list(padded_int)
    text_with_57 = convert_to_letters(int_list)
    plaintext = remove_padding(text_with_57)
    return plaintext

# end of padding scheme code

# RSA code


def encrypt():
    message = raw_input("Type what you want to encrypt: ").lower()
    if len(message) > 39:
        print "Message is too long (Max 39 Characters)"
        encrypt()
    elif message == "back":
        print ""
        pass
    else:
        integer = pad(message)
        ciphertext = pow(integer, 65537, 8019221400289369533604671985093874382300917269080749790505537409538611066319607)
        print ""
        print "Encrypted text:", ciphertext
        print ""


def decrypt():
    ciphertext = (raw_input("Type what you want to decrypt: "))
    if ciphertext == "back":
        pass
    else:
        ciphertext = int(ciphertext)
        padded_message = pow(ciphertext, 7154858063977406834886097227620751932940881206527700150157047995998517320015873, 8019221400289369533604671985093874382300917269080749790505537409538611066319607)
        plaintext = depad(padded_message)
        print ""
        print "Decrypted text:", plaintext
        print ""

print "Welcome to RSA hub"
print ""
while True:
    print "Options: \n 1) Encrypt text  \n 2) Decrypt text"
    decision = (raw_input("Select a number: "))
    if decision == "1":
        encrypt()
    elif decision == "2":
        decrypt()
    else:
        print "Invalid Input"
