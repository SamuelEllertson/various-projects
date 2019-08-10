import random


def modulus():
    modulus = int(raw_input("What is the modulus?: "))
    return modulus


def generator():
    generator = int(raw_input("What is your generator?: "))
    return generator


def pri_key():
    pri_key = int(raw_input("What is your Private Key?: "))
    return pri_key


def gen_and_disp_pub(generator, modulus, private):
    pub_key = generator ** private % modulus
    print "Here is your public key, Give this to the other party: %d" % pub_key


def ask_other_pub_key():
    other_pub_key = int(raw_input("What is the other parties public key?: "))
    return other_pub_key


def gen_secret(public, private, mod):
    secret = public ** private % mod
    print "\n Your shared key is: %d \n" % secret
    return secret


def manual():
    gen = generator()
    mod = modulus()
    prikey = pri_key()
    gen_and_disp_pub(gen, mod, prikey)
    other_pub_key = ask_other_pub_key()
    key = gen_secret(other_pub_key, prikey, mod)



def auto():
    gen = 3
    mod = 11577935946919
    prikey = random.randint(500, 90000)
    gen_and_disp_pub(gen, mod, prikey)
    other_pub_key = ask_other_pub_key()
    key = gen_secret(other_pub_key, prikey, mod)


### Here ends diffie hellman key exchange code


###Here starts encryption code

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
}


def to_numbers(plaintext):
    char_list = []
    pre_cipher = ""
    for char in plaintext:
        char_list.append(char)
    for index in range(len(char_list)):
        char_list[index] = str(char_num_dict[char_list[index]])
    for number in char_list:
        pre_cipher = pre_cipher + number
    return pre_cipher


def mult_cipher(pre_cipher, key):
    cipher = int(pre_cipher) * int(key)
    return cipher


def encrypt():
    plaintext = raw_input("Type what you want to encrypt (a-z, 0-9, space, ,.?)").lower()
    key = int(raw_input("What is the key?: "))
    print ""
    print "Encrypted text: ", mult_cipher(to_numbers(plaintext), key)
    print ""


###Here ends encryption code

###Here starts decryption code

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
}


def divide_cipher(cipher, key):
    number_text = cipher / key
    return number_text


def number_to_list(number_text):
    number_list = []
    number_text = str(number_text)
    for i in range(0, len(number_text), 2):
        number_list.append(number_text[i:i+2])
    for i in range(0, len(number_list)):
        number_list[i] = int(number_list[i])
    return number_list


def to_letters(number_list):
    plaintext = ""
    for number in number_list:
        plaintext = plaintext + num_char_dict[number]
    return plaintext


def decrypt():
    text = to_letters(number_to_list(divide_cipher(int(raw_input("Paste encrypted code: ")), int(raw_input("What is the key?: ")))))
    print ""
    print "Decrypted text: ", text
    print ""

while True:
    print "Options: \n 1) Generate key (Manual) \n 2) Generate key (Auto) \n 3) Encrypt text  \n 4) Decrypt text"
    decision = int(raw_input("Select a number: "))
    if decision == 1:
        manual()
    elif decision == 2:
        auto()
    elif decision == 3:
        encrypt()
    elif decision == 4:
        decrypt()
    else:
        print "Invalid Input"
