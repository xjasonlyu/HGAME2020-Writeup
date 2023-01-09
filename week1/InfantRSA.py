#!/usr/bin/env python3

def extended_euclidean_algorithm(a, b):
    """
    extended_euclidean_algorithm(a, b)

    The result is the largest common divisor for a and b.

    :param a: integer number
    :param b: integer number
    :return:  the largest common divisor for a and b
    """

    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_euclidean_algorithm(b % a, a)
        return g, x - (b // a) * y, y


def modular_inverse(e, t):
    """
    modular_inverse(e, t)

    Counts modular multiplicative inverse for e and t.

    :param e: in this case e is a public key exponent
    :param t: and t is an Euler function
    :return:  the result of modular multiplicative inverse for e and t
    """

    g, x, y = extended_euclidean_algorithm(e, t)

    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % t
        

p = 681782737450022065655472455411
q = 675274897132088253519831953441
e = 13
n = p*q
c = 275698465082361070145173688411496311542172902608559859019841
o = (p-1)*(q-1)
d = modular_inverse(e, o)
m = pow(c, d, n)
print(m)
print(hex(256))
n = m 
b = n.to_bytes(30, 'big')
print(b)
