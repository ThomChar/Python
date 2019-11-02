import hashlib, binascii, os
import csv
from tkinter import messagebox

PSEUDOS_FILE = "pseudos.csv"
PSEUDO_DEFAULT_INPUT = "Enter Username"

def hash(password) :
    hash_object = hashlib.sha512( password.encode() ).hexdigest()
    print(hash_object)
    return hash_object

def pseudoIsExiste(pseudo_search) :
    isExiste = False
    with open(PSEUDOS_FILE) as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        print("hello pseudo")
        for row in reader:
            pseudo = row[0]
            print(pseudo)
            if(pseudo == pseudo_search):
                isExiste = True
                break
    return isExiste

def checkPassword(pseudo_search, password) :
    passwordIsOk = False
    hashPassword = hash(password)
    with open(PSEUDOS_FILE) as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            pseudo = row[0]
            if(pseudo == pseudo_search and hashPassword == row[1]):
                passwordIsOk = True
                break
    return passwordIsOk










def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    print ('salt: ' + salt)
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    print ('pwdhash: ' + pwdhash)
    pwdhash = binascii.hexlify(pwdhash)
    print ('pwdhash hexlify: ' + pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password