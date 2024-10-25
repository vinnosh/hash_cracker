import hashlib
import pyfiglet
import itertools
import string

ascii_banner = pyfiglet.figlet_format("Hash Cracker")
print(ascii_banner)
print("Algorithms available: MD5 | SHA1 | SHA224 | SHA512 | SHA384 ")

hash_type = input("What's the hash type: ").upper()
hash_value = input("Enter hash: ")

# Brute force search with words of length up to 6 characters
max_word_length = 6

found = False
for length in range(1, max_word_length + 1):
    # Generate all possible combinations of characters with the current length
    for word in itertools.product(string.ascii_lowercase, repeat=length):
        word = ''.join(word)
        # Hash the word using the specified algorithm
        if hash_type == "MD5":
            hashed = hashlib.md5(word.encode('utf-8')).hexdigest()
        elif hash_type == "SHA1":
            hashed = hashlib.sha1(word.encode('utf-8')).hexdigest()
        elif hash_type == "SHA224":
            hashed = hashlib.sha224(word.encode('utf-8')).hexdigest()
        elif hash_type == "SHA512":
            hashed = hashlib.sha512(word.encode('utf-8')).hexdigest()
        elif hash_type == "SHA384":
            hashed = hashlib.sha384(word.encode('utf-8')).hexdigest()
        else:
            print("Invalid hash type.")
            break

        # Check if the generated hash matches the provided hash
        if hash_value == hashed:
            print(f"\033[1;32mHASH FOUND: {word}\n")
            found = True
            break
    if found:
        break

if not found:
    print("Hash not found for words up to length 6.")
