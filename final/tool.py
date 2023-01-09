
import binascii


def _print(promot, msg):
    print('\n'+binascii.hexlify(msg).decode()+'\n')

xor = lambda p, q: bytes(x^y for x,y in zip(p,q))


# >>> b'0000000000'
plaintext_0_suffix = b'0'*10
_print('>>>', plaintext_0_suffix)

####
r0 = input('>>> ').encode()
r0 = binascii.unhexlify(r0)


_print('>>>', r0)

iv = r0[:16]

text = b'Alice'+b'\x00'*11
x1 = xor(iv, text)

r0c0 = r0[16:32]
plaintext_1 = xor(r0c0, x1)

# >>>
_print('>>>', plaintext_0_suffix + plaintext_1 + b'')


#####
r1 = input('>>> ').encode()
r1 = binascii.unhexlify(r1)

_print('>>>', iv + r1[32:48])

#####
challenge2 = input('>>> ').encode()
challenge2 = binascii.unhexlify(challenge2)


_print('>>>', iv + r1[32:48] + xor(x1, challenge2) + r1[32:48])
