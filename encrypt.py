import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#encrypt text
def encrypt(plain_text):
    cipher_text = ""
    for letter in plain_text:
        if letter in chars:
            index = chars.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter  # Preserve unknown characters
    return cipher_text

#decrypt text
def decrypt(cipher_text):
    plain_text = ""
    for letter in cipher_text:
        if letter in key:
            index = key.index(letter)
            plain_text += chars[index]
        else:
            plain_text += letter  # Preserve unknown characters
    return plain_text
