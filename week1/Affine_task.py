#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gmpy2
#from secret import A, B, flag
A = 13
B = 14

flag = 'hgame{xr1A_J7ha_vG_TpH410}'

assert flag.startswith('hgame{') and flag.endswith('}')

TABLE = 'zxcvbnmasdfghjklqwertyuiop1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
MOD = len(TABLE)
print("MOD length: ", MOD)

cipher = ''
for b in flag:
    i = TABLE.find(b)
    if i == -1:
        cipher += b
    else:
        ii = (A*i + B) % MOD # 62
        cipher += TABLE[ii]

print(cipher)
# A8I5z{xr1A_J7ha_vG_TpH410}

def e(A, B):
    cipher = ''
    for b in flag[:6]:
        i = TABLE.find(b)
        if i == -1:
            cipher += b
        else:
            ii = (A*i + B) % MOD
            cipher += TABLE[ii]
    return cipher

def d(A, B):
    for t in 'A8I5z{xr1A_J7ha_vG_TpH410}':
        if not t in TABLE:
            print(t, end='')
        else:
            for i in range(len(TABLE)):
                if TABLE[(A*i + B) % MOD] == t:
                    print(TABLE[i], end='')
                    break
        

def main():
    d(A,B)

main()

