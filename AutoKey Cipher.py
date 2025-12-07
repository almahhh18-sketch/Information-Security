 AUTOKEY CIPHER

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lo = "abcdefghijklmnopqrstuvwxyz"


 --- التشفير ---
def autokey_encrypt(text, key):
    text = "".join([c for c in text.lower() if c.isalpha()])
    key = "".join([c for c in key.lower() if c.isalpha()])
    key_stream = key + text[:len(text) - len(key)]
    return "".join([ALPHABET[(alphabet_lo.index(p) + alphabet_lo.index(kc)) % 26]
                    for p, kc in zip(text, key_stream)])


 --- فك_التشفير ---
def autokey_decrypt(cipher, key):
    cipher = "".join([c for c in cipher.upper() if c.isalpha()])
    key_stream = list(key.lower())
    plain = ""
    for c in cipher:
        k = key_stream.pop(0)
        p_index = (ALPHABET.index(c) - alphabet_lo.index(k)) % 26
        p = alphabet_lo[p_index]
        plain += p
        key_stream.append(p)
    return plain
