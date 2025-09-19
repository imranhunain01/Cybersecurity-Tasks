# Author: Hunain Imran
# Task 01
# Prodigy InfoTech

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)

print("=== Welcome to Caesar Cipher Tool ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Do you want to Encrypt (E) or Decrypt (D)? ").upper()

if choice == "E":
    encrypted = encrypt(message, shift)
    print("Encrypted message:", encrypted)
elif choice == "D":
    decrypted = decrypt(message, shift)
    print("Decrypted message:", decrypted)
else:
    print("Invalid choice! Please enter E or D.")
