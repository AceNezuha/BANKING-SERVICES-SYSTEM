# cryptography module
import hashlib

class Encryption:
    #constructor
    def __init__(self, password=str):
        self.password = password

    def hash(self):
        h = hashlib.sha256(self.password.encode('utf8'))
        return h.hexdigest()

# test env
if __name__ == '__main__':
    encrypt = Encryption('client456')
    print(encrypt.hash())