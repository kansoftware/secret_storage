from Crypto.PublicKey import RSA  # https://m.habr.com/ru/post/265309/?mobile=yes
from Crypto.Cipher import PKCS1_OAEP
import os


gDefaultPath = ".store/"
gPubFilePath = os.getenv("HOME") + "/.ssh/id_rsa.pub"
gPrivFilePath = os.getenv("HOME") + '/.ssh/id_rsa'


def storedata(aName, aData, aPath=gDefaultPath):
    fn_pub = gPubFilePath
    key_pub = None
    with open(fn_pub, 'rb') as pub:
        key_pub = RSA.importKey(pub.read())

    if key_pub is None:
        return False

    encryptor = PKCS1_OAEP.new(key_pub)
    encrypted = encryptor.encrypt(aData)

    if not os.path.isdir(aPath):
        os.mkdir(aPath)

    with open(aPath + aName, 'wb') as file:
        file.write(encrypted)

    return True


def getdata(aName, aPath=gDefaultPath):
    if not os.path.isfile(aPath+aName):
        return None

    fn_priv = gPrivFilePath
    key_priv = None
    with open(fn_priv, 'rb') as pub:
        key_priv = RSA.importKey(pub.read())

    if key_priv is None:
        return None

    with open(aPath + aName, 'rb') as file:
        encrypted = file.read()

    decryptor = PKCS1_OAEP.new(key_priv)
    decrypted = decryptor.decrypt(encrypted)

    return decrypted


if __name__ == "__main__":
    message = 'Hello Blablacode.ru!'
    storedata("message", message.encode("utf-8"))
    message1 = getdata("message")


    print(message)
    print('=' * 60)
    print(message1.decode("utf-8"))
