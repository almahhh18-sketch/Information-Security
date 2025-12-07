 MULTIPLICATIVE CIPHER – المشفّر الجدائي

import math
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def mod_inv(a, m):
    for x in range(m):
        if (a * x) % m == 1:
            return x
    raise ValueError("لا يوجد معكوس ضربي")


 --- التشفير ---
def multiplicative_encrypt(text, key):
    if math.gcd(key, 26) != 1:
        raise ValueError("المفتاح غير صالح")
    text = "".join([c for c in text.upper() if c.isalpha()])
    return "".join([ALPHABET[(ALPHABET.index(c) * key) % 26] for c in text])


--- فك_التشفير ---
def multiplicative_decrypt(text, key):
    inv = mod_inv(key, 26)
    text = "".join([c for c in text.upper() if c.isalpha()])
    return "".join([ALPHABET[(ALPHABET.index(c) * inv) % 26] for c in text])

--- الهجوم_الأعمى ---
def multiplicative_bruteforce(cipher):
    cipher = "".join([c for c in cipher.upper() if c.isalpha()])
    results = {}
    for k in range(1, 26):
        if math.gcd(k, 26) == 1:
            results[k] = multiplicative_decrypt(cipher, k)
    return results
