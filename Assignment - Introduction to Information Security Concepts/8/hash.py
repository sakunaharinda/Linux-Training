import sys
import hashlib
import string
import secrets

def getSaltAsString(length=32):
    alpha = string.ascii_letters + string.digits
    salt = ''.join(secrets.choice(alpha) for _ in range (length))
    return salt

def getHash(password,salt):
    hashVal = hashlib.sha512((salt+password).encode())
    return hashVal.hexdigest()

if __name__ == '__main__':
    password = str(sys.argv[1])
    salt = getSaltAsString()
    print("Password entered: {}\n".format(password))
    print("salt = {}\n".format(salt))
    try:
        hash = getHash(password,salt)
        print(hash)
    except:
        print("Provide a valid password for hashing")