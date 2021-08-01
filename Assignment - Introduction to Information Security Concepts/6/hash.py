import sys
import hashlib

def getHash(password):
    hashVal = hashlib.pbkdf2_hmac(hash_name='sha512',password=password, salt=b'Km5d5ivMy8iexuHcZrsD',iterations=200000)
    return hashVal.hex()

if __name__ == '__main__':
    password = bytes(str(sys.argv[1]),'utf-8')
    print("Password entered: ",password)
    try:
        hash = getHash(password)
        print(hash)
    except:
        print("Provide a valid password for hashing")