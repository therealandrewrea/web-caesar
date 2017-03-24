def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    num = letter.lower()
    if num not in alphabet:
        return letter
    return alphabet.index(num)

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char not in alphabet: #corrected non char error on line 11
        return char
    char_pos = alphabet_position(char)
    new_char = char_pos + rot #new index value (correct -26 if greater than or equal to 26) #non letter character gets stuck here concatenate str and int
    if new_char >= 26:
        new_char = new_char - 26
    if char.isupper():
        return alphabet[new_char].upper()
    return alphabet[new_char]

def encrypt(text, rot):
    crypt = ""
    for let in text:
        let = rotate_character(let, rot)
        crypt = crypt + let
    return crypt
