import os
import pyaes
import binascii
from Crypto.Cipher import AES

KEY = os.urandom(32)
IV = os.urandom(16)
MSG = os.urandom(48)

xor = lambda x, y: bytes([ p ^ q for (p, q) in zip(x, y) ])

def encrypt(plaintext: bytes, seg=16):
    ciphertext = b''
    _shift = IV
    for i in range(0, len(plaintext), seg):
        plaintext_seg = plaintext[i:i+seg]
        blockcipher = pyaes.AES(KEY).encrypt(_shift)
        ciphertext_seg = xor(plaintext_seg, blockcipher)
        _shift = ciphertext_seg
        ciphertext += ciphertext_seg
    return ciphertext

def decrypt(ciphertext: bytes, seg=16):
    plaintext = b''
    _shift = IV
    for i in range(0, len(ciphertext), seg):
        ciphertext_seg = ciphertext[i:i+seg]
        blockcipher = pyaes.AES(KEY).encrypt(_shift)
        plaintext_seg = xor(ciphertext_seg, blockcipher)
        _shift = ciphertext_seg
        plaintext += plaintext_seg
    return plaintext

ciphertext = encrypt(MSG)
assert ciphertext == AES.new(KEY, AES.MODE_CFB, IV, segment_size=128).encrypt(MSG)
plaintext = decrypt(ciphertext)
assert plaintext == AES.new(KEY, AES.MODE_CFB, IV, segment_size=128).decrypt(ciphertext)

flag_1 = b'FLAG is hgame{51'
flag_2 = b'b72d4cd23b2fe672'
flag_3 = b''

init_seg = os.urandom(16)
# 0x00
print('*', binascii.hexlify(init_seg).decode())
_de_text_1 = binascii.unhexlify(input('1: Round 1. output> ').encode())

cipherblock_iv = xor(init_seg, _de_text_1)
flag_enc_1 = xor(flag_1, cipherblock_iv)

print('*', binascii.hexlify(flag_enc_1+init_seg).decode())
_de_text_2 = binascii.unhexlify(input('1: Round 2. output> ').encode())

cipherblock_c1 = xor(init_seg, _de_text_2[16:])
flag_enc_2 = xor(flag_2, cipherblock_c1)

print('*', binascii.hexlify(flag_enc_1+flag_enc_2+init_seg).decode())
_de_text_3 = binascii.unhexlify(input('1: Round 3. output> ').encode())

cipherblock_c2 = xor(init_seg, _de_text_3[32:])

flag_enc_3 = binascii.unhexlify(input('Flag. output> ').encode())[32:]
flag_3 = xor(cipherblock_c2, flag_enc_3) #

flag = flag_1 + flag_2 +flag_3
print(flag)
