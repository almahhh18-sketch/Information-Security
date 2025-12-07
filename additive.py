ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


--- التشفير ---
def additive_encrypt(text, key):
    text = "".join([c for c in text.upper() if c.isalpha()])
    return "".join([ALPHABET[(ALPHABET.index(c) + key) % 26] for c in text])


--- فك_التشفير ---
def additive_decrypt(text, key):
    text = "".join([c for c in text.upper() if c.isalpha()])
    return "".join([ALPHABET[(ALPHABET.index(c) - key) % 26] for c in text])


--- الهجوم_الأعمى ---
def additive_bruteforce(cipher):
    cipher = "".join([c for c in cipher.upper() if c.isalpha()])
    return {k: additive_decrypt(cipher, k) for k in range(26)}
