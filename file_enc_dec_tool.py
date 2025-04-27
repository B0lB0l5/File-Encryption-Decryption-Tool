from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename="secret.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key(filename="secret.key"):
    with open(filename, "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    output_file = file_path + ".encrypted"
    with open(output_file, "wb") as file:
        file.write(encrypted_data)
    
    print(f"File encrypted successfully! Saved as {output_file}")

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    output_file = file_path.replace(".encrypted", ".decrypted.txt")
    with open(output_file, "wb") as file:
        file.write(decrypted_data)
    
    print(f"File decrypted successfully! Saved as {output_file}")

def main():
    print("1. Generate a new secret key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        key = generate_key()
        save_key(key)
        print("New secret key generated and saved as 'secret.key'.")

    elif choice == "2":
        key = load_key()
        file_path = input("Enter the file path to encrypt: ")
        encrypt_file(file_path, key)

    elif choice == "3":
        key = load_key()
        file_path = input("Enter the encrypted file path to decrypt: ")
        decrypt_file(file_path, key)

    else:
        print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
