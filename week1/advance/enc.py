def sub_140001EB0(_a1, _a2):
    a1 = 0
    a2 = 0
    a3 = len(_a2)

    aAbcdefghijklmn = b'abcdefghijklmnopqrstuvwxyz0123456789+/ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    v11 = 0

    v3 = 0
    v4 = a3 - 2
    # index
    v5 = a2;
    v6 = a1;
    v7 = a1;

    if v4 > 0:
        v8 = a2 + 1
        v9 = (((v4 - 1) * 0xAAAAAAAAAAAAAAAB >> 64) >> 1) + 1
        v3 = 3 * v9
        #
        v10 = _a2[v8 - 1]
        v8 += 3
        _a1[v7] = aAbcdefghijklmn[v10 >> 2]
        _a1[v7+1] = aAbcdefghijklmn[(_a2[v8-3] >> 4) | 16 * (_a2[v8-4] & 3)]
        _a1[v7+2] = aAbcdefghijklmn[4 * (_a2[v8-3] & 0xF) | (_a2[v8-2] >> 6)]
        _a1[v7+3] = aAbcdefghijklmn[_a2[v8-2] & 0x3F]
        v7 += 4
        v9 -= 1
        while v9:
            v10 = _a2[v8 - 1]
            v8 += 3
            _a1[v7] = aAbcdefghijklmn[v10 >> 2]
            _a1[v7+1] = aAbcdefghijklmn[(_a2[v8-3] >> 4) | 16 * (_a2[v8-4] & 3)]
            _a1[v7+2] = aAbcdefghijklmn[4 * (_a2[v8-3] & 0xF) | (_a2[v8-2] >> 6)]
            _a1[v7+3] = aAbcdefghijklmn[_a2[v8-2] & 0x3F]
            v7 += 4
            v9 -= 1

        if v3 < a3:
            _a1[v7] = aAbcdefghijklmn[_a2[v3 + v5] >> 2]
            if v3 == a3 - 1:
                v11 = 61
                _a1[v7+1] = aAbcdefghijklmn[16 * (_a2[v3 + v5] & 3)]
            else:
                _a1[v7+1] = aAbcdefghijklmn[(_a2[v5 + v3 + 1] >> 4) | 16 * (_a2[v3 + v5] & 3)]
                v11 = aAbcdefghijklmn[4 * (_a2[v5 + v3 + 1] & 0xF)]
            
            _a1[v7+2] = v11;
            _a1[v7+3] = 61;
            v7 += 4;

        _a1[v7] = 0;
        return v7 - v6 + 1;


if __name__ == "__main__":
    import string

    my_base64chars  = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
    std_base64chars = 'abcdefghijklmnopqrstuvwxyz0123456789+/ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    import base64
    s = "0g371wvVy9qPztz7xQ+PxNuKxQv74B/5n/zwuPfX"
    s = s.translate(s.maketrans(my_base64chars, std_base64chars))
    data = base64.b64decode(s.encode())
    print(data)