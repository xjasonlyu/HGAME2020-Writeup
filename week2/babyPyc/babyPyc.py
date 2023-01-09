import dis, base64

#patten = b'/KDq6pvN/LLq6tzM/KXq59Oh/MTqxtOTxdrqs8OoR3V1X09J'
patten = b'QpeZYrN+Wr2iUZKYcZhvjbPcf4mfyL/tjtfNxM3JR3JPZX5Q'

# def listcomp(it):
#     l = []
#     for col in it:
#         (col, )
#         def f(_it):
#             _l = []
#             for row in _it:
#                 _l.append(raw_flag[6*row+col])
#             return l
#         l.append(f(range(6)))
#     return l

def listcomp(l):
    r = []
    for i in range(6):
        _r = []
        for j in range(6):
            _r.append(i+6*j)
        r.append(_r)
    return r

def unlistcomp(l):
    r = []
    for i in range(6):
        for j in range(6):
            r.append(l[j][i])
    return r

def enc(flag):
    raw_flag = flag[6:-1]
    raw_flag = raw_flag[::-1]
    _ciphers = listcomp(raw_flag)

    for row in range(5):
        for col in range(6):
            _ciphers[row][col] += _ciphers[row+1][col]
            _ciphers[row][col] %= 256

    cipher = b''
    for row in range(6):
        col = 0
        while col < 6:
            cipher += bytes([_ciphers[row][col]])
            col += 1

    return base64.b64encode(cipher)

#print(enc(b'hgame{P~eOrGyO_~eGtpi!$8hC$Nt90O-TI!Nd5EN!}'))
#print(dis.dis(enc))

def dec():
    p = base64.b64decode(patten)
    _ciphers = [list(p[i*6:i*6+6])for i in range(6)]
    r = list(range(5)); r.reverse()
    c = list(range(6)); c.reverse()
    for row in r:
        for col in c:
            _ciphers[row][col] -= _ciphers[row+1][col]
            _ciphers[row][col] %= 256
    raw_flag = bytes(unlistcomp(_ciphers))
    
    raw_flag = raw_flag[::-1]
    print(f'hgame{{{raw_flag.decode()}}}')

dec()

# hgame{Pyth0N~OpCOde_i$-5O~!NTEre$tINGG89!!}