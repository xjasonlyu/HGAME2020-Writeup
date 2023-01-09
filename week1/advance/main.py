
Dst = b"hgame{try_some_thing_hard}"

v0 = len(Dst)
v1 = v0

if not v0:
    print("try again")
    exit(0)


def sub_140002000(a1):
    return 4 * (((a1 + 2) * 0xAAAAAAAAAAAAAAAB >> 64) >> 1) + 1


v2 = sub_140002000(v0)
v3 = bytearray(b'\x00') * v2

import enc

enc.sub_140001EB0(v3, Dst)

print(v3)

if v3 == b"0g371wvVy9qPztz7xQ+PxNuKxQv74B/5n/zwuPfX":
    print("get it")
