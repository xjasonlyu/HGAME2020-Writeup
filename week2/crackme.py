import base64
import pyaes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

b64Key = b'SGc0bTNfMm8yMF9XZWVLMg=='
b64IV = b'MFB1T2g5SWxYMDU0SWN0cw=='
key = base64.b64decode(b64Key) # Hg4m3_2o20_WeeK2
iv = base64.b64decode(b64IV)   # 0PuOh9IlX054Icts

str4 = b'Same_ciphertext_'
str3_ct = b'dJntSWSPWbWocAq4yjBP5Q=='
hint_ct = b'mjdRqH4d1O8nbUYJk+wVu3AeE7ZtE9rtT/8BA8J897I='

def encrypt(key: bytes, iv: bytes, plaintext: bytes):
    _aes = pyaes.AES(key)
    precipherblock = [ (p ^ l) for (p, l) in zip(plaintext, iv) ]
    ciphertext = _aes.encrypt(precipherblock)
    return ciphertext

def decrypt(key: bytes, iv: bytes, ciphertext: bytes):
    _aes = pyaes.AES(key)
    plaintext = [ (p ^ l) for (p, l) in zip(_aes.decrypt(ciphertext), iv) ]
    return bytes(plaintext)

def calcIV(key: bytes, plaintext: bytes, ciphertext: bytes):
    _aes = pyaes.AES(key)
    iv = [ (p ^ l) for (p, l) in zip(_aes.decrypt(ciphertext), plaintext) ]
    return bytes(iv)

str2 = calcIV(key, str4, base64.b64decode(hint_ct)[:16])
ct = AES.new(key, AES.MODE_CBC, str2).encrypt(str4+b'\x10'*16)
assert base64.b64encode(ct) == hint_ct

_iv = encrypt(key, iv, str4)
str3 = decrypt(key, _iv, base64.b64decode(str3_ct))
ct = AES.new(key, AES.MODE_CBC, iv).encrypt(str4+str3)[16:]
assert base64.b64encode(ct) == str3_ct

str2 = base64.b64encode(str2)
str3 = unpad(str3, AES.block_size)

flag = f'hgame{{{str2.decode()}{str3.decode()}}}'
print(flag)