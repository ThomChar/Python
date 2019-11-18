import hashlib, binascii, os
import csv
from tkinter import messagebox

PSEUDOS_FILE = "pseudos.csv"
PSEUDO_DEFAULT_INPUT = "Enter Username"

# hash : the simple hash of password
def hash(password) :
    hash_object = hashlib.sha512( password.encode() ).hexdigest()
    return hash_object

# pseudoIsExiste : the pseudo existe ?
def pseudoIsExiste(pseudo_search) :
    isExiste = False
    with open(PSEUDOS_FILE) as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            pseudo = row[0]
            if(pseudo == pseudo_search):
                isExiste = True
                break
    return isExiste

# getPasswordByPseudo : return the password of pseudo
def getPasswordByPseudo(pseudo_search) :
    password = None
    with open(PSEUDOS_FILE) as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            pseudo = row[0]
            if(pseudo == pseudo_search):
                password = row[1]
                break
    return password

# hash_password : hash password with salt 
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

# verify_password : verify password with hash password
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