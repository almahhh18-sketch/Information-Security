VIGENERE CIPHER

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lo = "abcdefghijklmnopqrstuvwxyz"


# --- التشفير ---
def vigenere_encrypt(text, key):
    text = "".join([c for c in text.lower() if c.isalpha()])
    key = "".join([c for c in key.lower() if c.isalpha()])
    key_stream = (key * ((len(text)//len(key)) + 1))[:len(text)]
    return "".join([ALPHABET[(alphabet_lo.index(p) + alphabet_lo.index(kc)) % 26]
                    for p, kc in zip(text, key_stream)])


# --- فك_التشفير ---
def vigenere_decrypt(cipher, key):
    cipher = "".join([c for c in cipher.upper() if c.isalpha()])
    key = "".join([c for c in key.lower() if c.isalpha()])
    key_stream = (key * ((len(cipher)//len(key)) + 1))[:len(cipher)]
    return "".join([alphabet_lo[(ALPHABET.index(c) - alphabet_lo.index(kc)) % 26]
                    for c, kc in zip(cipher, key_stream)])
