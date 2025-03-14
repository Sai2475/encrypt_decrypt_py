import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)

key = chars.copy()

random.shuffle(key)

print(f"chars : {chars}")
print(f"key : {key}")

