from Crypto.PublicKey import RSA  # https://m.habr.com/ru/post/265309/?mobile=yes
from Crypto.Cipher import PKCS1_OAEP
import os

# TODO: Tests
gDefaultPath = ".store/"
gPubFilePath = os.getenv("HOME") + "/.ssh/id_rsa.pub"
gPrivFilePath = os.getenv("HOME") + '/.ssh/id_rsa'


def storedata(aName, aData, aPath=gDefaultPath, aPubFilePath=gPubFilePath):
    '''
    Save data to store. If type(aData) != bytes, aData will be serialized in string
    :param aName: name of file to save
    :param aData: data to save
    :param aPath: path to save
    :param aPubFilePath: path to public key
    :return: True, if data saved
    '''
    fn_pub = aPubFilePath
    key_pub = None
    with open(fn_pub, 'rb') as pub:
        key_pub = RSA.importKey(pub.read())

    if key_pub is None:
        return False

    encryptor = PKCS1_OAEP.new(key_pub)

    lData = aData if str(type(aData)) == "<class 'bytes'>" else str(aData).encode("utf-8")
    encrypted = encryptor.encrypt(lData)

    if not os.path.isdir(aPath):
        os.mkdir(aPath)

    with open(aPath + aName, 'wb') as file:
        file.write(encrypted)

    return True


def getdata(aName, aPath=gDefaultPath, aPrivFilePath=gPrivFilePath):
    '''
    Checking and loading saved data.
    :param aName: name of file to load
    :param aPath: path to load
    :param aPrivFilePath: path to private key
    :return: 'bytes' with stored data, or None if data absent
    '''
    if not os.path.isfile(aPath+aName):
        return None

    fn_priv = aPrivFilePath
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
