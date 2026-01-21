def caesar_cipher(text, shift, mode):
    if mode == "decrypt":
        shift = -shift

    result = ""

    for char in text:
        if char.islower():
            start = ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char

        elif char.isupper():
            start = ord('A')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char

        else:
            result += char

    return result


message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Type 'encrypt' or 'decrypt': ").lower()

shift = shift % 26
result = caesar_cipher(message, shift, mode)
print("Result:", result)

