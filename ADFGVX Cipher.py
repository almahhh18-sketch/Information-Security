 ADFGVX CIPHER
   - مصفوفة المفتاح الأول
   - التشفير 

ADFGVX = ["A","D","F","G","V","X"]


 --- مصفوفة_المفتاح ---
def adfgvx_matrix(key=None):
    base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    if key:
        key = "".join([c for c in key.upper() if c.isalnum()])
        seq = []
        for c in key:
            if c not in seq:
                seq.append(c)
        for c in base:
            if c not in seq:
                seq.append(c)
    else:
        seq = list(base)
    return [seq[i*6:(i+1)*6] for i in range(6)]


 --- التشفير ---
def adfgvx_encrypt(text, matrix, key):
    pos = {}
    for r in range(6):
        for c in range(6):
            pos[matrix[r][c]] = (ADFGVX[r], ADFGVX[c])

    text = "".join([c for c in text.upper() if c.isalnum()])
    frac = "".join([pos[c][0] + pos[c][1] for c in text])

    cols = {k: "" for k in key}
    for i, ch in enumerate(frac):
        cols[key[i % len(key)]] += ch

    result = ""
    for k in sorted(cols.keys()):
        result += cols[k]
    return result
