#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hashlib import md5

flag = b''

# assert flag.startswith(b'hgame) and flag.endswith(b')

class notRC4:
    def __init__(self):
        self.S = [0] * 256
        for i in range(256):
            self.S[i] = i
        # self.S = [0,1,2,3,4,5,6,...,255]
        self._i = 0
        self._j = 0
        self.T = [0] * 256

    def KSA(self, K):
        l = len(K)         #  8
        for i in range(256):
            self.T[i] = K[i%l]
        # self.T = K * 32
        for i in range(256):
            self._j = ( self._j + self.S[i] + self.T[i] ) % 256
            # swap
            self.S[i], self.S[self._j] = self.S[self._j], self.S[i]
        self._i = self._j = 0

    def PRGA(self, length):
        O = []
        for _ in range(length):
            self._i = ( self._i + 1 ) % 256
            self._j = ( self._j + self.S[self._i] ) % 256
            self.S[self._i], self.S[self._j] = self.S[self._j], self.S[self._i]
            t = ( self.S[self._i] + self.S[self._j] ) % 256
            O.append( self.S[t] )
        print(self.S)
        return O

def enc(msg):
    X = notRC4()
    X.KSA( md5(msg).digest()[:8] )
    R = X.PRGA( len(msg) )
    return xor(msg, R)

# print( enc(flag) )


def xor(s1, s2):
    return bytes(map( (lambda x: x[0]^x[1]), zip(s1, s2) ))


sBox = [219, 96, 199, 216, 68, 104, 66, 149, 157, 180, 15, 106, 225, 2, 245, 126, 218, 130, 67, 1, 117, 127, 37, 60, 78, 236, 38, 16, 217, 107, 173, 46, 194, 211, 204, 124, 65, 14, 85, 227, 110, 244, 249, 220, 97, 241, 19, 143, 251, 49, 252, 152, 45, 36, 129, 34, 237, 54, 174, 48, 183, 12, 71, 209, 9, 56, 231, 188, 153, 86, 98, 178, 73, 135, 3, 95, 43, 77, 40, 84, 223, 72, 89, 101, 42, 248, 166, 120, 138, 91, 160, 198, 203, 28, 247, 123, 41, 132, 139, 133, 147, 235, 207, 62, 151, 87, 51, 136, 0, 169, 102, 27, 170, 100, 39, 99, 134, 242, 61, 184, 64, 25, 21, 116, 243, 11, 221, 176, 35, 18, 215, 53, 88, 20, 163, 59, 125, 190, 4, 197, 32, 195, 212, 17, 191, 144, 145, 80, 108, 5, 103, 214, 142, 161, 93, 201, 140, 7, 79, 187, 192, 50, 205, 69, 22, 200, 111, 232, 185, 239, 70, 94, 228, 105, 229, 206, 24, 148, 168, 165, 23, 181, 10, 213, 238, 119, 122, 115, 155, 112, 141, 233, 175, 109, 113, 75, 8, 172, 230, 47, 162, 58, 208, 159, 210, 158, 226, 83, 246, 44, 193, 90, 29, 240, 179, 52, 63, 57, 254, 74, 222, 156, 82, 30, 114, 182, 255, 186, 150, 118, 146, 81, 224, 189, 202, 164, 121, 55, 177, 167, 137, 234, 33, 31, 131, 92, 6, 13, 250, 76, 128, 171, 196, 26, 253, 154]
cipher = b"^{\xafsjg\xc9%}\xae\xff\xb4\xf1\xde\x83m\xbe\x18r\xbe\x19'\x1d|\x7f2j\xb9^\xc7\xcd+\x9b9\xd5\xe5\xba8\xe2\x11\x92\x02\xd2E\x1fZIz*\x15"


from copy import deepcopy

def f(S, i, j, l):
    O = []
    for _ in range(l):
        t = ( S[i] + S[j] ) % 256
        O.append( S[t] )
        S[i], S[j] = S[j], S[i]
        j = ( j - S[i] ) % 256
        i = ( i - 1 ) % 256
    O.reverse()
    return O

for i in range(256):
    for j in range(256):
        s = deepcopy(sBox)
        o = f(s, i, j, len(cipher))
        m = xor(cipher, o)
        if b'hgame{' in m:
            print(m)
            exit(0)
    
    

