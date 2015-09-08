from math import log

ALPHABET = "abcdfghjklmnpqrstvwxyz0123456789BCDFGHJKLMNPQRSTVWXYZ"
BASE = len(ALPHABET)
MAXLEN = 6

def encode_id(n):
    pad = MAXLEN - 1
    n = int(n + pow(BASE, pad))

    s = []
    t = int(log(n, BASE))
    while True:
        bcp = int(pow(BASE, t))
        a = int(n / bcp) % BASE
        s.append(ALPHABET[a:a+1])
        n = n - (a * bcp)
        t -= 1
        if t < 0: break

    return "".join(reversed(s))

def decode_id(n):
    try:
        n = "".join(reversed(n))
        s = 0
        l = len(n) - 1
        t = 0
        while True:
            bcpow = int(pow(BASE, l - t))
            s = s + ALPHABET.index(n[t:t+1]) * bcpow
            t += 1
            if t > l: break

        pad = MAXLEN - 1
        s = int(s - pow(BASE, pad))

        return int(s)
    except ValueError:
        return None
