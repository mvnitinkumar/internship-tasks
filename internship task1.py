def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result
if __name__ == "__main__":
    print("Caesar Cipher Tool")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode! Please choose 'encrypt' or 'decrypt'.")
    else:
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))
        result = caesar_cipher(text, shift, mode)
        print(f"Result ({mode}ed text): {result}")
