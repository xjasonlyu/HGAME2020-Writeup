e = [ _ for _ in range(256) ]

def mul(a, b):
    assert len(a) == len(b)
    return [ a[_] for _ in b ]

def div_l(c, b):
    assert len(b) == len(c)
    a = [ None for _ in range(256) ]
    for i in range(256):
        a[b[i]] = c[i]
    return a

def div_r(c ,a):
    assert len(a) == len(c)
    return [ a.index(i) for i in c ]

def div(a, b):
    x = div_l(a, b)
    y = div_r(a, b)
    assert x == y
    return x

def inverse(a):
    return div_l(e, a)

def _pow(x, m):
    y = x
    m = bin(m)[3:]
    for _ in m:
        y = mul(y, y)
        if _ == '1':
            y = mul(x, y)
    return y

def _pow2(x, m):
    y = x
    m = bin(m)[3:]
    n = 1
    for _ in m:
        n *= 2
        if _ == '1':
            n +=1
    for _ in range(n-1):
        y = mul(y, x)
    return y

def test():
    import os, random
    random.seed(os.urandom(8))
    def rand_list():
        l = list(range(256))
        random.shuffle(l)
        return l
    a = rand_list()
    b = rand_list()
    c = rand_list()
    # a != b && a != c && b != c
    assert a != b and a != c and b != c
    # a * 1 = 1 * a = a
    assert mul(a, e) == mul(e, a) == a
    # (a * b) * c = a * (b * c)
    assert mul(mul(a, b), c) == mul(a, mul(b, c))
    # s = a * b
    s = mul(a, b)
    # s / b = a
    assert div_l(s, b) == a
    # s \ a = b
    assert div_r(s, a) == b
    # _a = a^-1
    _a = inverse(a)
    # _a * a = a * _a = 1
    assert mul(a, _a) == mul(_a, a) == e
    # a ^ 1024 = a * a * ... * a
    assert _pow(a, 1024) == _pow2(a, 1024)
    # x = a ^ 100 ; y = a ^ 110
    x = _pow(a, 100)
    y = _pow(a, 110)
    # y / x = y \ x = a ^ 10
    assert div_l(y, x) == div_r(y, x) == _pow(a, 10)
    # a ^ -123 * a ^ 321 = a ^ (321 - 123) = a ^ 321 - a ^ 123
    assert mul(inverse(_pow(a, 123)), _pow(a, 321))== _pow(a, 321-123) == div_l(_pow(a, 321), _pow(a, 123))

test()

# _pow(s, 595)
# _pow(s, 739)
s_595 = list(b'\xc8&\xc1E\xbe*\xc5\x84\xdb1\x05\x9b\xc0\xf2\xac/\x0b0\x8d\'\xc2b\x89\x93\xa6\xcd\xe1\x1b\xf4H\xffa\x90A\xf7,(\xea?\xa8\xa0\x8b\xf1\xf9"X\n\x86fj\x074\x7fBO\xd4F\xbd\xe6\xd9\xa7\xaf\x8a\x8c\xde\xab;!PT\x15)+w\xbc\x00>\xc6g\xc3\x85=9K\xb6<\xb7x\xaeUG\x83vk\xa9\xf6{\x03Y\x87\x14e\xfd\xed@i\xcc.\xd1\xebo\x106\xe2\xe7\xd7\xeeu\x9e\xfe\x95^R\xfb8\x04\xb4S\x16\xe0\xad\xd8\x98n\xca\xe4\xdd\xd2\xc7\x99l\xb3\\2L\xa3\x1d:_\x12\xb87\x17\x01\xb1#~q\x1c\t\xe8\xdar\xef\xcb\x0c\xe5\x80\xdf\xc9y\x0e`\xe9\x94\xd0\xcfW\x1f5\xf5h\xbf\xba\x91\xb9d\xfcM\x81\xec\x88\xb2c\x9f\xa4J|\xd3m\xd6s\xd5\x92\x9d\x9a3\xa2\xb5\xfa\x19N\xa1\x82][\xf8\x06\x13\xdcC\x1e\x1a\xaa\xc4tz\x08\x8f%$D\xbb\x97 \xce\x96V\xe3\x02I\x18\x11\x0f\r\xf3p\x8e\xa5Z-\xf0}\xb0Q\x9c')
s_739 = list(b'U\x17\x8aE\xa6\x19\xab\x7fd0\xd2)\xc0\xae\xcc/G_\xe3\'\r\xfb\xaf\x00\xb1hgi-\xc1\xffa\x8d\t&\x99k\x95\x93\xa8.\x07\xcd\x87\x01\xe8\x89\x86\xf6f48F\xdc\x96\xd4`P\xd6!\xfe\xc4B:\xd31C\x9f\x1dT{2c9\x0bY5#\xf7\xb8H\xe0Db\xb6wv\xe1\xbbI\x8f\x83l\x80\xa9\x04q\x03\xf0m\xf4\x1bp\x8e\xc6u\xfd\x16$\x06\xf9Z\xec\xa2\xcb\xd7V\xb9\xd1\xbdt^\xe7\xe2\xac\x18\xb4\x15=n\xad\xd8S+\xca\xeb\xdd\xd0;\x84\xe6\x08\x8c3\xb3\x90\x02\xc8}\xee\xea7K\x98\xde\x8b~\xcf\xfa\x11\n\xda\xa4L\xa3\x0cWQ\xdf\xc9yj\x9d\xe9\xfcJO\x1a\x1f\xdb\xf5M\xbf\x9e e\x1c*\x9b\x85\xe5\x88\xb2\xc7\xf2\x91\x10\x0e,\xd9<s\xd5\xef\xb0@|\xc3\xbc(\xb5"\xa1\x82\xa7[\xf8A\x13\x14\xc2\x1eN\xaao\xedr\xba\xcex]\x92\x05\x97\x12\xc5%\\\xb7>R\x9a\x94\x0fX\xf3\xbe?\xa5\xe4\xa0z\xf16\x81\x9c')

s_144 = div(s_739, s_595)
s_163 = div(s_595, _pow(s_144, 3))
s_19 = div(s_595, _pow(s_144, 4))
s_11 = div(s_163, _pow(s_19, 8))
s_8 = div(s_19, s_11)
s_3 = div(s_739, _pow(s_8, 92))
s_2 = div(s_739, _pow(s_11, 67))
s = div(s_3, s_2)
assert _pow(s, 595) == s_595

f = list(b"\\-\xa5{\xb9\x85J @\xfa\x91\x0b\x88\r4I\x7f\xb9\xe5\r\xc0\x84\x8f\xa6\xc0i\xb0\xa4\x1b\x8fIw\x84'\xa2\xa4\x00\x91\x87\x10\r\\\x8c\x12")
flag = bytes([ s.index(_) for _ in f ])
print(flag.decode())
