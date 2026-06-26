message = input("Enter text to encrypt: ")

key = 5

encrypted = ""

for char in message:
    encrypted += chr(ord(char) + key)

print("Encrypted Text:", encrypted)

decrypted = ""

for char in encrypted:
    decrypted += chr(ord(char) - key)

print("Decrypted Text:", decrypted)