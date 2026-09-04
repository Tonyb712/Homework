def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char

    return result


def caesar_decipher(cyphertext, shift):
    result = ""
    
    for char in cyphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base - shift) % 26
            result += chr(base + shifted)
        else:
            result += char

    return result


def letter_frequency(text):
    freq = [0] * 26
    
    for char in text:
        if char.isalpha():
            lower = char.lower()
            index = ord(lower) - ord('a')
            freq[index] += 1
    
    return freq


print("\n=== Caesar Cipher Menu ===")
print("1. Enter a message and shift value")
print("2. Quit")

choice = input("Choose an option: ").strip()

if choice == "1":
    text = input("\nEnter your message: ")

    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            break
        except ValueError:
            print("Shift must be an integer. Try again.")

    ciphered = caesar_cipher(text, shift)
    print("\nCiphered text:")
    print(ciphered)

    freq = letter_frequency(text)
    print("\nLetter frequency (a-z):")
    for i in range(26):
        letter = chr(ord('a') + i)
        print(f"{letter}: {freq[i]}")

    deciphered = caesar_decipher(ciphered, shift)
    print("\nDeciphered text:")
    print(deciphered)

elif choice == "2":
    print("Goodbye")

else:
    print("Invalid choice. Please select 1 or 2.")
