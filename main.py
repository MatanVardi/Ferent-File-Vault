from cryptography.fernet import Fernet
from hashlib import sha256, scrypt
from BytesAndInts import BytesAndInts
import hmac
import json
import os

def extension_remover(file_name : str):
    return os.path.splitext(file_name)[0]

def repeated_key_xor(plain_text: bytes, key: bytes) -> bytes:
    """
    Encrypts using OTP
    :param plain_text: The plain text
    :param key: The encryption/decryption key
    :return: ciphertext
    """
    key = scrypt(key, salt=sha256(key).digest(), n = 2048, r = 8, p = 1, dklen= 32)
    pt = plain_text
    len_key = len(key)
    encoded = []

    for i in range(0, len(pt)):
        encoded.append(pt[i] ^ key[i % len_key])
    return bytes(encoded)
key = b""
# Key Save
key_mode = input("Do you want to Sign in or create a new key?").lower()
if key_mode == "ck":

    key = Fernet.generate_key()
    key_hash = sha256(key).hexdigest()
    password_value = input("What is your password?").encode("utf-8")
    key_encrypted = repeated_key_xor(key, password_value)
    key_password_hmac = hmac.new(password_value, key_encrypted, digestmod=sha256).digest()
    print(f" {key_password_hmac.hex()} {len(key_password_hmac)}")
    key_encrypted_final = key_password_hmac + key_encrypted
    # print(key_encrypted)
    j_dict = {"key_hash" : key_hash, "key_xor" : BytesAndInts.byte2Int(key_encrypted_final)}
    with open("Key.json", "w") as key_file:
        key_file.write(json.dumps(j_dict))

elif key_mode == "si":
    with open("Key.json", "r") as key_file:
        j_dict = json.loads(key_file.read())
    key_encryption_final = BytesAndInts.int2Byte(j_dict["key_xor"])
    key_hmac = key_encryption_final[:32]
    key_encrypted = key_encryption_final[32:]
    password_value = input("What is your password?").encode("utf-8")
    key_password_hmac = hmac.new(password_value, key_encrypted, digestmod=sha256).digest()
    print(key_password_hmac.hex())
    print(key_hmac.hex())
    assert hmac.compare_digest(key_password_hmac, key_hmac)
    key_decrypted = repeated_key_xor(key_encrypted, password_value)
    assert sha256(key_decrypted).hexdigest() == j_dict["key_hash"]
    key = key_decrypted




mode = input("Do you want to encrypt or decrypt?").lower()
if mode in ["e", "encrypt"]:
    file_name = input("Enter a file name")
    with open(file_name, "rb") as file:
        contents = file.read()
    fernet_ob = Fernet(key)
    contents_encrypted = fernet_ob.encrypt(contents)
    with open(extension_remover(file_name) + "encrypted.txt", "wb") as file:
        file.write(contents_encrypted)
if mode in ["d", "decrypt"]:
    file_name = input("Enter a file name")
    with open(file_name, "rb") as file:
        contents_encrypted = file.read()
    fernet_ob = Fernet(key)
    contents = fernet_ob.decrypt(contents_encrypted)
    with open(extension_remover(file_name) + "decrypted.txt", "wb") as file:
        file.write(contents)





