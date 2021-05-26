from random import choice
from string import ascii_uppercase


def random_string(length):
    letters = ascii_uppercase
    return ''.join(choice(letters) for i in range(length))


def generate_list(some_list):
    for i in range(80):
        some_list.append(random_string(5))
    return some_list


def select_key(generated_list):
    return choice(generated_list)


def generate_key(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def cipher(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)


def original_text(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)


if __name__ == '__main__':
    user_input = input("Enter a random string: ")
    sequence = []
    print(generate_list(sequence), len(sequence))
    keyword = select_key(sequence)
    print("Keyword -->", keyword, type(keyword), sequence.index(keyword))
    KEY = generate_key(user_input, keyword)
    print("KEY-->", KEY)
    text = cipher(user_input, KEY)
    print("Cipher Text: ", text)
    print("Decrypted Text", original_text(text, KEY))
