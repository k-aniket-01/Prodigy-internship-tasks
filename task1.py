def caesar_cipher(message, shift, mode):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift if mode == "encrypt" else ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            encrypted += chr(shifted)
        else:
            encrypted += char
    return encrypted

def main():
    message = input("Enter the message to encrypt or decrypt: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Enter the mode (encrypt or decrypt): ")

    if mode == "decrypt":
        shift = -shift

    result = caesar_cipher(message, shift, mode)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()