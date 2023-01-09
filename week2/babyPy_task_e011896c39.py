import dis

def encrypt(msg):
    a = msg[::-1]
    b = list(a)
    for i in range(1, len(b)):
        c = b[i-1] ^ b[i]
        b[i] = c
    O = bytes(b)
    return O.hex()


#print(dis.dis(encrypt))


cipher = '7d037d045717722d62114e6a5b044f2c184c3f44214c2d4a22'


def decrypt(cipher):
    b = bytes.fromhex(cipher)
    c = bytearray(b)
    for i in range(1, len(b)):
        x = b[i] ^ b[i-1]
        c[i] = x
    c.reverse()
    return c.decode()

print(decrypt(cipher))
