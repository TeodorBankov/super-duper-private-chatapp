import cryptography
from cryptography.fernet import Fernet

def generate_key():

    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():

    return open("secret.key", "rb").read()

def encrypt_message(message):

    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    return(encrypted_message)

def decrypt_message(encrypted_message):

    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    return(decrypted_message.decode())

generate_key()
x=input()
enc_msg = encrypt_message(x)
print(enc_msg)
print(decrypt_message(enc_msg))
