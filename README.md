# File Encryption and Decryption

This Python script allows you to securely encrypt and decrypt files using the `cryptography` module's `Fernet` symmetric encryption. The script can generate a secret key, encrypt a file, and decrypt an encrypted file using that key.

## Features
- **Generate a new secret key** for encryption.
- **Encrypt files** with the generated key.
- **Decrypt encrypted files** using the same secret key.

## Prerequisites
- Python 3.x (Recommended version: Python 3.6 or later)
- The `cryptography` library. You can install it using pip:

```bash
pip install cryptography
How to Use
1. Clone the Repository
To clone this repository, run the following command:

bash
Copy
Edit
git clone https://github.com/yourusername/file-encryption.git
2. Run the Script
Navigate to the directory where you cloned the repository, then execute the script:

bash
Copy
Edit
cd file-encryption
python file_encryption.py
3. Menu Options
The script will present you with three options:

Generate a new secret key: This will create a new key and save it as secret.key.

Encrypt a file: Encrypts a file by using the key saved in secret.key.

Decrypt a file: Decrypts an encrypted file (with .encrypted extension) using the saved key.

Example
1. Generate a new secret key
bash
Copy
Edit
1. Generate a new secret key
2. Encrypt a file
3. Decrypt a file
Enter your choice (1/2/3): 1
New secret key generated and saved as 'secret.key'.
2. Encrypt a file
bash
Copy
Edit
1. Generate a new secret key
2. Encrypt a file
3. Decrypt a file
Enter your choice (1/2/3): 2
Enter the file path to encrypt: test.txt
File encrypted successfully! Saved as test.txt.encrypted
3. Decrypt a file
bash
Copy
Edit
1. Generate a new secret key
2. Encrypt a file
3. Decrypt a file
Enter your choice (1/2/3): 3
Enter the encrypted file path to decrypt: test.txt.encrypted
File decrypted successfully! Saved as test.txt.decrypted.txt
License
This project is licensed under the MIT License - see the LICENSE file for details.

bash
Copy
Edit

### Notes:
- Be sure to replace `https://github.com/yourusername/file-encryption.git` with the actual URL of your GitHub repository.
- You can modify the "LICENSE" link to reflect the license you choose for the repository.
