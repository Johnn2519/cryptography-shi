def encode(message, key, symbols="abcdefghijklmnopqrstuvwxyz"):
    sub_message = ""
    for letter in message:
        if letter in key:
            sub_message += key[symbols.index(letter)]
        else:
            sub_message += letter
    return sub_message

def decode(message, key, symbols="abcdefghijklmnopqrstuvwxyz"):
    return encode(message, symbols, key)

if __name__ == "__main__":
    key = "zyxwvutsrqponmlkjihgfedcba"
    code = encode("this is a secret message", key)
    print(code)
    print(decode(code, key))