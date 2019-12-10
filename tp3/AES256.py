from Crypto.Cipher import AES
from password import *

CRYPTO_FILE = "crypto.csv"

def crypto(password, data) :
    key = password.encode()
    cipher = AES.new(key, AES.MODE_EAX)

    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())

    return ciphertext, tag, nonce

def decrypt(password, ciphertext, tag, nonce) : 
    key = password.encode()
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        print("The message is authentic:", plaintext.decode())
    except ValueError:
        print("Key incorrect or message corrupted")

def save_crypto(login, hashpassword) :
    with open(CRYPTO_FILE, mode='a') as employee_file:
        #employee_writer = csv.writer(employee_file, delimiter=';', lineterminator="\n")
        #employee_writer.writerow([login, hashpassword])

password = 'Sixteen byte key'
data = "Hello, I m Rémi and I like chocolate."

ciphertext, tag, nonce = crypto(password, data)
decrypt(password, ciphertext, tag, nonce)

# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html