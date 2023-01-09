

_a1 = bytearray(b'\x00' * 8)
_a2 = bytearray(b'33' * 8)

def f(a1, a2):
    for i in range(len(a1)):
        if a2[i*2] <= 96 or a2[i*2] > 102:
            if a2[i*2] <= 47 or a2[i*2] > 57:
                print("Illegal input!")
                exit(0)
            a1[i] = a2[i*2] - 48
        else:
            a1[i] = a2[i*2] - 87

        if a2[i*2+1] <= 96 or a2[i*2+1] > 102:
            if a2[i*2+1] <= 47 or a2[i*2+1] > 57:
                print("Illegal input!")
                exit(0)
            a1[i] = 16 * a1[i] + a2[i*2+1] - 48
        else:
            a1[i] = 16 * a1[i] + a2[i*2+1] - 87


#f(_a1, _a2)
#print(_a1)

def do():
    for c in [15, 35, 62, 99, 99, 121, 130, 210] + [102, 203, 244, 30, 203, 27, 1, 2]:
        for i in range(256):
            k = bytearray(hex(i)[2:].zfill(2).encode())
            a = [None]
            f(a, k)
            if a[0] == c:
                print(bytes(k).decode(), end='')
                break
    print()
        


do()

# [135, 33, 182, 99, 65, 81, 0, 82]
# [34, 223, 160, 10, 155, 27, 1, 70]

#v = (76, 60, -42, 54, 80, -120, 32, -52)
v = (76, 60, 214, 54, 80, 136, 32, 204)

byte_602050 = b'e4sy_Re_'
byte_602060 = b'Easylif3'


def main():

    for i in range(8):
        v14[i] = ((v14[i] & 0xE0) >> 5) | 8 * v14[i]
        v14[i] = v14[i] & 0x55 ^ ((v16[7-i] & 0xAA) >> 1) | v14[i] & 0xAA
        v16[7-i] = 2 * (v14[i] & 0x55) ^ v16[7-i] & 0xAA | v16[7-i] & 0x55
        v14[i] = v14[i] & 0x55 ^ ((v16[7-i] & 0xAA) >> 1) | v14[i] & 0xAA

    _v14 = [41, 8, -91, 79, 15, -38, 69, -109]
    _v16 = [32, 85, 0, 0, 51, 59, 3, 108]


    for j in range(8):
        # v14 = [41, 8, -91, 79, 15, -38, 69, -109]
        v14[j] ^= v[j];
        if v14[j] != byte_602050[j]:
            print("sry, wrong flag")
            exit(0);


    for k in range(8):
        # v16 = [32, 85, 0, 0, 51, 59, 3, 108]
        v16[k] ^= v14[k] ^ v[k];
        if v16[k] != byte_602060[k]:
            print("sry, wrong flag")
            exit(0);


def e(a, b):
    v14 = [a]
    v16 = [None]*7 + [b]
    i = 0
    v14[i] = ((v14[i] & 0xE0) >> 5) | 8 * v14[i]
    v14[i] = v14[i] & 0x55 ^ ((v16[7-i] & 0xAA) >> 1) | v14[i] & 0xAA
    v16[7-i] = 2 * (v14[i] & 0x55) ^ v16[7-i] & 0xAA | v16[7-i] & 0x55
    v14[i] = v14[i] & 0x55 ^ ((v16[7-i] & 0xAA) >> 1) | v14[i] & 0xAA
    return v14[0], v16[7]


def test():

    _v14 = [None] * 8
    _v16 = [None] * 8

    for j in range(8):
        _v14[j] = v[j] ^ byte_602050[j]

    for k in range(8):
        # _v16[k] = byte_602060[k] ^ (_v14[k] ^ v[k])
        _v16[k] = byte_602060[k] ^ (byte_602050[k] ^ v[k])

    print(_v14)
    print(_v16)

    # [41, 8, 165, 79, 15, 218, 69, 147]
    # [32, 85, 0, 0, 51, 59, 3, 108]

    v14 = [None] * 8
    v16 = [None] * 8

    for i in range(8):
        try:
            for j in range(256):
                for k in range(256):
                    a, b = e(j, k)
                    if a == _v14[i] and b == _v16[7-i]:
                        v14[i] = j
                        v16[7-i] = k
                        raise
            print("find nothing")
        except Exception as _e:
            #print(_e)
            continue

    print(v14)
    print(v16)

    # [135, 33, 182, 99, 65, 81, 0, 82]
    # [34, 223, 160, 10, 155, 27, 1, 70]
                    

test()